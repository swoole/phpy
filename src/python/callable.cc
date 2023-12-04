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

struct ZendCallable;
static void Callable_dealloc(ZendCallable *self);
static PyObject *Callable_call(ZendCallable *self, PyObject *args, PyObject *kwds);

// clang-format off
struct ZendCallable {
    PyObject_HEAD
    zval callable;
};

static PyTypeObject ZendCallableType = {
    .ob_base = PyVarObject_HEAD_INIT(NULL, 0)
    .tp_name = "zend_callable",
    .tp_basicsize = sizeof(ZendCallable),
    .tp_itemsize = 0,
    .tp_dealloc = (destructor) Callable_dealloc,
    .tp_call = (ternaryfunc) Callable_call,
    .tp_flags = Py_TPFLAGS_DEFAULT,
    .tp_doc = PyDoc_STR("zend_callable"),
    .tp_new = PyType_GenericNew,
};

//  clang-format on

PyObject* callable2py(zval *zv) {
    ZendCallable *cb = PyObject_New(ZendCallable, &ZendCallableType);
    cb->callable = *zv;
    zval_add_ref(&cb->callable);
    return (PyObject *)cb;
}

zval *zend_callable_cast(PyObject *pv) {
    ZendCallable *obj = (ZendCallable *) pv;
    return &obj->callable;
}

bool ZendCallable_Check(PyObject *pv) {
    return Py_IS_TYPE(pv, &ZendCallableType);
}

static void Callable_dealloc(ZendCallable *self) {
    zval_ptr_dtor(&self->callable);
    Py_TYPE(self)->tp_free((PyObject*) self);
}

static PyObject *Callable_call(ZendCallable *self, PyObject *args, PyObject *kwds) {
    Py_ssize_t TupleSize = PyTuple_Size(args);
    uint32_t argc = TupleSize;
    zval argv[argc];
    tuple2argv(argv, args, TupleSize, 0);
    ON_SCOPE_EXIT {
        release_argv(argc, argv);
    };

    zval retval;
    zend_result result = call_user_function(NULL, NULL, &self->callable, &retval, argc, argv);

    if (result == FAILURE) {
        PyErr_Format(PyExc_NameError, "Function  call failed");
        Py_INCREF(Py_None);
        return Py_None;
    }

    RETURN_PYOBJ(&retval);
}

bool py_module_callable_init(PyObject *m) {
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
