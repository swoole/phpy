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
#include "zend_exceptions.h"
#include "ext/standard/basic_functions.h"

struct ZendCallable;
static void Callable_dealloc(ZendCallable *self);
static PyObject *Callable_call(ZendCallable *self, PyObject *args, PyObject *kwds);

// clang-format off
struct ZendCallable {
    PyObject_HEAD
    zval callable;
    zend_fcall_info_cache cache;
    bool cacheable;
};

static PyTypeObject ZendCallableType = { PyVarObject_HEAD_INIT(NULL, 0) };

// clang-format on

static void Callable_dtor(PyObject *pv) {
    ZendCallable *self = (ZendCallable *) pv;
    zend_release_fcall_info_cache(&self->cache);
    self->cache = {};
    zval_ptr_dtor(&self->callable);
    ZVAL_NULL(&self->callable);
}

static bool Callable_is_cacheable(const zval *callable) {
    if (UNEXPECTED(Z_ISREF_P(callable))) {
        return false;
    }
    if (Z_TYPE_P(callable) != IS_ARRAY) {
        return true;
    }

    // Callable arrays are immutable after their zval is copied unless one of
    // their two components is a reference. In that case PHP code may change
    // the target without replacing this wrapper's array, so it must continue
    // through Zend's dynamic callable resolution path.
    HashTable *values = Z_ARRVAL_P(callable);
    zval *target = zend_hash_index_find(values, 0);
    zval *method = zend_hash_index_find(values, 1);
    return target != nullptr && method != nullptr && !Z_ISREF_P(target) && !Z_ISREF_P(method);
}

namespace phpy {
namespace python {
PyObject *new_callable(const zval *zv) {
    ZendCallable *cb = PyObject_New(ZendCallable, &ZendCallableType);
    cb->callable = *zv;
    zval_add_ref(&cb->callable);
    cb->cache = {};
    cb->cacheable = Callable_is_cacheable(&cb->callable);
    phpy::php::add_object((PyObject *) cb, Callable_dtor);
    return (PyObject *) cb;
}
}  // namespace python
}  // namespace phpy

zval *zend_callable_cast(PyObject *pv) {
    ZendCallable *obj = (ZendCallable *) pv;
    return &obj->callable;
}

bool ZendCallable_Check(PyObject *pv) {
    return Py_IS_TYPE(pv, &ZendCallableType);
}

static void Callable_dealloc(ZendCallable *self) {
    if (phpy::php::del_object((PyObject *) self)) {
        Callable_dtor((PyObject *) self);
    }
    Py_TYPE(self)->tp_free((PyObject *) self);
}

static PyObject *Callable_call(ZendCallable *self, PyObject *args, PyObject *kwds) {
    Py_ssize_t TupleSize = PyTuple_Size(args);
    uint32_t argc = TupleSize;
    zval *argv = new zval[argc];
    phpy::python::tuple2argv(argv, args, TupleSize, 0);
    ON_SCOPE_EXIT {
        phpy::python::release_argv(argc, argv);
        delete[] argv;
    };

    if (EG(exception) != NULL) {
        PyErr_SetString(PyExc_RuntimeError, "Argument conversion failed");
        return NULL;
    }

    zval named_args;
    ZVAL_UNDEF(&named_args);
    if (kwds != NULL && PyDict_Size(kwds) > 0) {
        py2php_scalar(kwds, &named_args);
        if (EG(exception) != NULL) {
            PyErr_SetString(PyExc_RuntimeError, "Keyword argument conversion failed");
            zval_ptr_dtor(&named_args);
            return NULL;
        }
    }
    ON_SCOPE_EXIT {
        if (!Z_ISUNDEF(named_args)) {
            zval_ptr_dtor(&named_args);
        }
    };

    zval retval;
    HashTable *named_params = Z_TYPE(named_args) == IS_ARRAY ? Z_ARRVAL(named_args) : nullptr;
    zend_fcall_info_cache *cache = self->cacheable ? &self->cache : nullptr;
    zend_result result = phpy::php::call_fn(NULL, &self->callable, &retval, argc, argv, named_params, cache);
    if (result == FAILURE) {
        if (EG(exception) && phpy_options.display_exception) {
            zend_exception_error(EG(exception), E_ERROR);
            zend_clear_exception();
        }
        PyErr_Format(PyExc_RuntimeError, "Function call failed");
        return NULL;
    }
    if (PyErr_Occurred()) {
        return NULL;
    }
    RETURN_PYOBJ(&retval);
}

bool py_module_callable_init(PyObject *m) {
    ZendCallableType.tp_name = "zend_callable";
    ZendCallableType.tp_basicsize = sizeof(ZendCallable);
    ZendCallableType.tp_itemsize = 0;
    ZendCallableType.tp_dealloc = (destructor) Callable_dealloc;
    ZendCallableType.tp_call = (ternaryfunc) Callable_call;
    ZendCallableType.tp_flags = Py_TPFLAGS_DEFAULT;
    ZendCallableType.tp_doc = PyDoc_STR("zend_callable");
    ZendCallableType.tp_new = PyType_GenericNew;

    if (PyType_Ready(&ZendCallableType) < 0) {
        return false;
    }
    Py_INCREF(&ZendCallableType);
    if (PyModule_AddObject(m, "Callable", (PyObject *) &ZendCallableType) < 0) {
        Py_DECREF(&ZendCallableType);
        Py_DECREF(m);
        return false;
    }
    return true;
}
