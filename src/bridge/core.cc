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

#include <algorithm>
#include <vector>

using phpy::CallObject;
using phpy::StrObject;
using phpy::python::OwnedPythonReference;

const int var_dump_level = 3;

static int init_mode = 0;

int phpy_init(int mode) {
    if (init_mode > 0) {
        return -1;
    } else {
        init_mode = mode;
        return 0;
    }
}

int phpy_get_mode(void) {
    return init_mode;
}

static bool try_convert_python_base_value(PyObject *pv, zval *zv);
static PyObject *try_convert_php_base_value(zval *zv);

constexpr size_t kMaxConversionDepth = 128;

/**
 * Tracks containers that are active in one conversion call.
 *
 * The guard deliberately owns no process-global or thread-local state. Its
 * destructor removes the container even when a nested conversion returns
 * early, which makes recursive conversion safe for exceptions and re-entry.
 */
template <typename T>
class ConversionRecursionGuard {
  public:
    ConversionRecursionGuard(std::vector<T *> &active,
                             T *value,
                             const char *recursive_message,
                             const char *depth_message)
    : active_(active), entered_(false) {
        if (std::find(active_.begin(), active_.end(), value) != active_.end()) {
            PyErr_SetString(PyExc_ValueError, recursive_message);
            return;
        }
        if (active_.size() >= kMaxConversionDepth) {
            PyErr_SetString(PyExc_RecursionError, depth_message);
            return;
        }
        active_.push_back(value);
        entered_ = true;
    }

    ConversionRecursionGuard(const ConversionRecursionGuard &) = delete;
    ConversionRecursionGuard &operator=(const ConversionRecursionGuard &) = delete;

    ~ConversionRecursionGuard() {
        if (entered_) {
            active_.pop_back();
        }
    }

    explicit operator bool() const {
        return entered_;
    }

  private:
    std::vector<T *> &active_;
    bool entered_;
};

enum class PythonToPhpPolicy {
    // Keep Python values behind their corresponding PHPy wrapper objects.
    PreserveObjects,
    // Materialize Python scalar and container values as native PHP values.
    ConvertContainers,
};

/**
 * Stateful Python-to-PHP conversion for one top-level value.
 *
 * Recursive calls reuse this instance, so the policy cannot change halfway
 * through a conversion and cyclic Python containers can be detected reliably.
 */
class PythonToPhpConverter {
  public:
    explicit PythonToPhpConverter(PythonToPhpPolicy policy) : policy_(policy) {}

    bool convert(PyObject *value, zval *result);
    bool convertContainer(PyObject *value, zval *result);

  private:
    bool convertPreservingObjects(PyObject *value, zval *result);
    bool convertRecursively(PyObject *value, zval *result);
    bool convertIterable(PyObject *value, zval *result);
    bool convertDictionary(PyObject *value, zval *result);

    PythonToPhpPolicy policy_;
    std::vector<PyObject *> active_containers_;
};

#ifndef PySet_CheckExact
#define PySet_CheckExact(op) Py_IS_TYPE(op, &PySet_Type)
#endif

/**
 * Not exact Python built-in types like tuple, set, dict, or list must be handled as PyObject.
 * Custom subclasses may override access methods, leading to unpredictable errors.
 * For example, pygame.key.ScancodeWrapper inherits from tuple but internally sets `.tp_as_mapping =
 * &pg_scancodewrapper_mapping`, overloading the array access operator. In such cases, if PyTuple_Check is used in PHPy,
 * it will attempt to cast ScancodeWrapper to a PyTuple type and use PyTuple_GetItem to retrieve data,
 * resulting in False. However, in Python code, calling __getitem__ for dictionary access returns True.
 * Reference: https://github.com/pygame/pygame/blob/main/src_c/key.c
 */
bool PythonToPhpConverter::convertPreservingObjects(PyObject *pv, zval *zv) {
    if (!phpy_options.return_as_object && try_convert_python_base_value(pv, zv)) {
        return !PyErr_Occurred();
    }
    if (PyUnicode_CheckExact(pv)) {
        phpy::php::new_str(zv, pv);
    } else if (PyList_CheckExact(pv)) {
        phpy::php::new_list(zv, pv);
    } else if (PyTuple_CheckExact(pv)) {
        phpy::php::new_tuple(zv, pv);
    } else if (PySet_CheckExact(pv)) {
        phpy::php::new_set(zv, pv);
    } else if (PyDict_CheckExact(pv)) {
        phpy::php::new_dict(zv, pv);
    } else if (PyModule_CheckExact(pv)) {
        phpy::php::new_module(zv, pv);
    } else if (PyType_CheckExact(pv)) {
        phpy::php::new_type(zv, pv);
    } else if (PyIter_Check(pv)) {
        phpy::php::new_iter(zv, pv);
    } else {
        phpy::php::new_object(zv, pv);
    }
    return true;
}

bool PythonToPhpConverter::convertRecursively(PyObject *pv, zval *zv) {
    if (try_convert_python_base_value(pv, zv)) {
        return !PyErr_Occurred();
    }
    if (PyByteArray_Check(pv)) {
        ZVAL_STRINGL(zv, PyByteArray_AS_STRING(pv), PyByteArray_GET_SIZE(pv));
    } else if (PyBytes_Check(pv)) {
        ZVAL_STRINGL(zv, PyBytes_AS_STRING(pv), PyBytes_GET_SIZE(pv));
    } else if (PyUnicode_Check(pv)) {
        zend_string *value = py2zstr(pv);
        if (value == nullptr) {
            return false;
        }
        ZVAL_STR(zv, value);
    } else if (PyList_Check(pv)) {
        return convertIterable(pv, zv);
    } else if (PyRange_Check(pv)) {
        return convertIterable(pv, zv);
    } else if (PyTuple_Check(pv)) {
        return convertIterable(pv, zv);
    } else if (PyDict_Check(pv)) {
        return convertDictionary(pv, zv);
    } else if (PySet_Check(pv)) {
        return convertIterable(pv, zv);
    } else if (PyLong_CheckExact(pv)) {
        return python_long_to_php(pv, zv);
    } else if (PyFloat_Check(pv)) {
        ZVAL_DOUBLE(zv, PyFloat_AsDouble(pv));
    } else {
        phpy::php::new_object(zv, pv);
    }
    return !PyErr_Occurred();
}

bool PythonToPhpConverter::convert(PyObject *value, zval *result) {
    return policy_ == PythonToPhpPolicy::ConvertContainers ? convertRecursively(value, result)
                                                           : convertPreservingObjects(value, result);
}

void py2php_scalar(PyObject *pv, zval *zv) {
    PythonToPhpConverter converter(PythonToPhpPolicy::ConvertContainers);
    if (!converter.convert(pv, zv)) {
        ZVAL_NULL(zv);
        phpy::php::throw_error_if_occurred();
    }
}

void py2php_array(PyObject *pv, zval *zv) {
    if (!PyList_Check(pv) && !PyTuple_Check(pv) && !PySet_Check(pv) && !PyDict_Check(pv) && !PyIter_Check(pv)) {
        ZVAL_EMPTY_ARRAY(zv);
        return;
    }

    PythonToPhpConverter converter(PythonToPhpPolicy::ConvertContainers);
    if (!converter.convertContainer(pv, zv)) {
        if (!Z_ISUNDEF_P(zv)) {
            zval_ptr_dtor(zv);
        }
        ZVAL_EMPTY_ARRAY(zv);
        phpy::php::throw_error_if_occurred();
    }
}

/**
 * Increase reference count of the value
 */
void py2php(PyObject *pv, zval *zv) {
    PythonToPhpConverter converter(PythonToPhpPolicy::PreserveObjects);
    if (!converter.convert(pv, zv)) {
        ZVAL_NULL(zv);
        phpy::php::throw_error_if_occurred();
    }
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
    ZVAL_UNDEF(zv);
    PythonToPhpConverter converter(PythonToPhpPolicy::PreserveObjects);
    if (!converter.convertContainer(pv, zv)) {
        if (!Z_ISUNDEF_P(zv)) {
            zval_ptr_dtor(zv);
        }
        ZVAL_NULL(zv);
        phpy::php::throw_error_if_occurred();
    }
}

zend_string *py2zstr(PyObject *pv) {
    Py_ssize_t sl;
    const char *sv = PyUnicode_AsUTF8AndSize(pv, &sl);
    if (sv == nullptr) {
        return nullptr;
    }
    return zend_string_init(sv, sl, 0);
}

bool python_long_to_php(PyObject *pv, zval *zv) {
    int overflow;
    auto lval = PyLong_AsLongAndOverflow(pv, &overflow);
    if (overflow == 0) {
        if (lval == -1 && PyErr_Occurred()) {
            return false;
        }
        ZVAL_LONG(zv, lval);
    } else {
        ssize_t len;
        OwnedPythonReference str(PyObject_Str(pv));
        if (!str) {
            return false;
        }
        const char *sval = phpy::python::string2utf8(str.get(), &len);
        if (sval == nullptr) {
            return false;
        }
        ZVAL_STRINGL(zv, sval, len);
    }
    return true;
}

/**
 * Return value: New reference.
 */
PyObject *php_number_to_python_long(zval *zv) {
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

static bool try_convert_python_base_value(PyObject *pv, zval *zv) {
    if (PyBool_Check(pv)) {
        ZVAL_BOOL(zv, Py_IsTrue(pv));
    } else if (Py_IsNone(pv)) {
        ZVAL_NULL(zv);
    } else if (!phpy_options.numeric_as_object && PyLong_CheckExact(pv)) {
        python_long_to_php(pv, zv);
    } else if (!phpy_options.numeric_as_object && PyFloat_Check(pv)) {
        ZVAL_DOUBLE(zv, PyFloat_AsDouble(pv));
    } else if (ZendObject_Check(pv)) {
        ZVAL_ZVAL(zv, zend_object_cast(pv), 1, 0);
    } else if (ZendReference_Check(pv)) {
        ZVAL_COPY(zv, zend_reference_cast(pv));
    } else if (ZendResource_Check(pv)) {
        ZVAL_COPY(zv, zend_resource_cast(pv));
    } else if (ZendString_Check(pv)) {
        ZVAL_COPY(zv, zend_string_cast(pv));
    } else if (ZendArray_Check(pv)) {
        ZVAL_COPY(zv, zend_array_cast(pv));
    } else {
        return false;
    }
    return true;
}

/**
 * Stateful PHP-to-Python conversion for one top-level value.
 *
 * PHP references are dereferenced at the language boundary. The active array
 * stack is local to this converter and therefore cannot leak into another
 * request, nested call, or synchronous callback into PHP.
 */
class PhpToPythonConverter {
  public:
    PyObject *convert(zval *value);
    PyObject *convertArrayToList(zend_array *array);
    PyObject *convertArrayToTuple(zend_array *array);
    PyObject *convertArrayToSet(zend_array *array);
    PyObject *convertArrayToDict(zend_array *array);

  private:
    PyObject *convertArray(zval *value);
    std::vector<zend_array *> active_arrays_;
};

PyObject *PhpToPythonConverter::convertArrayToList(zend_array *ht) {
    ConversionRecursionGuard<zend_array> guard(active_arrays_,
                                                ht,
                                                "recursive PHP array cannot be converted to Python",
                                                "PHP array nesting exceeds the conversion limit");
    if (!guard) {
        return NULL;
    }

    OwnedPythonReference list(PyList_New(0));
    if (!list) {
        return NULL;
    }
    zval *current;
    ZEND_HASH_FOREACH_VAL(ht, current) {
        OwnedPythonReference elem(convert(current));
        if (!elem || PyList_Append(list.get(), elem.get()) < 0) {
            return NULL;
        }
    }
    ZEND_HASH_FOREACH_END();
    return list.release();
}

/**
 * Return value: New reference.
 */
PyObject *array2list(zend_array *ht) {
    PhpToPythonConverter converter;
    return converter.convertArrayToList(ht);
}

/**
 * Return value: New reference.
 */
PyObject *array2tuple(zend_array *ht) {
    PhpToPythonConverter converter;
    return converter.convertArrayToTuple(ht);
}

PyObject *PhpToPythonConverter::convertArrayToTuple(zend_array *ht) {
    ConversionRecursionGuard<zend_array> guard(active_arrays_,
                                                ht,
                                                "recursive PHP array cannot be converted to Python",
                                                "PHP array nesting exceeds the conversion limit");
    if (!guard) {
        return NULL;
    }

    zval *current;
    OwnedPythonReference tuple(PyTuple_New(phpy::php::array_count(ht)));
    if (!tuple) {
        return NULL;
    }
    Py_ssize_t index = 0;
    ZEND_HASH_FOREACH_VAL(ht, current) {
        OwnedPythonReference elem(convert(current));
        if (!elem) {
            return NULL;
        }
        // The tuple is newly allocated and the index is known to be valid.
        // PyTuple_SET_ITEM steals the new element reference.
        PyTuple_SET_ITEM(tuple.get(), index++, elem.release());
    }
    ZEND_HASH_FOREACH_END();
    return tuple.release();
}

/**
 * Return value: New reference.
 */
PyObject *array2set(zend_array *ht) {
    PhpToPythonConverter converter;
    return converter.convertArrayToSet(ht);
}

PyObject *PhpToPythonConverter::convertArrayToSet(zend_array *ht) {
    ConversionRecursionGuard<zend_array> guard(active_arrays_,
                                                ht,
                                                "recursive PHP array cannot be converted to Python",
                                                "PHP array nesting exceeds the conversion limit");
    if (!guard) {
        return NULL;
    }

    zval *current;
    OwnedPythonReference pset(PySet_New(0));
    if (!pset) {
        return NULL;
    }
    ZEND_HASH_FOREACH_VAL(ht, current) {
        OwnedPythonReference elem(convert(current));
        if (!elem || PySet_Add(pset.get(), elem.get()) < 0) {
            return NULL;
        }
    }
    ZEND_HASH_FOREACH_END();
    return pset.release();
}

bool PythonToPhpConverter::convertIterable(PyObject *pv, zval *zv) {
    ConversionRecursionGuard<PyObject> guard(active_containers_,
                                              pv,
                                              "recursive Python container cannot be converted to PHP",
                                              "Python container nesting exceeds the conversion limit");
    if (!guard) {
        return false;
    }

    OwnedPythonReference iter(PyObject_GetIter(pv));
    if (!iter) {
        return false;
    }
    array_init(zv);
    while (true) {
        OwnedPythonReference next(PyIter_Next(iter.get()));
        if (!next) {
            break;
        }
        zval item;
        if (!convert(next.get(), &item)) {
            zval_ptr_dtor(zv);
            ZVAL_UNDEF(zv);
            return false;
        }
        add_next_index_zval(zv, &item);
    }
    if (PyErr_Occurred()) {
        zval_ptr_dtor(zv);
        ZVAL_UNDEF(zv);
        return false;
    }
    return true;
}

/**
 * Return value: New reference.
 */
PyObject *PhpToPythonConverter::convertArrayToDict(zend_array *ht) {
    ConversionRecursionGuard<zend_array> guard(active_arrays_,
                                                ht,
                                                "recursive PHP array cannot be converted to Python",
                                                "PHP array nesting exceeds the conversion limit");
    if (!guard) {
        return NULL;
    }

    uint32_t index;
    zend_string *key;
    zval *value;
    OwnedPythonReference dict(PyDict_New());
    if (!dict) {
        return NULL;
    }
    ZEND_HASH_FOREACH_KEY_VAL(ht, index, key, value) {
        OwnedPythonReference dict_key;
        if (key) {
            dict_key.reset(PyUnicode_FromStringAndSize(ZSTR_VAL(key), ZSTR_LEN(key)));
        } else {
            dict_key.reset(PyLong_FromLong(index));
        }
        OwnedPythonReference elem(convert(value));
        if (!dict_key || !elem || PyDict_SetItem(dict.get(), dict_key.get(), elem.get()) < 0) {
            return NULL;
        }
    }
    ZEND_HASH_FOREACH_END();
    return dict.release();
}

PyObject *array2dict(zend_array *ht) {
    PhpToPythonConverter converter;
    return converter.convertArrayToDict(ht);
}

bool PythonToPhpConverter::convertDictionary(PyObject *pv, zval *zv) {
    ConversionRecursionGuard<PyObject> guard(active_containers_,
                                              pv,
                                              "recursive Python container cannot be converted to PHP",
                                              "Python container nesting exceeds the conversion limit");
    if (!guard) {
        return false;
    }

    OwnedPythonReference iter(PyObject_GetIter(pv));
    if (!iter) {
        return false;
    }
    array_init(zv);
    while (true) {
        /**
         * PyIter_Next()
         * Return value: New reference
         */
        OwnedPythonReference next(PyIter_Next(iter.get()));
        if (!next) {
            break;
        }
        /**
         * PyDict_GetItem()
         * Return value: Borrowed reference
         */
        auto value = PyDict_GetItem(pv, next.get());
        zval item;
        if (value == NULL || !convert(value, &item)) {
            zval_ptr_dtor(zv);
            ZVAL_UNDEF(zv);
            return false;
        }
        StrObject key(next.get());
        if (!key) {
            zval_ptr_dtor(&item);
            zval_ptr_dtor(zv);
            ZVAL_UNDEF(zv);
            return false;
        }
        add_assoc_zval_ex(zv, key.val(), key.len(), &item);
    }
    if (PyErr_Occurred()) {
        zval_ptr_dtor(zv);
        ZVAL_UNDEF(zv);
        return false;
    }
    return true;
}

bool PythonToPhpConverter::convertContainer(PyObject *value, zval *result) {
    return PyDict_Check(value) ? convertDictionary(value, result) : convertIterable(value, result);
}

/**
 * Return value: New reference.
 */
PyObject *PhpToPythonConverter::convertArray(zval *zv) {
    zend_array *ht = Z_ARRVAL_P(zv);
    if (zend_array_is_list(ht)) {
        return convertArrayToList(ht);
    } else {
        return convertArrayToDict(ht);
    }
}

static PyObject *try_convert_php_base_value(zval *zv) {
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
    case IS_OBJECT:
        return phpy::python::new_object(zv);
    case IS_RESOURCE:
        return phpy::python::new_resource(zv);
    case IS_REFERENCE:
        return phpy::python::new_reference(zv);
    default:
        return NULL;
    }
}

PyObject *PhpToPythonConverter::convert(zval *zv) {
    // References describe PHP storage, not a Python value. Only the referenced
    // value crosses this conversion boundary.
    while (Z_TYPE_P(zv) == IS_REFERENCE) {
        zv = Z_REFVAL_P(zv);
    }
    PyObject *pv = try_convert_php_base_value(zv);
    if (pv != NULL) {
        return pv;
    }
    if (PyErr_Occurred()) {
        return NULL;
    }
    switch (Z_TYPE_P(zv)) {
    case IS_STRING:
        return string2py(zv);
    case IS_ARRAY:
        return convertArray(zv);
    default:
        PyErr_Format(PyExc_TypeError, "[php2py] Unsupported php type[%d]", Z_TYPE_P(zv));
        return NULL;
    }
}

PyObject *php2py(zval *zv) {
    PhpToPythonConverter converter;
    return converter.convert(zv);
}

/**
 * Return value: New reference.
 */
PyObject *php2py_object(zval *zv) {
    PyObject *pv = try_convert_php_base_value(zv);
    if (pv != NULL) {
        return pv;
    }
    if (PyErr_Occurred()) {
        return NULL;
    }
    switch (Z_TYPE_P(zv)) {
    case IS_STRING:
        return phpy::python::new_string(zv);
    case IS_ARRAY:
        return phpy::python::new_array(zv);
    default:
        PyErr_Format(PyExc_TypeError, "[php2py_object] Unsupported PHP type[%d]", Z_TYPE_P(zv));
        return NULL;
    }
}

void debug_dump(uint32_t i, zval *item) {
    printf("[%d] type=%d, ptr=%p \n", i, item->u1.v.type, item->value.arr);
}

void debug_dump(uint32_t i, PyObject *pv) {
    ssize_t len;
    OwnedPythonReference str(PyObject_Str(pv));
    OwnedPythonReference repr(PyObject_Repr(pv));
    printf("[%d] type=%s, str=%s, repr=%s, ptr=%p\n",
           i,
           Py_TypeName(pv),
           phpy::python::string2utf8(str.get(), &len),
           phpy::python::string2utf8(repr.get(), &len),
           pv);
}

void var_dump(zval *var) {
    php_var_dump(var, var_dump_level);
}

void debug_var_dump(zval *var) {
    php_debug_zval_dump(var, var_dump_level);
}

void debug_print_refcnt(const char *fn, PyObject *zv) {
    printf("[%s] refcount=%zu\n", fn, Py_REFCNT(zv));
}

CallObject::CallObject(PyObject *_fn, zval *_return_value, uint32_t _argc, zval *_argv, zend_array *_kwargs) {
    fn = _fn;
    return_value = _return_value;
    if (_kwargs) {
        kwargs = array2dict(_kwargs);
        args_ready = kwargs != nullptr;
    }
    if (_argv && args_ready) {
        args_ready = parse_args(_argc, _argv);
    }
}

CallObject::CallObject(PyObject *_fn, zval *_return_value, zval *_argv) {
    fn = _fn;
    return_value = _return_value;
    if (_argv) {
        args_ready = parse_args(_argv);
    }
}

void CallObject::call() {
    if (!args_ready) {
        phpy::php::throw_error_if_occurred();
        RETVAL_NULL();
        return;
    }
    OwnedPythonReference value;
    if (argc == 0 && kwargs == nullptr) {
        value = OwnedPythonReference(PyObject_CallNoArgs(fn));
    } else {
        args = args == nullptr ? PyTuple_New(0) : args;
        if (args == nullptr) {
            phpy::php::throw_error_if_occurred();
            RETVAL_NULL();
            return;
        }
        value = OwnedPythonReference(PyObject_Call(fn, args, kwargs));
    }
    if (value) {
        py2php(value.get(), return_value);
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

bool CallObject::parse_args(uint32_t _argc, zval *_argv) {
    argc = _argc;
    if (argc == 0 && kwargs == nullptr) {
        return true;
    }
    args = PyTuple_New(argc);
    if (args == nullptr) {
        return false;
    }
    for (uint32_t i = 0; i < argc; i++) {
        OwnedPythonReference elem(php2py(&_argv[i]));
        if (!elem) {
            return false;
        }
        // The tuple is new and i is in range. PyTuple_SET_ITEM steals elem.
        PyTuple_SET_ITEM(args, i, elem.release());
    }
    return true;
}

bool CallObject::parse_args(zval *array) {
    argc = phpy::php::array_count(array);
    if (argc == 0) {
        return true;
    }

    OwnedPythonReference arg_list(PyList_New(0));
    if (!arg_list) {
        return false;
    }
    zval *current;
    zend_string *string_key;
    zend_ulong num_key;

    ZEND_HASH_FOREACH_KEY_VAL(Z_ARRVAL_P(array), num_key, string_key, current) {
        OwnedPythonReference elem(php2py(current));
        if (!elem) {
            return false;
        }
        if (!string_key) {
            if (PyList_Append(arg_list.get(), elem.get()) < 0) {
                return false;
            }
        } else {
            if (kwargs == nullptr) {
                kwargs = PyDict_New();
                if (kwargs == nullptr) {
                    return false;
                }
            }
            OwnedPythonReference key(string2py(string_key));
            if (!key || PyDict_SetItem(kwargs, key.get(), elem.get()) < 0) {
                return false;
            }
        }
        (void) num_key;
    }
    ZEND_HASH_FOREACH_END();

    args = PyList_AsTuple(arg_list.get());
    return args != nullptr;
}

StrObject::StrObject(PyObject *pv) {
    if (!PyUnicode_Check(pv)) {
        pv = str_ = PyObject_Str(pv);
        if (pv == nullptr) {
            return;
        }
    }
    val_ = phpy::python::string2utf8(pv, &len_);
}

namespace phpy {
namespace php {
bool env_equals(const char *name, size_t nlen, const char *val, size_t vlen) {
    zend_string *res = php_getenv(name, nlen);
    if (res) {
        bool result = ZSTR_LEN(res) == vlen && strncasecmp(ZSTR_VAL(res), val, vlen) == 0;
        zend_string_release(res);
        return result;
    }
    return false;
}
}  // namespace php
namespace python {
const char *string2utf8(PyObject *pv, ssize_t *len) {
    return PyUnicode_AsUTF8AndSize(pv, len);
};

const char *string2char_ptr(PyObject *pv, ssize_t *len) {
    const char *c_str;
    if (ZendString_Check(pv)) {
        zval *z2 = zend_string_cast(pv);
        *len = Z_STRLEN_P(z2);
        c_str = Z_STRVAL_P(z2);
    } else if (PyByteArray_Check(pv)) {
        c_str = PyByteArray_AS_STRING(pv);
        *len = PyByteArray_GET_SIZE(pv);
    } else if (PyBytes_Check(pv)) {
        c_str = PyBytes_AS_STRING(pv);
        *len = PyBytes_GET_SIZE(pv);
    } else if (PyUnicode_Check(pv)) {
        c_str = PyUnicode_AsUTF8AndSize(pv, len);
    } else {
        return NULL;
    }
    return c_str;
}

void string2zval(PyObject *pv, zval *zv) {
    Py_ssize_t len;
    auto sval = string2char_ptr(pv, &len);
    if (sval != NULL) {
        ZVAL_STRINGL(zv, sval, len);
        return;
    }
    if (PyErr_Occurred()) {
        ZVAL_EMPTY_STRING(zv);
        phpy::php::throw_error_if_occurred();
        return;
    }
    OwnedPythonReference value(PyObject_Str(pv));
    if (value) {
        const char *sv = PyUnicode_AsUTF8AndSize(value.get(), &len);
        if (sv != NULL) {
            ZVAL_STRINGL(zv, sv, len);
        } else {
            ZVAL_EMPTY_STRING(zv);
        }
        if (sv == NULL) {
            phpy::php::throw_error_if_occurred();
        }
    } else {
        ZVAL_EMPTY_STRING(zv);
        phpy::php::throw_error_if_occurred();
    }
}

void tuple2argv(zval *argv, PyObject *args, ssize_t size, int begin) {
    Py_ssize_t i;
    for (i = begin; i < size; i++) {
        // PyTuple_GetItem()
        // Return value: Borrowed reference
        PyObject *arg = PyTuple_GetItem(args, i);
        if (arg == NULL) {
            PyErr_SetString(PyExc_TypeError, "wrong parameter");
            break;
        }
        zval item;
        if (phpy_options.argument_as_object) {
            py2php(arg, &item);
        } else {
            py2php_scalar(arg, &item);
        }
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
