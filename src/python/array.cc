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

struct ZendArray;
static int Array_init(ZendArray *self, PyObject *args, PyObject *kwds);
static PyObject *Array_get(ZendArray *self, PyObject *args);
static PyObject *Array_set(ZendArray *self, PyObject *args);
static PyObject *Array_unset(ZendArray *self, PyObject *args);
static PyObject *Array_count(ZendArray *self, PyObject *args);
static void Array_destroy(ZendArray *self);

// clang-format off
struct ZendArray {
    PyObject_HEAD
    zval array;
};

static PyMethodDef Array_methods[] = {
    {"get", (PyCFunction) Array_get, METH_VARARGS, "Get array item value" },
    {"set", (PyCFunction) Array_set, METH_VARARGS, "Set array item value" },
    {"unset", (PyCFunction) Array_unset, METH_VARARGS, "Set array item value" },
    {"count", (PyCFunction) Array_count, METH_NOARGS, "Get array length" },
    {NULL}  /* Sentinel */
};

static PyTypeObject ZendArrayType = { PyVarObject_HEAD_INIT(NULL, 0) };

//  clang-format on

static void Array_dtor(PyObject *pv) {
    ZendArray *self = (ZendArray *) pv;
    zval_ptr_dtor(&self->array);
    ZVAL_NULL(&self->array);
}

static int Array_init(ZendArray *self, PyObject *args, PyObject *kwds) {
    PyObject *pv = NULL;
    if (!PyArg_ParseTuple(args, "|O", &pv)) {
        return -1;
    }
    if (pv) {
        object2array(pv, &self->array);
    } else {
        array_init(&self->array);
    }
    phpy::php::add_object((PyObject *)self, Array_dtor);
    return 0;
}

static PyObject *Array_get(ZendArray *self, PyObject *args) {
    zval *result;
    PyObject *key;
    if (!PyArg_ParseTuple(args, "O", &key)) {
        return NULL;
    }
    if (PyLong_Check(key)) {
        result = phpy::php::array_get(&self->array, PyLong_AsLong(key));
    } else {
        ssize_t l_key;
        auto skey = phpy::python::string2utf8(key, &l_key);
        result = phpy::php::array_get(&self->array, skey, l_key);
    }
    if (!result) {
        Py_INCREF(Py_None);
        return Py_None;
    }
    return php2py_for_cpython(result);
}

static PyObject *Array_set(ZendArray *self, PyObject *args) {
    PyObject *value;
    PyObject *key;
    if (!PyArg_ParseTuple(args, "OO", &key, &value)) {
        return NULL;
    }
    zval rv;
    py2php(value, &rv);
    if (PyLong_Check(key)) {
        zend_hash_index_update(Z_ARR(self->array), PyLong_AsLong(key), &rv);
    } else {
        ssize_t l_key;
        auto skey = phpy::python::string2utf8(key, &l_key);
        zend_hash_str_update(Z_ARR(self->array), skey, l_key, &rv);
    }
    Py_INCREF(Py_None);
    return Py_None;
}

static PyObject *Array_unset(ZendArray *self, PyObject *args) {
    zend_result result;
    PyObject *key;
    if (!PyArg_ParseTuple(args, "O", &key)) {
        return NULL;
    }
    if (PyLong_Check(key)) {
        result = zend_hash_index_del(Z_ARR(self->array), PyLong_AsLong(key));
    } else {
        ssize_t l_key;
        auto skey = phpy::python::string2utf8(key, &l_key);
        result = zend_hash_str_del(Z_ARR(self->array), skey, l_key);
    }
    if (result == SUCCESS) {
        Py_INCREF(Py_True);
        return Py_True;
    } else {
        Py_INCREF(Py_False);
        return Py_False;
    }
}

static PyObject *Array_count(ZendArray *self, PyObject *args) {
    return PyLong_FromLong(phpy::php::array_count(&self->array));
}

static void Array_destroy(ZendArray *self) {
    zval_ptr_dtor(&self->array);
    Py_TYPE(self)->tp_free((PyObject*) self);
    phpy::php::del_object((PyObject *)self);
}

bool py_module_array_init(PyObject *m) {
    ZendArrayType.tp_name = "zend_array";
    ZendArrayType.tp_basicsize = sizeof(ZendArray);
    ZendArrayType.tp_itemsize = 0;
    ZendArrayType.tp_dealloc = (destructor) Array_destroy;
    ZendArrayType.tp_flags = Py_TPFLAGS_DEFAULT;
    ZendArrayType.tp_doc = PyDoc_STR("zend_array");
    ZendArrayType.tp_methods = Array_methods;
    ZendArrayType.tp_init = (initproc) Array_init;
    ZendArrayType.tp_new = PyType_GenericNew;

    if (PyType_Ready(&ZendArrayType) < 0) {
        return false;
    }
    Py_INCREF(&ZendArrayType);
    if (PyModule_AddObject(m, "Array", (PyObject *) &ZendArrayType) < 0) {
        Py_DECREF(&ZendArrayType);
        Py_DECREF(m);
        return false;
    }
    return true;
}

bool ZendArray_Check(PyObject *pv) {
    return Py_IS_TYPE(pv, &ZendArrayType);
}

zval *zend_array_cast(PyObject *pv) {
    ZendArray *obj = (ZendArray *) pv;
    return &obj->array;
}

namespace phpy {
namespace python {
PyObject *new_array(zval *zv) {
    ZendArray *self = PyObject_New(ZendArray, &ZendArrayType);
    self->array = *zv;
    phpy::php::add_object((PyObject *) self, Array_dtor);
    zval_add_ref(&self->array);
    return (PyObject *)self;
}
PyObject *new_array(PyObject *pv) {
    ZendArray *self = PyObject_New(ZendArray, &ZendArrayType);
    object2array(pv, &self->array);
    phpy::php::add_object((PyObject *) self, Array_dtor);
    return (PyObject *)self;
}
}
}
