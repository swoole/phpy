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

static PyTypeObject ZendReferenceType = { PyVarObject_HEAD_INIT(NULL, 0) };

// clang-format on

static int Reference_init(ZendReference *self, PyObject *args, PyObject *kwds) {
    ZVAL_NEW_REF(&self->reference, &self->value);
    ZVAL_NULL(Z_REFVAL(self->reference));
    return 0;
}

static void Reference_dtor(PyObject *pv) {
    ZendReference *self = (ZendReference *) pv;
    zval_ptr_dtor(&self->reference);
    ZVAL_NULL(&self->reference);
}

static PyObject *Reference_get(ZendReference *self, PyObject *args) {
    return php2py(&self->reference);
}

static void Reference_destroy(ZendReference *self) {
    if (phpy::php::del_object((PyObject *) self)) {
        Reference_dtor((PyObject *) self);
    }
    Py_TYPE(self)->tp_free((PyObject *) self);
}

bool py_module_reference_init(PyObject *m) {
    ZendReferenceType.tp_name = "zend_reference";
    ZendReferenceType.tp_basicsize = sizeof(ZendReference);
    ZendReferenceType.tp_itemsize = 0;
    ZendReferenceType.tp_dealloc = (destructor) Reference_destroy;
    ZendReferenceType.tp_flags = Py_TPFLAGS_DEFAULT;
    ZendReferenceType.tp_doc = PyDoc_STR("zend_reference");
    ZendReferenceType.tp_methods = Reference_methods;
    ZendReferenceType.tp_init = (initproc) Reference_init;
    ZendReferenceType.tp_new = PyType_GenericNew;

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

namespace phpy {
namespace python {
PyObject *new_reference(zval *zv) {
    auto pyobj = php2py(Z_REFVAL_P(zv));
    phpy::php::add_object((PyObject *) pyobj, Reference_dtor);
    return pyobj;
}
}  // namespace python
}  // namespace phpy
