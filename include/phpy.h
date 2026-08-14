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

#pragma once

#ifdef HAVE_CONFIG_H
#include "config.h"
#endif

#define PY_SSIZE_T_CLEAN
#include <Python.h>

#ifdef HAVE_PUTENV
#undef HAVE_PUTENV
#endif

#ifdef HAVE_GETPID
#undef HAVE_GETPID
#endif

#include <main/php.h>
#include <main/SAPI.h>
#include <main/php_main.h>
#include <main/php_variables.h>
#include <main/php_ini.h>
#include <zend_ini.h>
#include <zend_interfaces.h>

#include "phpy_api.h"

#include <iostream>

#define __SCOPEGUARD_CONCATENATE_IMPL(s1, s2) s1##s2
#define __SCOPEGUARD_CONCATENATE(s1, s2) __SCOPEGUARD_CONCATENATE_IMPL(s1, s2)

template <typename Fun>
class ScopeGuard {
  public:
    ScopeGuard(Fun &&f) : _fun(std::forward<Fun>(f)), _active(true) {}

    ~ScopeGuard() {
        if (_active) {
            _fun();
        }
    }

    void dismiss() {
        _active = false;
    }

    ScopeGuard() = delete;
    ScopeGuard(const ScopeGuard &) = delete;
    ScopeGuard &operator=(const ScopeGuard &) = delete;

    ScopeGuard(ScopeGuard &&rhs) : _fun(std::move(rhs._fun)), _active(rhs._active) {
        rhs.dismiss();
    }

  private:
    Fun _fun;
    bool _active;
};

namespace detail {
enum class ScopeGuardOnExit {};

template <typename Fun>
inline ScopeGuard<Fun> operator+(ScopeGuardOnExit, Fun &&fn) {
    return ScopeGuard<Fun>(std::forward<Fun>(fn));
}
}  // namespace detail

#define ON_SCOPE_EXIT auto __SCOPEGUARD_CONCATENATE(ext_exitBlock_, __LINE__) = detail::ScopeGuardOnExit() + [&]()

enum {
    PHPY_PHP_EXTENSION = 1,
    PHPY_PYTHON_MODULE = 2,
};

int phpy_init(int mode);
int phpy_get_mode(void);

zval *zend_string_cast(PyObject *pv);
zval *zend_reference_cast(PyObject *pv);
zval *zend_resource_cast(PyObject *pv);
zval *zend_object_cast(PyObject *pv);
zval *zend_callable_cast(PyObject *pv);
zval *zend_array_cast(PyObject *pv);
/**
 * Type conversion, Python to PHP
 */
void py2php(PyObject *pv, zval *zv);
/**
 * Convert to PHP scalar types as much as possible
 */
void py2php_scalar(PyObject *pv, zval *zv);
/** Convert supported Python containers or iterators to a PHP array. */
void py2php_array(PyObject *pv, zval *zv);
zend_string *py2zstr(PyObject *pv);
bool object2array(PyObject *pv, zval *zv);
void object2string(PyObject *pv, zval *zv);

bool python_long_to_php(PyObject *pv, zval *zv);
/**
 * Type conversion, PHP to Python
 * Return value: New reference.
 */
PyObject *php2py(zval *zv);
/**
 * PHP to Python, Convert actual value to python object type as much as possible
 * Return value: New reference.
 */
PyObject *php2py_object(zval *zv);
/**
 * Wrap a Python container or string with PHPy's Python-facing wrapper type.
 * Return value: New reference.
 */
PyObject *py2py_scalar(PyObject *pv);
/**
 * Return value: New reference.
 */
PyObject *array2list(zend_array *ht);
/**
 * Return value: New reference.
 */
static inline PyObject *array2list(zval *zv) {
    return array2list(Z_ARRVAL_P(zv));
}
/**
 * Return value: New reference.
 */
PyObject *array2set(zend_array *ht);
static inline PyObject *array2set(zval *zv) {
    return array2set(Z_ARRVAL_P(zv));
}
PyObject *array2tuple(zend_array *ht);
static inline PyObject *array2tuple(zval *zv) {
    return array2tuple(Z_ARRVAL_P(zv));
}
PyObject *resource2py(zval *zres);
PyObject *reference2py(zval *zv);
/**
 * Return value: New reference.
 */
PyObject *array2dict(zend_array *ht);
/**
 * Return value: New reference.
 */
PyObject *string2py(const zend_string *zv);
/**
 * Return value: New reference.
 */
PyObject *php_number_to_python_long(zval *zv);
/**
 * Return value: New reference.
 */
static inline PyObject *array2dict(zval *zv) {
    return array2dict(Z_ARRVAL_P(zv));
}
/**
 * Return value: New reference.
 */
static inline PyObject *string2py(const zval *zv) {
    return string2py(Z_STR_P(zv));
}

PyObject *object_create(zend_class_entry *ce, PyObject *args, uint32_t argc, int begin);
PyObject *object_create(PyObject *pv, zend_class_entry *ce, PyObject *args, uint32_t argc, int begin);

bool ZendString_Check(PyObject *pv);
bool ZendArray_Check(PyObject *pv);
bool ZendObject_Check(PyObject *pv);
bool ZendReference_Check(PyObject *pv);
bool ZendResource_Check(PyObject *pv);
bool ZendCallable_Check(PyObject *pv);

void debug_dump(uint32_t i, zval *item);
void debug_dump(uint32_t i, PyObject *pObj);
void var_dump(zval *var);
void debug_var_dump(zval *var);
void debug_print_refcnt(const char *fn, PyObject *zv);

bool py_module_string_init(PyObject *m);
bool py_module_object_init(PyObject *m);
bool py_module_resource_init(PyObject *m);
bool py_module_class_init(PyObject *m);
bool py_module_reference_init(PyObject *m);
bool py_module_callable_init(PyObject *m);
bool py_module_array_init(PyObject *m);
bool py_module_iterator_init(PyObject *m);

PyObject *py_module_create(bool py_module);

int php_class_core_init(INIT_FUNC_ARGS);
int php_class_module_init(INIT_FUNC_ARGS);
int php_class_object_init(INIT_FUNC_ARGS);
int php_class_str_init(INIT_FUNC_ARGS);
int php_class_dict_init(INIT_FUNC_ARGS);
int php_class_sequence_init(INIT_FUNC_ARGS);
int php_class_list_init(INIT_FUNC_ARGS);
int php_class_tuple_init(INIT_FUNC_ARGS);
int php_class_set_init(INIT_FUNC_ARGS);
int php_class_type_init(INIT_FUNC_ARGS);
int php_class_iter_init(INIT_FUNC_ARGS);
int php_class_fn_init(INIT_FUNC_ARGS);
int php_class_error_init(INIT_FUNC_ARGS);
void php_class_init_all(INIT_FUNC_ARGS);
int php_python_operator_init(INIT_FUNC_ARGS);

zend_class_entry *phpy_object_get_ce();
zend_class_entry *phpy_sequence_get_ce();
zend_class_entry *phpy_iter_get_ce();

void phpy_object_ctor(zval *zobject, PyObject *object);
/**
 * Return value: Borrowed reference.
 */
PyObject *phpy_object_get_handle(const zval *zobject);
/**
 * Return value: Borrowed reference.
 */
PyObject *phpy_object_get_handle(const zend_object *object);

void phpy_object_iterator_reset(zval *object);
PyObject *phpy_object_iterator_next(zval *object);
PyObject *phpy_object_iterator_current(const zval *object);
bool phpy_object_iterator_valid(const zval *object);
uint32_t phpy_object_iterator_index(const zval *object);

#define RETURN_PYOBJ(retval)                                                                                           \
    PyObject *pyobj = php2py_object(retval);                                                                           \
    zval_ptr_dtor(retval);                                                                                             \
    return pyobj;

#define STR_AND_LEN(str) str, sizeof(str) - 1

#define Py_TypeName(pv) Py_TYPE(pv)->tp_name

#ifndef Py_IsTrue
#define Py_IsTrue PyObject_IsTrue
#endif

#ifndef Py_IsNone
#define Py_IsNone(ob) (Py_TYPE(ob) == Py_TYPE(Py_None))
#define PyObject_CallNoArgs _PyObject_CallNoArg
#endif

#ifndef Py_IS_TYPE
#define Py_IS_TYPE(ob, type) (Py_TYPE(ob) == type)
#endif

namespace phpy {
namespace php {
void new_module(zval *zv, PyObject *pv);
void new_object(zval *zv, PyObject *pv);
void new_object(zval *zv, PyObject *pv, zend_class_entry *ce);
/**
 * This function does not increment the reference count for pv object;
 * a new reference must be passed in, otherwise a gc error will occur.
 */
void new_object_no_addref(zval *zv, PyObject *pv);
void new_dict(zval *zv, PyObject *pv);
void new_list(zval *zv, PyObject *pv);
void new_tuple(zval *zv, PyObject *pv);
void new_set(zval *zv, PyObject *pv);
void new_str(zval *zv, PyObject *pv);
void new_type(zval *zv, PyObject *pv);
void new_fn(zval *zv, PyObject *fn);
void new_iter(zval *zv, PyObject *type);
void new_error(zval *zv, PyObject *error);

void add_object(PyObject *pv, void (*)(PyObject *));
bool del_object(PyObject *pv);
void call_builtin_fn(const char *name, size_t l_name, zval *arguments, zval *return_value);
bool env_equals(const char *name, size_t nlen, const char *val, size_t vlen);
void throw_error(PyObject *error);

static inline void throw_error_if_occurred() {
    auto error = PyErr_Occurred();
    if (error != NULL) {
        phpy::php::throw_error(error);
    }
}

#define CHECK_ARG(pObj)                                                                                                \
    if (pObj == NULL) {                                                                                                \
        phpy::php::throw_error_if_occurred();                                                                          \
        return;                                                                                                        \
    }

static inline bool is_typeof(const zval *zv, int type) {
    return Z_TYPE_P(zv) == type;
}

static inline bool is_null(const zval *zv) {
    return zv == NULL || ZVAL_IS_NULL(zv);
}

static inline bool is_array(const zval *zv) {
    return is_typeof(zv, IS_ARRAY);
}

static inline bool is_empty_array(const zval *zv) {
    return is_typeof(zv, IS_ARRAY) && zend_hash_num_elements(Z_ARRVAL_P(zv)) == 0;
}

static inline bool is_string(const zval *zv) {
    return is_typeof(zv, IS_STRING);
}

static inline bool is_object(const zval *zv) {
    return is_typeof(zv, IS_OBJECT);
}

static inline bool is_pyobject(const zval *zv) {
    return is_object(zv) && instanceof_function(Z_OBJCE_P(zv), phpy_object_get_ce());
}

/**
 * Parse the single integer index argument shared by the sequence offset*
 * methods (PyList / PyTuple).
 */
static inline ssize_t get_key(INTERNAL_FUNCTION_PARAMETERS) {
    zend_long k;
    ZEND_PARSE_PARAMETERS_START(1, 1)
    Z_PARAM_LONG(k)
    ZEND_PARSE_PARAMETERS_END_EX(return 0);
    return (ssize_t) k;
}

/**
 * Normalize a possibly negative index against `size`; returns false when the
 * index is out of range.
 */
static inline bool normalize_index(PyObject *object, ssize_t size, ssize_t index, ssize_t *normalized) {
    if (index < 0) {
        index += size;
    }
    if (index < 0 || index >= size) {
        return false;
    }
    *normalized = index;
    return true;
}

/**
 * Shared PyList/PyTuple offsetGet body. `get_size`/`get_item` must be the
 * container-specific accessors (e.g. PyList_GET_SIZE / PyList_GetItem); the
 * latter returns a borrowed reference. The caller holds the GIL.
 */
template <typename GetSize, typename GetItem>
static void sequence_offset_get(PyObject *object,
                                ssize_t index,
                                const char *class_name,
                                GetSize get_size,
                                GetItem get_item,
                                zval *return_value) {
    ssize_t normalized;
    if (!normalize_index(object, get_size(object), index, &normalized)) {
        zend_throw_error(NULL, "%s: index[%ld] out of range", class_name, index);
        return;
    }
    PyObject *value = get_item(object, normalized);
    if (value != NULL) {
        py2php(value, return_value);
    }
}

/**
 * Shared PyList/PyDict/PySet/PyTuple constructor conversion: a null or empty
 * argument builds an empty container, a PHP array is converted through
 * `from_array` (array2list / array2dict / ...), anything else raises an
 * "unsupported type" error.
 */
template <typename MakeEmpty, typename FromArray>
static inline PyObject *construct_container(zval *arg, const char *name, MakeEmpty make_empty, FromArray from_array) {
    if (phpy::php::is_null(arg) || phpy::php::is_empty_array(arg)) {
        return make_empty();
    }
    if (phpy::php::is_array(arg)) {
        return from_array(arg);
    }
    zend_throw_error(NULL, "%s: unsupported type", name);
    return nullptr;
}

/**
 * Shared php_class_*_init registration for the leaf Py* classes: registers
 * the internal class and applies the common final / no-dynamic-properties /
 * not-serializable flags.
 *
 * INIT_CLASS_ENTRY() is avoided on purpose: PHP < 8.3 computes the class-name
 * length with sizeof(name) - 1, which only works for string literals. Building
 * the entry manually with strlen() keeps this helper valid on every supported
 * PHP version.
 */
static inline zend_class_entry *register_internal_class(const char *name,
                                                        const zend_function_entry *methods,
                                                        zend_class_entry *parent) {
    zend_class_entry ce;
    memset(&ce, 0, sizeof(zend_class_entry));
    ce.name = zend_string_init_interned(name, strlen(name), 1);
    ce.info.internal.builtin_functions = methods;
    zend_class_entry *registered = zend_register_internal_class_ex(&ce, parent);
    registered->ce_flags |= ZEND_ACC_FINAL | ZEND_ACC_NO_DYNAMIC_PROPERTIES | ZEND_ACC_NOT_SERIALIZABLE;
    return registered;
}

/**
 * Return value: Borrowed reference.
 */
static inline zval *array_get(zval *zv, long index) {
    return zend_hash_index_find(Z_ARR_P(zv), index);
}
/**
 * Return value: Borrowed reference. If not exist, returns null pointer
 */
static inline zval *array_get(zval *zv, const char *key, size_t l_key) {
    return zend_hash_str_find(Z_ARR_P(zv), key, l_key);
}
/**
 * Return value: Borrowed reference.
 */
static inline zval *object_get(zval *zo, const char *name, size_t l_name) {
    static zval rv;
    return zend_read_property(Z_OBJCE_P(zo), Z_OBJ_P(zo), name, l_name, 0, &rv);
}

PyObject *arg_1(INTERNAL_FUNCTION_PARAMETERS);
PyObject *arg_1(INTERNAL_FUNCTION_PARAMETERS, zend_class_entry *ce);

static inline uint32_t array_count(zend_array *ht) {
    return zend_array_count(ht);
}

static inline uint32_t array_count(const zval *zv) {
    return zend_array_count(Z_ARRVAL_P(zv));
}

/**
 * Return value: New reference.
 */static inline zend_result call_fn(
    zval *object,
    zval *function_name,
    zval *retval_ptr,
    uint32_t param_count,
    zval *params,
    HashTable *named_params = nullptr,
    zend_fcall_info_cache *cache = nullptr) {
    if (cache == nullptr) {
        zend_result result = FAILURE;
        zend_try {
            result = call_user_function_named(NULL, object, function_name, retval_ptr, param_count, params, named_params);
        }
        zend_end_try();
        if (EG(exception) != NULL) {
            return FAILURE;
        }
        return result;
    }

    zend_fcall_info fci;
    fci.size = sizeof(fci);
    fci.object = object == nullptr ? nullptr : Z_OBJ_P(object);
    ZVAL_COPY_VALUE(&fci.function_name, function_name);
    fci.retval = retval_ptr;
    fci.param_count = param_count;
    fci.params = params;
    fci.named_params = named_params;

    zend_result result = FAILURE;
    zend_try {
        result = zend_call_function(&fci, cache);
    }
    zend_end_try();
    if (EG(exception) != NULL) {
        return FAILURE;
    }
    return result;
}
}  // namespace php
struct CallObject {
    PyObject *args = nullptr;
    PyObject *kwargs = nullptr;
    uint32_t argc = 0;
    PyObject *fn;
    zval *return_value;
    bool args_ready = true;
    CallObject(PyObject *_fn, zval *_return_value, uint32_t _argc, zval *_argv, zend_array *_kwargs);
    CallObject(PyObject *_fn, zval *_return_value, zval *_argv);
    bool parse_args(zval *array);
    bool parse_args(uint32_t _argc, zval *_argv);
    ~CallObject();
    void call();
};
class StrObject {
  private:
    PyObject *str_ = nullptr;
    ssize_t len_ = 0;
    const char *val_ = nullptr;

  public:
    StrObject(PyObject *pv);
    ~StrObject() {
        if (str_) {
            Py_DECREF(str_);
        }
    }
    explicit operator bool() const {
        return val_ != nullptr;
    }
    const char *val() const {
        return val_;
    }
    ssize_t len() const {
        return len_;
    }
};
namespace python {
/**
 * Shared tp_dealloc boilerplate for the zend_* wrapper types: run the
 * registered dtor exactly once (either at PHP request shutdown or when the
 * Python object is collected, whichever happens first), then free the object.
 */
template <typename T, typename Dtor>
static void destroy_wrapper(T *self, Dtor dtor) {
    if (phpy::php::del_object((PyObject *) self)) {
        dtor((PyObject *) self);
    }
    Py_TYPE(self)->tp_free((PyObject *) self);
}

/**
 * Register a Python heap type into the module, covering the boilerplate that
 * every py_module_*_init repeats: PyType_Ready, INCREF, PyModule_AddObject.
 */
inline bool register_python_type(PyObject *m, PyTypeObject *type, const char *name) {
    if (PyType_Ready(type) < 0) {
        return false;
    }
    Py_INCREF(type);
    if (PyModule_AddObject(m, name, (PyObject *) type) < 0) {
        Py_DECREF(type);
        Py_DECREF(m);
        return false;
    }
    return true;
}

/** Owns one new CPython reference and releases it on every exit path. */
class OwnedPythonReference {
  public:
    explicit OwnedPythonReference(PyObject *value = nullptr) : value_(value) {}
    OwnedPythonReference(const OwnedPythonReference &) = delete;
    OwnedPythonReference &operator=(const OwnedPythonReference &) = delete;
    OwnedPythonReference(OwnedPythonReference &&other) noexcept : value_(other.release()) {}

    OwnedPythonReference &operator=(OwnedPythonReference &&other) noexcept {
        if (this != &other) {
            reset(other.release());
        }
        return *this;
    }

    ~OwnedPythonReference() {
        reset();
    }

    PyObject *get() const noexcept {
        return value_;
    }

    explicit operator bool() const noexcept {
        return value_ != nullptr;
    }

    PyObject *release() noexcept {
        PyObject *value = value_;
        value_ = nullptr;
        return value;
    }

    /** Replaces the owned reference with another new reference. */
    void reset(PyObject *value = nullptr) noexcept {
        Py_XDECREF(value_);
        value_ = value;
    }

  private:
    PyObject *value_;
};

PyObject *new_array(const zval *zv);
PyObject *new_array(PyObject *pv);
PyObject *new_string(const zval *zv);
PyObject *new_string(size_t len);
PyObject *new_string(PyObject *pv);
PyObject *new_object(zval *zv);
PyObject *new_resource(const zval *zv);
PyObject *new_reference(zval *zv);
PyObject *new_callable(const zval *zv);
PyObject *new_iterator(zval *zv);
const char *string2utf8(PyObject *pv, ssize_t *len);
const char *string2char_ptr(PyObject *pv, ssize_t *len);
void string2zval(PyObject *pv, zval *zv);
void tuple2argv(zval *argv, PyObject *args, ssize_t size, int begin = 1);
void release_argv(uint32_t argc, zval *argv);
class LockGuard {
  public:
    LockGuard() : state_(PyGILState_Ensure()), released_(false) {}

    ~LockGuard() {
        if (!released_) {
            PyGILState_Release(state_);
        }
    }

    void release() {
        if (!released_) {
            PyGILState_Release(state_);
            released_ = true;
        }
    }

    LockGuard(const LockGuard &) = delete;
    LockGuard &operator=(const LockGuard &) = delete;

  private:
    PyGILState_STATE state_;
    bool released_;
};

#if PHPY_ENABLE_GIL
#define LOCK_GIL() LockGuard gil
#else
#define LOCK_GIL()
#endif
}  // namespace python
struct Options {
    bool numeric_as_object;
    bool return_as_object;
    bool argument_as_object;
    bool display_exception;
};
}  // namespace phpy

extern phpy::Options phpy_options;
