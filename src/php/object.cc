/*
  +----------------------------------------------------------------------+
  | Phpy                                                                 |
  +----------------------------------------------------------------------+
  | This source file is subject to version 2.0 of the Apache license,    |
  | that is bundled with this package in the file LICENSE, and is        |
  | available through the world-wide-web at the following url:           |
  | http://www.apache.org/licenses/LICENSE-2.0.html                      |
  | If you did not receive a copy of the Apache2.0 license and are unable|
  | to obtain it through the world-wide-web, please send a note to       |
  | license@swoole.com so we can mail you a copy immediately.            |
  +----------------------------------------------------------------------+
  | Author: Tianfeng Han  <rango@swoole.com>                             |
  | Copyright: 上海识沃网络科技有限公司                                       |
  +----------------------------------------------------------------------+
 */

#include "phpy.h"
#include "zend_interfaces.h"
BEGIN_EXTERN_C()
#include "stubs/phpy_object_arginfo.h"
END_EXTERN_C()

using phpy::CallObject;
using phpy::python::LockGuard;

zend_class_entry *PyObject_ce;
static zend_object_handlers object_handlers;

struct Object {
    PyObject *object;
    PyObject *iterator;
    PyObject *current;
    uint32_t index;
    zend_object std;
};

static zend_always_inline Object *phpy_object_get_object(zend_object *object) {
    return (Object *) ((char *) object - object_handlers.offset);
}

static zend_always_inline Object *phpy_object_get_object(zval *zobject) {
    return (Object *) ((char *) Z_OBJ_P(zobject) - object_handlers.offset);
}

PyObject *phpy_object_get_handle(zend_object *object) {
    return phpy_object_get_object(object)->object;
}

PyObject *phpy_object_get_handle(zval *zobject) {
    return phpy_object_get_object(zobject)->object;
}

void phpy_object_iterator_reset(zval *object) {
    auto oo = phpy_object_get_object(object);
    if (oo->iterator != NULL) {
        Py_DECREF(oo->iterator);
        oo->iterator = NULL;
    }
    if (oo->current != NULL) {
        Py_DECREF(oo->current);
        oo->current = NULL;
    }
    oo->index = 0;
    // Return value: New reference
    oo->iterator = PyObject_GetIter(oo->object);
    if (oo->iterator == NULL) {
        phpy::php::throw_error_if_occurred();
    } else {
        // Return value: New reference
        oo->current = PyIter_Next(oo->iterator);
        if (oo->current == NULL && PyErr_Occurred()) {
            phpy::php::throw_error_if_occurred();
        }
    }
}

PyObject *phpy_object_iterator_next(zval *object) {
    auto oo = phpy_object_get_object(object);
    if (oo->iterator == NULL) {
        return NULL;
    }
    // Return value: New reference
    if (oo->current != NULL) {
        Py_DECREF(oo->current);
        oo->current = NULL;
    }
    oo->current = PyIter_Next(oo->iterator);
    oo->index++;
    if (oo->current == NULL && PyErr_Occurred()) {
        phpy::php::throw_error_if_occurred();
    }
    return oo->current;
}

bool phpy_object_iterator_valid(zval *object) {
    auto oo = phpy_object_get_object(object);
    return oo->current != NULL;
}

PyObject *phpy_object_iterator_current(zval *object) {
    return phpy_object_get_object(object)->current;
}

uint32_t phpy_object_iterator_index(zval *object) {
    return phpy_object_get_object(object)->index;
}

static zend_object *phpy_object_create_object(zend_class_entry *ce) {
    Object *object_object = (Object *) zend_object_alloc(sizeof(*object_object), ce);

    zend_object_std_init(&object_object->std, ce);
    object_properties_init(&object_object->std, ce);
    object_object->std.handlers = &object_handlers;

    return &object_object->std;
}

static void phpy_object_free_object(zend_object *object) {
    Object *object_object = phpy_object_get_object(object);
    if (object_object->object != NULL) {
        Py_DECREF(object_object->object);
    }
    if (object_object->iterator != NULL) {
        Py_DECREF(object_object->iterator);
    }
    if (object_object->current != NULL) {
        Py_DECREF(object_object->current);
    }
    zend_object_std_dtor(&object_object->std);
}

// zend_object_cast_t returned int in older supported PHP releases and
// zend_result in newer ones. Derive the exact ABI type from Zend instead of
// forcing either signature or casting an incompatible function pointer.
using ObjectCastResult =
    decltype(zend_std_cast_object_tostring(static_cast<zend_object *>(nullptr), static_cast<zval *>(nullptr), 0));

static ObjectCastResult phpy_object_cast_object(zend_object *object, zval *result, int type) {
    if (type != _IS_BOOL) {
        return zend_std_cast_object_tostring(object, result, type);
    }

    PyObject *value = phpy_object_get_handle(object);
    if (UNEXPECTED(value == nullptr)) {
        zend_throw_error(nullptr, "PyObject is not initialized");
        ZVAL_FALSE(result);
        return FAILURE;
    }

    LOCK_GIL();
    const int truth = PyObject_IsTrue(value);
    if (UNEXPECTED(truth < 0)) {
        phpy::php::throw_error_if_occurred();
        ZVAL_FALSE(result);
        return FAILURE;
    }
    ZVAL_BOOL(result, truth);
    return SUCCESS;
}

namespace phpy {
namespace php {
void new_object(zval *zv, PyObject *object) {
    new_object(zv, object, PyObject_ce);
}
void new_object(zval *zv, PyObject *object, zend_class_entry *ce) {
    object_init_ex(zv, ce);
    Py_INCREF(object);
    phpy_object_get_object(zv)->object = object;
}
void new_object_no_addref(zval *zv, PyObject *object) {
    object_init_ex(zv, PyObject_ce);
    phpy_object_get_object(zv)->object = object;
}
PyObject *arg_1(INTERNAL_FUNCTION_PARAMETERS) {
    zval *zk;

    ZEND_PARSE_PARAMETERS_START(1, 1)
    Z_PARAM_ZVAL(zk)
    ZEND_PARSE_PARAMETERS_END_EX(return NULL);

    return php2py(zk);
}
PyObject *arg_1(INTERNAL_FUNCTION_PARAMETERS, zend_class_entry *ce) {
    zval *zk;

    ZEND_PARSE_PARAMETERS_START(1, 1)
    Z_PARAM_OBJECT_OF_CLASS(zk, ce)
    ZEND_PARSE_PARAMETERS_END_EX(return NULL);

    return php2py(zk);
}
}  // namespace php
}  // namespace phpy

using phpy::php::arg_1;

int php_class_object_init(INIT_FUNC_ARGS) {
    zend_class_entry ce;
    INIT_CLASS_ENTRY(ce, "PyObject", class_PyObject_methods);
    PyObject_ce = zend_register_internal_class_ex(&ce, NULL);
    PyObject_ce->ce_flags |= ZEND_ACC_NO_DYNAMIC_PROPERTIES | ZEND_ACC_NOT_SERIALIZABLE;
    zend_class_implements(PyObject_ce, 3, zend_ce_iterator, zend_ce_arrayaccess, zend_ce_countable);

    PyObject_ce->create_object = phpy_object_create_object;

    memcpy(&object_handlers, &std_object_handlers, sizeof(zend_object_handlers));
    object_handlers.offset = XtOffsetOf(Object, std);
    object_handlers.free_obj = phpy_object_free_object;
    object_handlers.cast_object = phpy_object_cast_object;

    return SUCCESS;
}

zend_class_entry *phpy_object_get_ce() {
    return PyObject_ce;
}

void phpy_object_ctor(zval *zobject, PyObject *object) {
    phpy_object_get_object(zobject)->object = object;
}

ZEND_METHOD(PyObject, __construct) {
    zval *zv = NULL;

    ZEND_PARSE_PARAMETERS_START(0, 1)
    Z_PARAM_OPTIONAL
    Z_PARAM_ZVAL(zv)
    ZEND_PARSE_PARAMETERS_END_EX(return);

    LOCK_GIL();
    if (zv == NULL) {
        phpy_object_get_object(ZEND_THIS)->object = Py_None;
        Py_INCREF(Py_None);
    } else {
        phpy_object_get_object(ZEND_THIS)->object = php2py_object(zv);
    }
}

ZEND_METHOD(PyObject, __call) {
    char *name;
    size_t l_name;
    zval *arguments;

    ZEND_PARSE_PARAMETERS_START(2, 2)
    Z_PARAM_STRING(name, l_name)
    Z_PARAM_ARRAY(arguments)
    ZEND_PARSE_PARAMETERS_END_EX(RETURN_FALSE);

    auto object = phpy_object_get_handle(ZEND_THIS);
    LOCK_GIL();
    auto fn = PyObject_GetAttrString(object, name);
    if (fn == NULL) {
        phpy::php::throw_error_if_occurred();
        return;
    }
    ON_SCOPE_EXIT {
        Py_DECREF(fn);
    };
    if (!PyCallable_Check(fn)) {
        PyErr_Format(PyExc_TypeError, "'%.200s' object is not callable", Py_TypeName(fn));
        phpy::php::throw_error_if_occurred();
        return;
    }
    CallObject caller(fn, return_value, arguments);
    caller.call();
}

ZEND_METHOD(PyObject, __get) {
    char *name;
    size_t l_name;

    ZEND_PARSE_PARAMETERS_START(1, 1)
    Z_PARAM_STRING(name, l_name)
    ZEND_PARSE_PARAMETERS_END_EX(RETURN_FALSE);

    phpy_get_attr(ZEND_THIS, name, l_name, return_value);
}

ZEND_METHOD(PyObject, __set) {
    char *name;
    size_t l_name;
    zval *zvalue;

    ZEND_PARSE_PARAMETERS_START(2, 2)
    Z_PARAM_STRING(name, l_name)
    Z_PARAM_ZVAL(zvalue)
    ZEND_PARSE_PARAMETERS_END_EX(RETURN_FALSE);

    auto object = phpy_object_get_handle(ZEND_THIS);
    LOCK_GIL();
    auto value = php2py(zvalue);
    if (value == NULL) {
        phpy::php::throw_error_if_occurred();
        return;
    }
    ON_SCOPE_EXIT {
        Py_DECREF(value);
    };
    if (PyObject_SetAttrString(object, name, value) < 0) {
        phpy::php::throw_error_if_occurred();
    }
}

ZEND_METHOD(PyObject, __unset) {
    char *name;
    size_t l_name;

    ZEND_PARSE_PARAMETERS_START(1, 1)
    Z_PARAM_STRING(name, l_name)
    ZEND_PARSE_PARAMETERS_END_EX(return);

    auto object = phpy_object_get_handle(ZEND_THIS);
    LOCK_GIL();
    if (PyObject_DelAttrString(object, name) < 0) {
        phpy::php::throw_error_if_occurred();
    }
}

ZEND_METHOD(PyObject, __toString) {
    LOCK_GIL();
    phpy::python::string2zval(phpy_object_get_handle(ZEND_THIS), return_value);
}

ZEND_METHOD(PyObject, toArray) {
    ZEND_PARSE_PARAMETERS_NONE();

    phpy_to_array(ZEND_THIS, return_value);
}

ZEND_METHOD(PyObject, toValue) {
    ZEND_PARSE_PARAMETERS_NONE();

    phpy_to_value(ZEND_THIS, return_value);
}

ZEND_METHOD(PyObject, __invoke) {
    int argc = 0;
    zval *argv = NULL;
    HashTable *kwargs;

    ZEND_PARSE_PARAMETERS_START(0, -1)
    Z_PARAM_OPTIONAL
    Z_PARAM_VARIADIC_WITH_NAMED(argv, argc, kwargs)
    ZEND_PARSE_PARAMETERS_END();

    auto object = phpy_object_get_handle(ZEND_THIS);
    LOCK_GIL();
    if (object == NULL) {
        PyErr_SetString(PyExc_RuntimeError, "PyObject is not initialized");
        phpy::php::throw_error_if_occurred();
        return;
    }
    if (!PyCallable_Check(object)) {
        PyErr_Format(PyExc_TypeError, "'%.200s' object is not callable", Py_TypeName(object));
        phpy::php::throw_error_if_occurred();
        return;
    }

    CallObject caller(object, return_value, argc, argv, kwargs);
    caller.call();
}

ZEND_METHOD(PyObject, rewind) {
    LOCK_GIL();
    phpy_object_iterator_reset(ZEND_THIS);
}

ZEND_METHOD(PyObject, next) {
    LOCK_GIL();
    phpy_object_iterator_next(ZEND_THIS);
}

ZEND_METHOD(PyObject, valid) {
    LOCK_GIL();
    RETURN_BOOL(phpy_object_iterator_valid(ZEND_THIS));
}

ZEND_METHOD(PyObject, key) {
    LOCK_GIL();
    RETURN_LONG(phpy_object_iterator_index(ZEND_THIS));
}

ZEND_METHOD(PyObject, current) {
    auto current = phpy_object_iterator_current(ZEND_THIS);
    if (current == NULL) {
        return;
    }
    LOCK_GIL();
    py2php(current, return_value);
}

ZEND_METHOD(PyObject, count) {
    auto object = phpy_object_get_handle(ZEND_THIS);
    LOCK_GIL();
    auto size = PyObject_Size(object);
    if (size < 0) {
        phpy::php::throw_error_if_occurred();
        return;
    }
    RETURN_LONG(size);
}

ZEND_METHOD(PyObject, offsetGet) {
    LOCK_GIL();
    auto pk = arg_1(INTERNAL_FUNCTION_PARAM_PASSTHRU);
    CHECK_ARG(pk);
    auto object = phpy_object_get_handle(ZEND_THIS);
    /**
     * PyObject_GetItem()
     * Return value: New reference
     */
    auto value = PyObject_GetItem(object, pk);
    Py_DECREF(pk);
    if (value == NULL) {
        phpy::php::throw_error_if_occurred();
        return;
    }
    py2php(value, return_value);
    Py_DECREF(value);
}

ZEND_METHOD(PyObject, offsetSet) {
    zval *zv;
    zval *zk;

    ZEND_PARSE_PARAMETERS_START(2, 2)
    Z_PARAM_ZVAL(zk)
    Z_PARAM_ZVAL(zv)
    ZEND_PARSE_PARAMETERS_END_EX(RETURN_FALSE);

    auto object = phpy_object_get_handle(ZEND_THIS);
    LOCK_GIL();
    PyObject *pk = php2py(zk);
    if (pk == NULL) {
        phpy::php::throw_error_if_occurred();
        return;
    }
    ON_SCOPE_EXIT {
        Py_DECREF(pk);
    };
    PyObject *pv = php2py(zv);
    if (pv == NULL) {
        phpy::php::throw_error_if_occurred();
        return;
    }
    ON_SCOPE_EXIT {
        Py_DECREF(pv);
    };
    /**
     * PyObject_SetItem()
     * Increase reference count of the value
     */
    auto value = PyObject_SetItem(object, pk, pv);
    if (value < 0) {
        phpy::php::throw_error_if_occurred();
    }
}

ZEND_METHOD(PyObject, offsetUnset) {
    LOCK_GIL();
    auto pk = arg_1(INTERNAL_FUNCTION_PARAM_PASSTHRU);
    CHECK_ARG(pk);
    auto object = phpy_object_get_handle(ZEND_THIS);
    auto result = PyObject_DelItem(object, pk);
    Py_DECREF(pk);
    if (result < 0) {
        if (PyErr_ExceptionMatches(PyExc_KeyError) || PyErr_ExceptionMatches(PyExc_IndexError)) {
            PyErr_Clear();
            return;
        }
        phpy::php::throw_error_if_occurred();
    }
}

ZEND_METHOD(PyObject, offsetExists) {
    LOCK_GIL();
    auto pk = arg_1(INTERNAL_FUNCTION_PARAM_PASSTHRU);
    CHECK_ARG(pk);
    auto object = phpy_object_get_handle(ZEND_THIS);
    auto value = PyObject_GetItem(object, pk);
    Py_DECREF(pk);
    if (value == NULL) {
        // PHP's isset() returns false for a missing key. Preserve every other
        // Python exception because it indicates a real protocol failure.
        if (PyErr_ExceptionMatches(PyExc_KeyError) || PyErr_ExceptionMatches(PyExc_IndexError)) {
            PyErr_Clear();
            RETURN_FALSE;
        }
        phpy::php::throw_error_if_occurred();
        return;
    }
    RETVAL_BOOL(!Py_IsNone(value));
    Py_DECREF(value);
}
