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

struct ZendClass;

static int Class_init(ZendClass *self, PyObject *args, PyObject *kwds);
static void Class_dealloc(ZendClass *self);
static PyObject *Class_new(ZendClass *self, PyObject *args);
static PyObject *Class_get(ZendClass *self, PyObject *args);
static PyObject *Class_set(ZendClass *self, PyObject *args);

// clang-format off
struct ZendClass {
    PyObject_HEAD
    zend_class_entry *ce;
};

static PyMethodDef Class_methods[] = {
    {"new", (PyCFunction) Class_new, METH_VARARGS, "Create an instance" },
    {"get", (PyCFunction) Class_get, METH_VARARGS, "Get class static property" },
    {"set", (PyCFunction) Class_set, METH_VARARGS, "Set class static property" },
    {NULL}  /* Sentinel */
};

static PyTypeObject ZendClassType = {PyVarObject_HEAD_INIT(NULL, 0)};
// clang-format on

bool py_module_class_init(PyObject *m) {
    ZendClassType.tp_name = "zend_class";
    ZendClassType.tp_basicsize = sizeof(ZendClass);
    ZendClassType.tp_itemsize = 0;
    ZendClassType.tp_dealloc = (destructor) Class_dealloc;
    ZendClassType.tp_flags = Py_TPFLAGS_DEFAULT;
    ZendClassType.tp_doc = PyDoc_STR("zend_class");
    ZendClassType.tp_methods = Class_methods;
    ZendClassType.tp_init = (initproc) Class_init;
    ZendClassType.tp_new = PyType_GenericNew;

    if (PyType_Ready(&ZendClassType) < 0) {
        return false;
    }
    Py_INCREF(&ZendClassType);
    if (PyModule_AddObject(m, "Class", (PyObject *) &ZendClassType) < 0) {
        Py_DECREF(&ZendClassType);
        Py_DECREF(m);
        return false;
    }
    return true;
}

static void Class_dtor(PyObject *pv) {
    ZendClass *self = (ZendClass *) pv;
    self->ce = NULL;
}

static int Class_init(ZendClass *self, PyObject *args, PyObject *kwds) {
    const char *name = 0;
    size_t l_name;
    if (!PyArg_ParseTuple(args, "s#", &name, &l_name)) {
        PyErr_SetString(PyExc_TypeError, "must supply at least 1 parameter.");
        return -1;
    }

    zend_string *_class_name = zend_string_init(name, l_name, 0);
    zend_class_entry *ce = zend_lookup_class(_class_name);
    if (ce == NULL) {
        PyErr_Format(PyExc_TypeError, "Class \"%s\" not found", ZSTR_VAL(_class_name));
        zend_string_release(_class_name);
        return -1;
    }
    zend_string_release(_class_name);
    self->ce = ce;
    phpy::php::add_object((PyObject *) self, Class_dtor);
    return 0;
}

static PyObject *Class_new(ZendClass *self, PyObject *args) {
    if (self->ce == NULL) {
        PyErr_SetString(PyExc_RuntimeError, "not initialized or life cycle has ended");
        return NULL;
    }
    return object_create(self->ce, args, PyTuple_Size(args), 0);
}

static void Class_dealloc(ZendClass *self) {
    if (phpy::php::del_object((PyObject *) self)) {
        self->ce = NULL;
    }
    Py_TYPE(self)->tp_free((PyObject *) self);
}

static PyObject *Class_get(ZendClass *self, PyObject *args) {
    if (self->ce == NULL) {
        PyErr_SetString(PyExc_RuntimeError, "not initialized or life cycle has ended");
        return NULL;
    }
    char *name;
    size_t l_name;
    if (!PyArg_ParseTuple(args, "s#", &name, &l_name)) {
        return NULL;
    }

    zval *retval;
    zend_first_try {
        retval = zend_read_static_property(self->ce, name, l_name, 0);
    }
    zend_catch {
        Py_INCREF(Py_None);
        return Py_None;
    }
    zend_end_try();

    RETURN_PYOBJ(retval);
}

static PyObject *Class_set(ZendClass *self, PyObject *args) {
    if (self->ce == NULL) {
        PyErr_SetString(PyExc_RuntimeError, "not initialized or life cycle has ended");
        return NULL;
    }
    char *name;
    size_t l_name;
    PyObject *value;
    if (!PyArg_ParseTuple(args, "s#O", &name, &l_name, &value)) {
        return NULL;
    }

    zval rv;
    py2php(value, &rv);

    if (zend_update_static_property(self->ce, name, l_name, &rv) == SUCCESS) {
        Py_INCREF(Py_True);
        return Py_True;
    } else {
        Py_INCREF(Py_False);
        return Py_False;
    }
}
