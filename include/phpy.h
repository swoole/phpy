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
zend_string *py2zstr(PyObject *pv);
void object2array(PyObject *pv, zval *zv);
void object2string(PyObject *pv, zval *zv);

void long2long(PyObject *pv, zval *zv);
/**
 * Type conversion, PHP to Python
 */
PyObject *php2py(zval *zv);
/**
 * PHP to Python, Convert actual value to python object type as much as possible
 */
PyObject *php2py_object(zval *zv);
/**
 * Python to Python, Convert actual value to PHP scalar type as much as possible
 */
PyObject *py2py_scalar(PyObject *pv);

PyObject *array2list(zend_array *ht);
static inline PyObject *array2list(zval *zv) {
    return array2list(Z_ARRVAL_P(zv));
}
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
PyObject *array2dict(zend_array *ht);
PyObject *string2py(zend_string *zv);
PyObject *long2long(zval *zv);

static inline PyObject *array2dict(zval *zv) {
    return array2dict(Z_ARRVAL_P(zv));
}

static inline PyObject *string2py(zval *zv) {
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

zend_class_entry *phpy_object_get_ce();
zend_class_entry *phpy_sequence_get_ce();
zend_class_entry *phpy_iter_get_ce();
zend_class_entry *phpy_dict_get_ce();

void phpy_object_ctor(zval *zobject, PyObject *object);
/**
 * Return value: Borrowed reference.
 */
PyObject *phpy_object_get_handle(zval *zobject);
/**
 * Return value: Borrowed reference.
 */
PyObject *phpy_object_get_handle(zend_object *object);

void phpy_object_iterator_reset(zval *object);
PyObject *phpy_object_iterator_next(zval *object);
PyObject *phpy_object_iterator_current(zval *object);
bool phpy_object_iterator_valid(zval *object);
uint32_t phpy_object_iterator_index(zval *object);

#define RETURN_PYOBJ(retval)                                                                                           \
    PyObject *pyobj = php2py_object(retval);                                                                           \
    zval_ptr_dtor(retval);                                                                                             \
    return pyobj;

#define CHECK_ARG(pObj)                                                                                                \
    if (pObj == NULL) {                                                                                                \
        RETURN_FALSE;                                                                                                  \
    }

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

static inline bool is_typeof(zval *zv, int type) {
    return Z_TYPE_P(zv) == type;
}

static inline bool is_null(zval *zv) {
    return zv == NULL || ZVAL_IS_NULL(zv);
}

static inline bool is_array(zval *zv) {
    return is_typeof(zv, IS_ARRAY);
}

static inline bool is_string(zval *zv) {
    return is_typeof(zv, IS_STRING);
}

static inline bool is_object(zval *zv) {
    return is_typeof(zv, IS_OBJECT);
}

static inline bool is_pyobject(zval *zv) {
    return is_object(zv) && instanceof_function(Z_OBJCE_P(zv), phpy_object_get_ce());
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
std::tuple<PyObject *, PyObject *> arg_2(INTERNAL_FUNCTION_PARAMETERS);
std::tuple<PyObject *, PyObject *> arg_2(INTERNAL_FUNCTION_PARAMETERS, zend_class_entry *ce);

static inline uint32_t array_count(zend_array *ht) {
    return zend_array_count(ht);
}

static inline uint32_t array_count(zval *zv) {
    return zend_array_count(Z_ARRVAL_P(zv));
}

static inline bool is_empty_array(zval *zv) {
    return Z_TYPE_P(zv) == IS_ARRAY && array_count(zv) == 0;
}

/**
 * Return value: New reference.
 */
static inline zend_result call_fn(
    zval *object, zval *function_name, zval *retval_ptr, uint32_t param_count, zval *params) {
    zend_result result = FAILURE;
    zend_try {
        result = call_user_function(NULL, object, function_name, retval_ptr, param_count, params);
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
    ssize_t len_;
    const char *val_;

  public:
    StrObject(PyObject *pv);
    ~StrObject() {
        if (str_) {
            Py_DECREF(str_);
        }
    }
    const char *val() {
        return val_;
    }
    ssize_t len() {
        return len_;
    }
};
namespace python {
PyObject *new_array(zval *zv);
PyObject *new_array(PyObject *pv);
PyObject *new_string(zval *zv);
PyObject *new_string(size_t len);
PyObject *new_string(PyObject *pv);
PyObject *new_object(zval *zv);
PyObject *new_resource(zval *zv);
PyObject *new_reference(zval *zv);
PyObject *new_callable(zval *zv);
const char *string2utf8(PyObject *pv, ssize_t *len);
const char *string2char_ptr(PyObject *pv, ssize_t *len);
void string2zval(PyObject *pv, zval *zv);
void tuple2argv(zval *argv, PyObject *args, ssize_t size, int begin = 1);
void release_argv(uint32_t argc, zval *argv);
bool contains(PyObject *obj, PyObject *key);
}  // namespace python
struct Options {
    bool numeric_as_object;
    bool argument_as_object;
    bool display_exception;
};
}  // namespace phpy

extern phpy::Options phpy_options;
