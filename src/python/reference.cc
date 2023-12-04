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

struct ZendReference;
static int Reference_init(ZendReference *self, PyObject *args, PyObject *kwds);
static PyObject *Reference_get(ZendReference *self, PyObject *args);
static void Reference_destroy(ZendReference *self);

// clang-format off
struct ZendReference {
    PyObject_HEAD
    zval reference;
    zval value;
};

static PyMethodDef Reference_methods[] = {
    {"get", (PyCFunction) Reference_get, METH_VARARGS, "Get referenced value" },
    {NULL}  /* Sentinel */
};

static PyTypeObject ZendReferenceType = {
    .ob_base = PyVarObject_HEAD_INIT(NULL, 0)
    .tp_name = "zend_reference",
    .tp_basicsize = sizeof(ZendReference),
    .tp_itemsize = 0,
    .tp_dealloc = (destructor) Reference_destroy,
    .tp_flags = Py_TPFLAGS_DEFAULT,
    .tp_doc = PyDoc_STR("zend_reference"),
    .tp_methods = Reference_methods,
    .tp_init = (initproc) Reference_init,
    .tp_new = PyType_GenericNew,
};

//  clang-format on

static int Reference_init(ZendReference *self, PyObject *args, PyObject *kwds) {
    ZVAL_NEW_REF(&self->reference, &self->value);
    ZVAL_NULL(Z_REFVAL(self->reference));
    return 0;
}

static PyObject *Reference_get(ZendReference *self, PyObject *args) {
    return php2py(&self->reference);
}

static void Reference_destroy(ZendReference *self) {
    zval_ptr_dtor(&self->reference);
    Py_TYPE(self)->tp_free((PyObject*) self);
}

bool py_module_reference_init(PyObject *m) {
    if (PyType_Ready(&ZendReferenceType) < 0) {
        return false;
    }
    Py_INCREF(&ZendReferenceType);
    if (PyModule_AddObject(m, "Reference", (PyObject *) &ZendReferenceType) < 0) {
        Py_DECREF(&ZendReferenceType);
        Py_DECREF(m);
        return false;
    }
    return true;
}

bool ZendReference_Check(PyObject *pv) {
    return Py_IS_TYPE(pv, &ZendReferenceType);
}

zval *zend_reference_cast(PyObject *pv) {
    ZendReference *obj = (ZendReference *) pv;
    return &obj->reference;
}

PyObject *reference2py(zval *zv) {
    return php2py(Z_REFVAL_P(zv));
}
