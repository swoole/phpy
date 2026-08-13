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
static PyObject *String_bytes(ZendString *self, PyObject *args);
static void String_destroy(ZendString *self);

// clang-format off
struct ZendString {
    PyObject_HEAD
    zval string;
};

static PySequenceMethods String_sq_methods = {};

static PyMethodDef String_methods[] = {
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
    const char *str = NULL;
    size_t len = 0;
    if (!PyArg_ParseTuple(args, "|s#", &str, &len)) {
        PyErr_SetString(PyExc_TypeError, "must supply at least 1 parameter.");
        return -1;
    }
    if (str == NULL) {
        ZVAL_EMPTY_STRING(&self->string);
    } else {
        ZVAL_STRINGL(&self->string, str, len);
    }
    phpy::php::add_object((PyObject *) self, String_dtor);
    return 0;
}

static PyObject *String_str(ZendString *self) {
    return PyUnicode_FromStringAndSize(Z_STRVAL_P(&self->string), Z_STRLEN_P(&self->string));
}

static PyObject *String_bytes(ZendString *self, PyObject *args) {
    return PyBytes_FromStringAndSize(Z_STRVAL_P(&self->string), Z_STRLEN_P(&self->string));
}

static PyObject *String_iadd(ZendString *self, PyObject *o2) {
    size_t s1_len = Z_STRLEN(self->string);
    ssize_t s2_len;
    const char *s2 = phpy::python::string2char_ptr(o2, &s2_len);
    if (s2 == NULL) {
        PyErr_Format(PyExc_TypeError, "can not concat '%s' to zend_string", Py_TypeName(o2));
        return NULL;
    }
    if (UNEXPECTED((size_t) s2_len > ZSTR_MAX_LEN - s1_len)) {
        return PyErr_NoMemory();
    }
    const size_t result_len = s1_len + (size_t) s2_len;
    zend_string *new_zstr = zend_string_extend(Z_STR(self->string), result_len, 0);
    if (!new_zstr) {
        PyErr_SetString(PyExc_MemoryError, "memory alloc fail");
        return NULL;
    }
    Z_STR(self->string) = new_zstr;
    memcpy(Z_STRVAL(self->string) + s1_len, s2, s2_len);
    Z_STRVAL(self->string)[result_len] = '\0';
    Py_INCREF(self);
    return (PyObject *) self;
}

static PyObject *String_add(ZendString *self, PyObject *o2) {
    size_t s1_len = Z_STRLEN(self->string);
    const char *s1 = Z_STRVAL(self->string);
    ssize_t s2_len;
    const char *s2 = phpy::python::string2char_ptr(o2, &s2_len);
    if (s2 == NULL) {
        PyErr_Format(PyExc_TypeError, "can not concat '%s' to zend_string", Py_TypeName(o2));
        return NULL;
    }
    if (UNEXPECTED((size_t) s2_len > ZSTR_MAX_LEN - s1_len)) {
        return PyErr_NoMemory();
    }
    const size_t result_len = s1_len + (size_t) s2_len;
    ZendString *new_str = (ZendString *) phpy::python::new_string(result_len);
    if (UNEXPECTED(new_str == NULL)) {
        return NULL;
    }
    memcpy(Z_STRVAL(new_str->string), s1, s1_len);
    memcpy(Z_STRVAL(new_str->string) + s1_len, s2, s2_len);
    Z_STRVAL(new_str->string)[result_len] = '\0';
    return (PyObject *) new_str;
}

static PyObject *String_compare(PyObject *o1, PyObject *o2, int op) {
    if (op != Py_EQ && op != Py_NE) {
        Py_RETURN_NOTIMPLEMENTED;
    }
    zval *z1 = zend_string_cast(o1);
    ssize_t len;
    const char *val = phpy::python::string2char_ptr(o2, &len);
    if (val == NULL) {
        Py_RETURN_NOTIMPLEMENTED;
    }
    const bool equal = len == (Py_ssize_t) Z_STRLEN_P(z1) && memcmp(Z_STRVAL_P(z1), val, len) == 0;
    if (equal == (op == Py_EQ)) {
        Py_RETURN_TRUE;
    } else {
        Py_RETURN_FALSE;
    }
}

static Py_ssize_t String_len(ZendString *self) {
    return Z_STRLEN_P(&self->string);
}

static PyObject *String_at(ZendString *self, Py_ssize_t offset) {
    if (offset >= (Py_ssize_t) Z_STRLEN_P(&self->string)) {
        PyErr_SetString(PyExc_IndexError, "zend_string index out of range");
        return NULL;
    }
    return PyLong_FromUnsignedLong((unsigned long) Z_STRVAL_P(&self->string)[offset]);
}

static int String_contains(ZendString *self, PyObject *o2) {
    ssize_t len;
    const char *val = phpy::python::string2char_ptr(o2, &len);
    if (val == NULL) {
        PyErr_Format(PyExc_TypeError, "zend_string membership test expects str/bytes, got %s",
                     Py_TypeName(o2));
        return -1;
    }
    if (php_memnstr(Z_STRVAL(self->string), val, len, Z_STRVAL(self->string) + Z_STRLEN(self->string))) {
        return 1;
    }
    return 0;
}

static void String_destroy(ZendString *self) {
    zval_ptr_dtor(&self->string);
    Py_TYPE(self)->tp_free((PyObject *) self);
    phpy::php::del_object((PyObject *) self);
}

bool py_module_string_init(PyObject *m) {
    String_sq_methods.sq_length = (lenfunc) String_len;
    String_sq_methods.sq_item = (ssizeargfunc) String_at;
    String_sq_methods.sq_concat = (binaryfunc) String_add;
    String_sq_methods.sq_contains = (objobjproc) String_contains;
    String_sq_methods.sq_inplace_concat = (binaryfunc) String_iadd;

    ZendStringType.tp_name = "zend_string";
    ZendStringType.tp_basicsize = sizeof(ZendString);
    ZendStringType.tp_itemsize = 0;
    ZendStringType.tp_dealloc = (destructor) String_destroy;
    ZendStringType.tp_as_sequence = &String_sq_methods;
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
    if (self == NULL) {
        return NULL;
    }
    ZVAL_UNDEF(&self->string);
    if (PyByteArray_Check(pv)) {
        ZVAL_STRINGL(&self->string, PyByteArray_AS_STRING(pv), PyByteArray_GET_SIZE(pv));
    } else if (PyBytes_Check(pv)) {
        ZVAL_STRINGL(&self->string, PyBytes_AS_STRING(pv), PyBytes_GET_SIZE(pv));
    } else if (PyUnicode_Check(pv)) {
        zend_string *value = py2zstr(pv);
        if (value == NULL) {
            Py_DECREF(self);
            return NULL;
        }
        ZVAL_STR(&self->string, value);
    } else {
        auto value = PyObject_Str(pv);
        if (value == NULL) {
            Py_DECREF(self);
            return NULL;
        }
        Py_ssize_t sl;
        const char *sv = PyUnicode_AsUTF8AndSize(value, &sl);
        if (sv == NULL) {
            Py_DECREF(value);
            Py_DECREF(self);
            return NULL;
        }
        ZVAL_STRINGL(&self->string, sv, sl);
        Py_DECREF(value);
    }
    phpy::php::add_object((PyObject *) self, String_dtor);
    return (PyObject *) self;
}

/**
 * Return value: New reference.
 */
PyObject *new_string(zval *zv) {
    ZendString *self = PyObject_New(ZendString, &ZendStringType);
    if (self == NULL) {
        return NULL;
    }
    self->string = *zv;
    phpy::php::add_object((PyObject *) self, String_dtor);
    zval_add_ref(&self->string);
    return (PyObject *) self;
}
PyObject *new_string(size_t len) {
    ZendString *self = PyObject_New(ZendString, &ZendStringType);
    if (self == NULL) {
        return NULL;
    }
    ZVAL_STR(&self->string, zend_string_alloc(len, 0));
    Z_STRVAL(self->string)[len] = '\0';
    phpy::php::add_object((PyObject *) self, String_dtor);
    return (PyObject *) self;
}
}  // namespace python
}  // namespace phpy
