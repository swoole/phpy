/*
  +----------------------------------------------------------------------+
  | Phpy                                                                 |
  +----------------------------------------------------------------------+
  | This source file is subject to version 2.0 of the Apache license,    |
  | that is bundled with this package in the file LICENSE.               |
  +----------------------------------------------------------------------+
 */

#include "phpy.h"
#include "zend_exceptions.h"

struct ZendIterator {
    PyObject_HEAD zend_object_iterator *iterator;
    bool started;
    bool needs_advance;
    bool exhausted;
};

static PyTypeObject ZendIteratorType = {PyVarObject_HEAD_INIT(NULL, 0)};

/**
 * Move a pending PHP exception across the language boundary. Keeping both a
 * Zend and a Python exception active at once leaves each VM with ambiguous
 * ownership, so the original PHP exception is converted and then cleared.
 */
static bool Iterator_translate_exception() {
    zend_object *exception = EG(exception);
    if (exception == nullptr) {
        return false;
    }

    zval rv;
    ZVAL_UNDEF(&rv);
    zval *value = zend_read_property(exception->ce, exception, ZEND_STRL("message"), true, &rv);
    zend_string *message = value == nullptr ? nullptr : zval_get_string(value);

    if (message != nullptr) {
        PyErr_SetString(PyExc_RuntimeError, ZSTR_VAL(message));
        zend_string_release(message);
    } else {
        PyErr_SetString(PyExc_RuntimeError, "PHP iterator raised an exception");
    }
    if (value == &rv) {
        zval_ptr_dtor(&rv);
    }
    zend_clear_exception();
    return true;
}

static void Iterator_dtor(PyObject *object) {
    ZendIterator *self = (ZendIterator *) object;
    if (self->iterator != nullptr) {
        zend_iterator_dtor(self->iterator);
        self->iterator = nullptr;
    }
}

static void Iterator_destroy(ZendIterator *self) {
    phpy::python::destroy_wrapper(self, Iterator_dtor);
}

static PyObject *Iterator_iter(ZendIterator *self) {
    Py_INCREF(self);
    return (PyObject *) self;
}

static bool Iterator_start(ZendIterator *self) {
    self->started = true;
    self->iterator->index = 0;
    if (self->iterator->funcs->rewind != nullptr) {
        self->iterator->funcs->rewind(self->iterator);
    }
    return !Iterator_translate_exception();
}

static PyObject *Iterator_next(ZendIterator *self) {
    if (self->exhausted) {
        return nullptr;
    }
    if (self->iterator == nullptr) {
        PyErr_SetString(PyExc_RuntimeError, "PHP iterator life cycle has ended");
        return nullptr;
    }

    if (!self->started && !Iterator_start(self)) {
        return nullptr;
    }

    // PHP advances after the yielded value has been consumed. Delaying the
    // move until the next Python next() call preserves generator side effects
    // and exception timing.
    if (self->needs_advance) {
        self->needs_advance = false;
        self->iterator->funcs->move_forward(self->iterator);
        if (Iterator_translate_exception()) {
            return nullptr;
        }
    }

    if (self->iterator->funcs->valid(self->iterator) != SUCCESS) {
        if (Iterator_translate_exception()) {
            return nullptr;
        }
        self->exhausted = true;
        return nullptr;
    }
    if (Iterator_translate_exception()) {
        return nullptr;
    }

    zval *value = self->iterator->funcs->get_current_data(self->iterator);
    if (Iterator_translate_exception()) {
        return nullptr;
    }
    if (value == nullptr) {
        PyErr_SetString(PyExc_RuntimeError, "PHP iterator returned no current value");
        return nullptr;
    }

    PyObject *result = php2py(value);
    if (result != nullptr) {
        self->needs_advance = true;
    }
    return result;
}

namespace phpy {
namespace python {
PyObject *new_iterator(zval *zv) {
    zend_class_entry *ce = Z_OBJCE_P(zv);
    zend_object_iterator *iterator = ce->get_iterator(ce, zv, 0);
    if (iterator == nullptr || EG(exception) != nullptr) {
        if (iterator != nullptr) {
            zend_iterator_dtor(iterator);
        }
        Iterator_translate_exception();
        if (!PyErr_Occurred()) {
            PyErr_Format(PyExc_TypeError, "Object of type %s did not create an Iterator", ZSTR_VAL(ce->name));
        }
        return nullptr;
    }

    ZendIterator *self = PyObject_New(ZendIterator, &ZendIteratorType);
    if (self == nullptr) {
        zend_iterator_dtor(iterator);
        return nullptr;
    }
    self->iterator = iterator;
    self->started = false;
    self->needs_advance = false;
    self->exhausted = false;
    phpy::php::add_object((PyObject *) self, Iterator_dtor);
    return (PyObject *) self;
}
}  // namespace python
}  // namespace phpy

bool py_module_iterator_init(PyObject *m) {
    ZendIteratorType.tp_name = "zend_iterator";
    ZendIteratorType.tp_basicsize = sizeof(ZendIterator);
    ZendIteratorType.tp_itemsize = 0;
    ZendIteratorType.tp_dealloc = (destructor) Iterator_destroy;
    ZendIteratorType.tp_flags = Py_TPFLAGS_DEFAULT;
    ZendIteratorType.tp_doc = PyDoc_STR("PHP Traversable iterator");
    ZendIteratorType.tp_iter = (getiterfunc) Iterator_iter;
    ZendIteratorType.tp_iternext = (iternextfunc) Iterator_next;

    return phpy::python::register_python_type(m, &ZendIteratorType, "Iterator");
}
