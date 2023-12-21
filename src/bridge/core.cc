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

BEGIN_EXTERN_C()
#include "ext/standard/php_var.h"
END_EXTERN_C()
#include "zend_exceptions.h"

using phpy::CallObject;

static void (*py2php_fn)(PyObject *pv, zval *zv);
static void py2php_object_impl(PyObject *pv, zval *zv);
static void py2php_scalar_impl(PyObject *pv, zval *zv);

static bool py2php_base_type(PyObject *pv, zval *zv);
static void iterator2array(PyObject *pv, zval *zv);

static inline void sequence2array(PyObject *pv, zval *zv) {
    iterator2array(pv, zv);
}

static inline void set2array(PyObject *pv, zval *zv) {
    iterator2array(pv, zv);
}

static void dict2array(PyObject *pv, zval *zv);

static void py2php_object_impl(PyObject *pv, zval *zv) {
    if (py2php_base_type(pv, zv)) {
        return;
    }
    if (PyUnicode_Check(pv)) {
        phpy::php::new_str(zv, pv);
    } else if (PyList_Check(pv)) {
        phpy::php::new_list(zv, pv);
    } else if (PyTuple_Check(pv)) {
        phpy::php::new_tuple(zv, pv);
    } else if (PySet_Check(pv)) {
        phpy::php::new_set(zv, pv);
    } else if (PyDict_Check(pv)) {
        phpy::php::new_dict(zv, pv);
    } else if (PyModule_Check(pv)) {
        phpy::php::new_module(zv, pv);
    } else if (PyType_Check(pv)) {
        phpy::php::new_type(zv, pv);
    } else if (PyIter_Check(pv)) {
        phpy::php::new_iter(zv, pv);
    } else {
        phpy::php::new_object(zv, pv);
    }
}

static void py2php_scalar_impl(PyObject *pv, zval *zv) {
    if (py2php_base_type(pv, zv)) {
        return;
    }
    if (PyByteArray_Check(pv)) {
        ZVAL_STRINGL(zv, PyByteArray_AS_STRING(pv), PyByteArray_GET_SIZE(pv));
    } else if (PyBytes_Check(pv)) {
        ZVAL_STRINGL(zv, PyBytes_AS_STRING(pv), PyBytes_GET_SIZE(pv));
    } else if (PyUnicode_Check(pv)) {
        ZVAL_STR(zv, py2zstr(pv));
    } else if (PyList_Check(pv)) {
        sequence2array(pv, zv);
    } else if (PyRange_Check(pv)) {
        sequence2array(pv, zv);
    } else if (PyTuple_Check(pv)) {
        sequence2array(pv, zv);
    } else if (PyDict_Check(pv)) {
        dict2array(pv, zv);
    } else if (PySet_Check(pv)) {
        set2array(pv, zv);
    } else {
        phpy::php::new_object(zv, pv);
    }
}

void py2php_scalar(PyObject *pv, zval *zv) {
    py2php_fn = py2php_scalar_impl;
    py2php_fn(pv, zv);
}

void py2php(PyObject *pv, zval *zv) {
    py2php_fn = py2php_object_impl;
    py2php_fn(pv, zv);
}

PyObject *py2py_scalar(PyObject *pv) {
    if (PyDict_Check(pv) || PySet_Check(pv) || PyList_Check(pv) || PyTuple_Check(pv)) {
        pv = phpy::python::new_array(pv);
    } else if (PyByteArray_Check(pv) || PyBytes_Check(pv) || PyUnicode_Check(pv)) {
        pv = phpy::python::new_string(pv);
    } else {
        Py_INCREF(pv);
    }
    return pv;
}

void object2array(PyObject *pv, zval *zv) {
    py2php_fn = py2php_object_impl;
    if (PyDict_Check(pv)) {
        dict2array(pv, zv);
    } else {
        iterator2array(pv, zv);
    }
}

zend_string *py2zstr(PyObject *pv) {
    Py_ssize_t sl;
    const char *sv = PyUnicode_AsUTF8AndSize(pv, &sl);
    return zend_string_init(sv, sl, 0);
}

void long2long(PyObject *pv, zval *zv) {
    int overflow;
    auto lval = PyLong_AsLongAndOverflow(pv, &overflow);
    if (overflow == 0) {
        ZVAL_LONG(zv, lval);
    } else {
        ssize_t len;
        auto s = PyObject_Str(pv);
        const char *sval = phpy::python::string2utf8(s, &len);
        ZVAL_STRINGL(zv, sval, len);
        Py_DECREF(s);
    }
}

PyObject *long2long(zval *zv) {
    PyObject *pv;
    if (Z_TYPE_P(zv) == IS_LONG) {
        pv = PyLong_FromLong(Z_LVAL_P(zv));
    } else if (Z_TYPE_P(zv) == IS_DOUBLE) {
        pv = PyLong_FromDouble(Z_DVAL_P(zv));
    } else {
        zend_string *s = zval_get_string(zv);
        pv = string2py(s);
        zend_string_release(s);
    }
    return pv;
}

static bool py2php_base_type(PyObject *pv, zval *zv) {
    if (PyBool_Check(pv)) {
        ZVAL_BOOL(zv, Py_IsTrue(pv));
    } else if (Py_IsNone(pv)) {
        ZVAL_NULL(zv);
    } else if (PyLong_Check(pv)) {
        long2long(pv, zv);
    } else if (PyFloat_Check(pv)) {
        ZVAL_DOUBLE(zv, PyFloat_AsDouble(pv));
    } else if (ZendObject_Check(pv)) {
        ZVAL_ZVAL(zv, zend_object_cast(pv), 1, 0);
    } else if (ZendReference_Check(pv)) {
        ZVAL_COPY(zv, zend_reference_cast(pv));
    } else if (ZendResource_Check(pv)) {
        ZVAL_COPY(zv, zend_reference_cast(pv));
    } else if (ZendString_Check(pv)) {
        ZVAL_COPY(zv, zend_string_cast(pv));
    } else if (ZendArray_Check(pv)) {
        ZVAL_COPY(zv, zend_array_cast(pv));
    } else {
        return false;
    }
    return true;
}

PyObject *array2list(zend_array *ht) {
    zval *current;
    PyObject *list = PyList_New(0);
    ZEND_HASH_FOREACH_VAL(ht, current) {
        PyList_Append(list, php2py(current));
    }
    ZEND_HASH_FOREACH_END();
    return list;
}

PyObject *array2set(zend_array *ht) {
    zval *current;
    PyObject *pset = PySet_New(0);
    ZEND_HASH_FOREACH_VAL(ht, current) {
        PySet_Add(pset, php2py(current));
    }
    ZEND_HASH_FOREACH_END();
    return pset;
}

static void iterator2array(PyObject *pv, zval *zv) {
    PyObject *iter = PyObject_GetIter(pv);
    array_init(zv);
    while (true) {
        PyObject *next = PyIter_Next(iter);
        if (!next) {
            break;
        }
        zval item;
        py2php_fn(next, &item);
        add_next_index_zval(zv, &item);
    }
    Py_DECREF(iter);
}

PyObject *array2dict(zend_array *ht) {
    uint32_t index;
    zend_string *key;
    zval *value;
    PyObject *dict = PyDict_New();
    ZEND_HASH_FOREACH_KEY_VAL(ht, index, key, value) {
        PyObject *dk;
        if (key) {
            dk = PyUnicode_FromStringAndSize(ZSTR_VAL(key), ZSTR_LEN(key));
        } else {
            dk = PyLong_FromLong(index);
        }
        PyDict_SetItem(dict, dk, php2py(value));
    }
    ZEND_HASH_FOREACH_END();
    return dict;
}

static void dict2array(PyObject *pv, zval *zv) {
    PyObject *iter = PyObject_GetIter(pv);
    array_init(zv);
    while (true) {
        PyObject *next = PyIter_Next(iter);
        if (!next) {
            break;
        }
        auto value = PyDict_GetItem(pv, next);
        zval item;
        py2php_fn(value, &item);

        ssize_t len;
        const char *key = phpy::python::string2utf8(next, &len);
        add_assoc_zval_ex(zv, key, len, &item);
    }
    Py_DECREF(iter);
}

static PyObject *array2py(zval *zv) {
    zend_array *ht = Z_ARRVAL_P(zv);
    if (zend_array_is_list(ht)) {
        return array2list(ht);
    } else {
        return array2dict(ht);
    }
}

PyObject *php2py(zval *zv) {
    switch (Z_TYPE_P(zv)) {
    case IS_NULL:
        Py_INCREF(Py_None);
        return Py_None;
    case IS_TRUE:
        Py_INCREF(Py_True);
        return Py_True;
    case IS_FALSE:
        Py_INCREF(Py_False);
        return Py_False;
    case IS_LONG:
        return PyLong_FromLong(Z_LVAL_P(zv));
    case IS_DOUBLE:
        return PyFloat_FromDouble(Z_DVAL_P(zv));
    case IS_STRING:
        return string2py(zv);
    case IS_ARRAY:
        return array2py(zv);
    case IS_OBJECT:
        return phpy::python::new_object(zv);
    case IS_RESOURCE:
        return phpy::python::new_resource(zv);
    case IS_REFERENCE:
        return phpy::python::new_reference(zv);
    default:
        return PyErr_Format(PyExc_TypeError, "[php2py] Unsupported php type[%d]", Z_TYPE_P(zv));
    }
}

PyObject *php2py_object(zval *zv) {
    switch (Z_TYPE_P(zv)) {
    case IS_NULL:
        Py_INCREF(Py_None);
        return Py_None;
    case IS_TRUE:
        Py_INCREF(Py_True);
        return Py_True;
    case IS_FALSE:
        Py_INCREF(Py_False);
        return Py_False;
    case IS_LONG:
        return PyLong_FromLong(Z_LVAL_P(zv));
    case IS_DOUBLE:
        return PyFloat_FromDouble(Z_DVAL_P(zv));
    case IS_STRING:
        return phpy::python::new_string(zv);
    case IS_ARRAY:
        return phpy::python::new_array(zv);
    case IS_OBJECT:
        return phpy::python::new_object(zv);
    case IS_RESOURCE:
        return phpy::python::new_resource(zv);
    case IS_REFERENCE:
        return phpy::python::new_reference(zv);
    default:
        return PyErr_Format(PyExc_TypeError, "[php2py] Unsupported php type[%d]", Z_TYPE_P(zv));
    }
}

void debug_dump(uint32_t i, zval *item) {
    printf("[%d] type=%d, ptr=%p \n", i, item->u1.v.type, item->value.arr);
}

void debug_dump(uint32_t i, PyObject *pObj) {
    ssize_t len;
    printf("[%d] type=%s, str=%s, repr=%s, ptr=%p\n",
           i,
           Py_TYPE(pObj)->tp_name,
           phpy::python::string2utf8(PyObject_Str(pObj), &len),
           phpy::python::string2utf8(PyObject_Repr(pObj), &len),
           pObj);
}

void var_dump(zval *var) {
    php_var_dump(var, 3);
}

CallObject::CallObject(PyObject *_fn, zval *_return_value, uint32_t _argc, zval *_argv, zend_array *_kwargs) {
    fn = _fn;
    return_value = _return_value;
    if (_kwargs) {
        kwargs = array2dict(_kwargs);
    }
    if (_argv) {
        parse_args(_argc, _argv);
    }
}

CallObject::CallObject(PyObject *_fn, zval *_return_value, zval *_argv) {
    fn = _fn;
    return_value = _return_value;
    if (_argv) {
        parse_args(_argv);
    }
}

void CallObject::call() {
    PyObject *value;
    if (argc == 0 && kwargs == nullptr) {
        value = PyObject_CallNoArgs(fn);
    } else {
        value = PyObject_Call(fn, args, kwargs);
    }
    if (value != NULL) {
        py2php(value, return_value);
        Py_DECREF(value);
    } else {
        phpy::php::throw_error_if_occurred();
        RETVAL_NULL();
    }
}

CallObject::~CallObject() {
    if (args) {
        Py_DECREF(args);
    }
    if (kwargs) {
        Py_DECREF(kwargs);
    }
}

PyObject *string2py(zend_string *zstr) {
    return PyUnicode_FromStringAndSize(ZSTR_VAL(zstr), ZSTR_LEN(zstr));
}

void CallObject::parse_args(uint32_t _argc, zval *_argv) {
    argc = _argc;
    if (argc == 0 && kwargs == nullptr) {
        return;
    }
    args = PyTuple_New(argc);
    for (uint32_t i = 0; i < argc; i++) {
        PyTuple_SetItem(args, i, php2py(&_argv[i]));
    }
}

void CallObject::parse_args(zval *array) {
    argc = phpy::php::array_count(array);
    if (argc == 0) {
        return;
    }

    auto arg_list = PyList_New(0);
    zval *current;
    zend_string *string_key;
    zend_ulong num_key;

    ZEND_HASH_FOREACH_KEY_VAL(Z_ARRVAL_P(array), num_key, string_key, current) {
        if (!string_key) {
            PyList_Append(arg_list, php2py(current));
        } else {
            if (kwargs == nullptr) {
                kwargs = PyDict_New();
            }
            PyDict_SetItem(kwargs, string2py(string_key), php2py(current));
        }
        (void) num_key;
    }
    ZEND_HASH_FOREACH_END();

    args = PyList_AsTuple(arg_list);
    Py_DECREF(arg_list);
}

namespace phpy {
namespace python {
const char *string2utf8(PyObject *pv, ssize_t *len) {
    return PyUnicode_AsUTF8AndSize(pv, len);
};
void tuple2argv(zval *argv, PyObject *args, ssize_t size, int begin) {
    Py_ssize_t i;
    for (i = begin; i < size; i++) {
        PyObject *arg = PyTuple_GetItem(args, i);
        if (arg == NULL) {
            PyErr_SetString(PyExc_TypeError, "wrong parameter");
            break;
        }
        zval item;
        py2php_scalar(arg, &item);
        argv[i - begin] = item;
    }
}

void release_argv(uint32_t argc, zval *argv) {
    for (uint32_t i = 0; i < argc; i++) {
        zval_ptr_dtor(&argv[i]);
    }
}
}  // namespace python
}  // namespace phpy
