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
static PyObject *Array_append(ZendArray *self, PyObject *args);
static PyObject *Array_count(ZendArray *self);
static PyObject *Array_collect(ZendArray *self);
static PyObject *Array_is_list(ZendArray *self);
static void Array_destroy(ZendArray *self);

// clang-format off
struct ZendArray {
    PyObject_HEAD
    zval array;
    HashPosition pos;
};

static PyMappingMethods Array_mp_methods = {};

static PyMethodDef Array_methods[] = {
    {"get", (PyCFunction) Array_get, METH_VARARGS, "Get array item value" },
    {"set", (PyCFunction) Array_set, METH_VARARGS, "Set array item value" },
    {"unset", (PyCFunction) Array_unset, METH_VARARGS, "Set array item value" },
    {"count", (PyCFunction) Array_count, METH_NOARGS, "Get array length" },
    {"collect", (PyCFunction) Array_collect, METH_NOARGS, "Convert array to dict/list" },
    {"is_list", (PyCFunction) Array_is_list, METH_NOARGS, "Check if the array is list" },
    {"append", (PyCFunction) Array_append, METH_VARARGS, "Append element to array" },
    {NULL}  /* Sentinel */
};

static PyTypeObject ZendArrayType = { PyVarObject_HEAD_INIT(NULL, 0) };

// clang-format on

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
    phpy::php::add_object((PyObject *) self, Array_dtor);
    return 0;
}

static PyObject *Array_getitem(ZendArray *self, PyObject *key) {
    zval *result;
    if (PyLong_Check(key)) {
        result = phpy::php::array_get(&self->array, PyLong_AsLong(key));
    } else {
        phpy::StrObject dkey(key);
        result = phpy::php::array_get(&self->array, dkey.val(), dkey.len());
    }
    if (!result) {
        Py_RETURN_NONE;
    }
    return php2py_object(result);
}

static PyObject *Array_get(ZendArray *self, PyObject *args) {
    PyObject *key;
    if (!PyArg_ParseTuple(args, "O", &key)) {
        return NULL;
    }
    return Array_getitem(self, key);
}

static bool Array_delitem(ZendArray *self, PyObject *key) {
    zend_result result;
    if (PyLong_Check(key)) {
        result = zend_hash_index_del(Z_ARR(self->array), PyLong_AsLong(key));
    } else {
        phpy::StrObject dkey(key);
        result = zend_hash_str_del(Z_ARR(self->array), dkey.val(), dkey.len());
    }
    return result == SUCCESS;
}

static int Array_setitem(ZendArray *self, PyObject *key, PyObject *value) {
    // value be set to NULL to delete an item
    if (value == NULL) {
        return Array_delitem(self, key) ? 0 : -1;
    }
    zval rv;
    py2php(value, &rv);
    zval *result;
    if (PyLong_Check(key)) {
        result = zend_hash_index_update(Z_ARR(self->array), PyLong_AsLong(key), &rv);
    } else {
        phpy::StrObject dkey(key);
        result = zend_hash_str_update(Z_ARR(self->array), dkey.val(), dkey.len(), &rv);
    }
    return result == NULL ? -1 : 0;
}

static PyObject *Array_set(ZendArray *self, PyObject *args) {
    PyObject *value;
    PyObject *key;
    if (!PyArg_ParseTuple(args, "OO", &key, &value)) {
        return NULL;
    }
    if (Array_setitem(self, key, value) == 0) {
        Py_RETURN_TRUE;
    } else {
        Py_RETURN_FALSE;
    }
}

static PyObject *Array_append(ZendArray *self, PyObject *args) {
    PyObject *value;
    if (!PyArg_ParseTuple(args, "O", &value)) {
        return NULL;
    }
    zval rv;
    py2php(value, &rv);
    if (add_next_index_zval(&self->array, &rv) == SUCCESS) {
        Py_RETURN_TRUE;
    } else {
        Py_RETURN_FALSE;
    }
}

static PyObject *Array_unset(ZendArray *self, PyObject *args) {
    PyObject *key;
    if (!PyArg_ParseTuple(args, "O", &key)) {
        return NULL;
    }
    if (Array_delitem(self, key)) {
        Py_RETURN_TRUE;
    } else {
        Py_RETURN_FALSE;
    }
}

static PyObject *Array_count(ZendArray *self) {
    return PyLong_FromLong(phpy::php::array_count(&self->array));
}

static Py_ssize_t Array_len(ZendArray *self) {
    return phpy::php::array_count(&self->array);
}

static PyObject *Array_collect(ZendArray *self) {
    if (zend_array_is_list(Z_ARRVAL(self->array))) {
        return array2list(Z_ARRVAL(self->array));
    } else {
        return array2dict(Z_ARRVAL(self->array));
    }
}

static PyObject *Array_is_list(ZendArray *self) {
    if (zend_array_is_list(Z_ARRVAL(self->array))) {
        Py_RETURN_TRUE;
    } else {
        Py_RETURN_FALSE;
    }
}

static PyObject *Array_iter(ZendArray *self) {
    zend_hash_internal_pointer_reset_ex(Z_ARRVAL(self->array), &self->pos);
    Py_INCREF(self);
    return (PyObject *) self;
}

static PyObject *Array_next(ZendArray *self) {
    int keytype;
    zend_string *sval;
    zend_ulong lval = 0;

    keytype = zend_hash_get_current_key_ex(Z_ARRVAL(self->array), &sval, &lval, &self->pos);
    zend_hash_move_forward_ex(Z_ARRVAL(self->array), &self->pos);

    if (HASH_KEY_IS_STRING == keytype) {
        return PyUnicode_FromStringAndSize(ZSTR_VAL(sval), ZSTR_LEN(sval));
    } else if (HASH_KEY_IS_LONG == keytype) {
        return PyLong_FromLong(lval);
    } else if (HASH_KEY_NON_EXISTENT == keytype) {
        return NULL;
    } else {
        PyErr_SetString(PyExc_RuntimeError, "zend_array iterator error");
        return NULL;
    }
}

static void Array_destroy(ZendArray *self) {
    if (phpy::php::del_object((PyObject *) self)) {
        zval_ptr_dtor(&self->array);
        ZVAL_NULL(&self->array);
    }
    Py_TYPE(self)->tp_free((PyObject *) self);
}

bool py_module_array_init(PyObject *m) {
    Array_mp_methods.mp_length = (lenfunc) Array_len;
    Array_mp_methods.mp_subscript = (binaryfunc) Array_getitem;
    Array_mp_methods.mp_ass_subscript = (objobjargproc) Array_setitem;

    ZendArrayType.tp_name = "zend_array";
    ZendArrayType.tp_basicsize = sizeof(ZendArray);
    ZendArrayType.tp_itemsize = 0;
    ZendArrayType.tp_dealloc = (destructor) Array_destroy;
    ZendArrayType.tp_as_mapping = &Array_mp_methods;
    ZendArrayType.tp_flags = Py_TPFLAGS_DEFAULT;
    ZendArrayType.tp_doc = PyDoc_STR("zend_array");
    ZendArrayType.tp_methods = Array_methods;
    ZendArrayType.tp_init = (initproc) Array_init;
    ZendArrayType.tp_new = PyType_GenericNew;
    ZendArrayType.tp_iter = (getiterfunc) Array_iter;
    ZendArrayType.tp_iternext = (iternextfunc) Array_next;

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
    return (PyObject *) self;
}
PyObject *new_array(PyObject *pv) {
    ZendArray *self = PyObject_New(ZendArray, &ZendArrayType);
    object2array(pv, &self->array);
    phpy::php::add_object((PyObject *) self, Array_dtor);
    return (PyObject *) self;
}
}  // namespace python
}  // namespace phpy
