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

struct ZendString;
static int String_init(ZendString *self, PyObject *args, PyObject *kwds);
static PyObject *String_len(ZendString *self, PyObject *args);
static PyObject *String_bytes(ZendString *self, PyObject *args);
static PyObject *String_compare(PyObject *o1, PyObject *o2, int op);
static PyObject *String_str(ZendString *self);
static void String_destroy(ZendString *self);

// clang-format off
struct ZendString {
    PyObject_HEAD
    zval string;
};

static PyMethodDef String_methods[] = {
    {"len", (PyCFunction) String_len, METH_NOARGS, "Get string length" },
    {"__bytes__", (PyCFunction) String_bytes, METH_NOARGS, "Convert to bytes" },
    {NULL}  /* Sentinel */
};

static PyTypeObject ZendStringType = { PyVarObject_HEAD_INIT(NULL, 0) };

// clang-format on

static void String_dtor(PyObject *pv) {
    ZendString *self = (ZendString *) pv;
    zval_ptr_dtor(&self->string);
    ZVAL_NULL(&self->string);
}

static int String_init(ZendString *self, PyObject *args, PyObject *kwds) {
    const char *str;
    size_t len;
    if (!PyArg_ParseTuple(args, "s#", &str, &len)) {
        PyErr_SetString(PyExc_TypeError, "must supply at least 1 parameter.");
        return -1;
    }
    ZVAL_STRINGL(&self->string, str, len);
    phpy::php::add_object((PyObject *) self, String_dtor);
    return 0;
}

static PyObject *String_str(ZendString *self) {
    return PyUnicode_FromStringAndSize(Z_STRVAL_P(&self->string), Z_STRLEN_P(&self->string));
}

static PyObject *String_bytes(ZendString *self, PyObject *args) {
    return PyBytes_FromStringAndSize(Z_STRVAL_P(&self->string), Z_STRLEN_P(&self->string));
}

static PyObject *String_compare(PyObject *o1, PyObject *o2, int op) {
    if (op != Py_EQ) {
        Py_RETURN_NOTIMPLEMENTED;
    }
    bool equals;
    zval *z1 = zend_string_cast(o1);
    if (ZendString_Check(o2)) {
        zval *z2 = zend_string_cast(o2);
        equals = zend_string_equal_content(Z_STR_P(z1), Z_STR_P(z2));
    } else if (PyByteArray_Check(o2)) {
        const char *val = PyByteArray_AS_STRING(o2);
        size_t len = PyByteArray_GET_SIZE(o2);
        equals = (len == Z_STRLEN_P(z1) && memcmp(Z_STRVAL_P(z1), val, len) == 0);
    } else if (PyBytes_Check(o2)) {
        const char *val = PyBytes_AS_STRING(o2);
        size_t len = PyBytes_GET_SIZE(o2);
        equals = (len == Z_STRLEN_P(z1) && memcmp(Z_STRVAL_P(z1), val, len) == 0);
    } else if (PyUnicode_Check(o2)) {
        Py_ssize_t len;
        const char *val = PyUnicode_AsUTF8AndSize(o2, &len);
        equals = (len == (Py_ssize_t) Z_STRLEN_P(z1) && memcmp(Z_STRVAL_P(z1), val, len) == 0);
    } else {
        Py_RETURN_NOTIMPLEMENTED;
    }
    if (equals) {
        Py_RETURN_TRUE;
    } else {
        Py_RETURN_FALSE;
    }
}

static PyObject *String_len(ZendString *self, PyObject *args) {
    return PyLong_FromLong(Z_STRLEN_P(&self->string));
}

static void String_destroy(ZendString *self) {
    zval_ptr_dtor(&self->string);
    Py_TYPE(self)->tp_free((PyObject *) self);
    phpy::php::del_object((PyObject *) self);
}

bool py_module_string_init(PyObject *m) {
    ZendStringType.tp_name = "zend_string";
    ZendStringType.tp_basicsize = sizeof(ZendString);
    ZendStringType.tp_itemsize = 0;
    ZendStringType.tp_dealloc = (destructor) String_destroy;
    ZendStringType.tp_str = (reprfunc) String_str;
    ZendStringType.tp_flags = Py_TPFLAGS_DEFAULT;
    ZendStringType.tp_doc = PyDoc_STR("zend_string");
    ZendStringType.tp_richcompare = (richcmpfunc) String_compare;
    ZendStringType.tp_methods = String_methods;
    ZendStringType.tp_init = (initproc) String_init;
    ZendStringType.tp_new = PyType_GenericNew;

    if (PyType_Ready(&ZendStringType) < 0) {
        return false;
    }
    Py_INCREF(&ZendStringType);
    if (PyModule_AddObject(m, "String", (PyObject *) &ZendStringType) < 0) {
        Py_DECREF(&ZendStringType);
        Py_DECREF(m);
        return false;
    }
    return true;
}

bool ZendString_Check(PyObject *pv) {
    return Py_IS_TYPE(pv, &ZendStringType);
}

zval *zend_string_cast(PyObject *pv) {
    ZendString *obj = (ZendString *) pv;
    return &obj->string;
}

namespace phpy {
namespace python {
PyObject *new_string(PyObject *pv) {
    ZendString *self = PyObject_New(ZendString, &ZendStringType);
    if (PyByteArray_Check(pv)) {
        ZVAL_STRINGL(&self->string, PyByteArray_AS_STRING(pv), PyByteArray_GET_SIZE(pv));
    } else if (PyBytes_Check(pv)) {
        ZVAL_STRINGL(&self->string, PyBytes_AS_STRING(pv), PyBytes_GET_SIZE(pv));
    } else if (PyUnicode_Check(pv)) {
        ZVAL_STR(&self->string, py2zstr(pv));
    } else {
        auto value = PyObject_Str(pv);
        if (value != NULL) {
            Py_ssize_t sl;
            const char *sv = PyUnicode_AsUTF8AndSize(value, &sl);
            ZVAL_STRINGL(&self->string, sv, sl);
            Py_DECREF(value);
        } else {
            PyErr_Print();
            zend_throw_error(NULL, "PyObject<%s> has no attribute '__str__'", Py_TYPE(pv)->tp_name);
        }
    }
    return (PyObject *) self;
}
PyObject *new_string(zval *zv) {
    ZendString *self = PyObject_New(ZendString, &ZendStringType);
    self->string = *zv;
    phpy::php::add_object((PyObject *) self, String_dtor);
    zval_add_ref(&self->string);
    return (PyObject *) self;
}
}  // namespace python
}  // namespace phpy
