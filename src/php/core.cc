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

#include <tuple>
#include <unordered_map>
#include <unordered_set>
#include <string>
#include <vector>

#include <php_network.h>
#include <php_streams.h>
#include <zend_exceptions.h>

#include "stubs/phpy_core_arginfo.h"

typedef void (*PyObjectDtor)(PyObject *);

static zend_class_entry *PyCore_ce;
static PyObject *module_builtins = nullptr;
static PyObject *module_phpy = nullptr;
static PyObject *module_operator = nullptr;
static std::unordered_map<const char *, PyObject *> builtin_functions;
static std::unordered_map<const char *, PyObject *> operator_functions;
static std::unordered_map<PyObject *, PyObjectDtor> zend_objects;
static PyObject *py_contains_operator;
static long eval_code_id = 0;

using phpy::CallObject;
using phpy::php::arg_1;
using phpy::php::arg_2;

phpy::Options phpy_options;

ZEND_METHOD(PyCore, import) {
    size_t l_module;
    char *module;
    ZEND_PARSE_PARAMETERS_START(1, 1)
    Z_PARAM_STRING(module, l_module)
    ZEND_PARSE_PARAMETERS_END_EX(RETURN_FALSE);

    PyObject *m = PyImport_ImportModule(module);
    if (m == NULL) {
        phpy::php::throw_error_if_occurred();
    } else {
        phpy::php::new_module(return_value, m);
    }
}

ZEND_METHOD(PyCore, eval) {
    size_t l_input_code;
    char *input_code;
    zval *zglobal_params = NULL;

    ZEND_PARSE_PARAMETERS_START(1, 2)
    Z_PARAM_STRING(input_code, l_input_code)
    Z_PARAM_OPTIONAL
    Z_PARAM_ARRAY_OR_NULL(zglobal_params)
    ZEND_PARSE_PARAMETERS_END_EX(RETURN_FALSE);

    std::string module_name = "eval_code_" + std::to_string(eval_code_id++);
    PyObject *module = PyModule_New(module_name.c_str());
    if (module == NULL) {
        phpy::php::throw_error_if_occurred();
        RETURN_FALSE;
    }

    // Borrowed reference
    PyObject *globals = PyModule_GetDict(module);

    if (!phpy::php::is_null(zglobal_params)) {
        auto pglobal_params = array2dict(zglobal_params);
        auto status = PyDict_Merge(globals, pglobal_params, 0);
        Py_DECREF(pglobal_params);
        if (status != 0) {
            Py_DECREF(module);
            phpy::php::throw_error_if_occurred();
            RETURN_FALSE;
        }
    }

    PyObject *result = PyRun_StringFlags(input_code, Py_file_input, globals, NULL, NULL);
    if (result == NULL) {
        phpy::php::throw_error_if_occurred();
        RETVAL_FALSE;
    } else {
        phpy::php::new_module(return_value, module);
        Py_DECREF(result);
    }
    Py_DECREF(module);
}

ZEND_METHOD(PyCore, next) {
    auto iter = arg_1(INTERNAL_FUNCTION_PARAM_PASSTHRU, phpy_iter_get_ce());
    CHECK_ARG(iter);
    auto next = PyIter_Next(iter);
    if (next == NULL) {
        return;
    }
    py2php(next, return_value);
}

ZEND_METHOD(PyCore, int) {
    zval *zv;

    ZEND_PARSE_PARAMETERS_START(1, 1)
    Z_PARAM_ZVAL(zv)
    ZEND_PARSE_PARAMETERS_END_EX(return );

    PyObject *pv = long2long(zv);
    phpy::php::new_object(return_value, pv);
    Py_DECREF(pv);
}

ZEND_METHOD(PyCore, object) {
    zval *zv = NULL;

    ZEND_PARSE_PARAMETERS_START(0, 1)
    Z_PARAM_OPTIONAL
    Z_PARAM_ZVAL(zv)
    ZEND_PARSE_PARAMETERS_END_EX(return );

    if (zv == NULL || ZVAL_IS_NULL(zv)) {
        phpy::php::call_builtin_fn(ZEND_STRL("object"), nullptr, return_value);
    } else {
        phpy::php::new_object(return_value, php2py_object(zv));
    }
}

ZEND_METHOD(PyCore, float) {
    zval *zv;

    ZEND_PARSE_PARAMETERS_START(1, 1)
    Z_PARAM_ZVAL(zv)
    ZEND_PARSE_PARAMETERS_END_EX(return );

    PyObject *pv = PyFloat_FromDouble(zval_get_double(zv));
    phpy::php::new_object(return_value, pv);
    Py_DECREF(pv);
}

ZEND_METHOD(PyCore, fn) {
    zval *zv;

    ZEND_PARSE_PARAMETERS_START(1, 1)
    Z_PARAM_ZVAL(zv)
    ZEND_PARSE_PARAMETERS_END_EX(return );

    PyObject *pv = phpy::python::new_callable(zv);
    phpy::php::new_fn(return_value, pv);
    Py_DECREF(pv);
}

ZEND_METHOD(PyCore, scalar) {
    auto pyobj = arg_1(INTERNAL_FUNCTION_PARAM_PASSTHRU, phpy_object_get_ce());
    CHECK_ARG(pyobj);
    py2php_scalar(pyobj, return_value);
    Py_DECREF(pyobj);
}

ZEND_METHOD(PyCore, setOptions) {
    zval *options;

    ZEND_PARSE_PARAMETERS_START(1, 1)
    Z_PARAM_ARRAY(options)
    ZEND_PARSE_PARAMETERS_END_EX(return );

    zval *opt;

    if ((opt = phpy::php::array_get(options, ZEND_STRL("numeric_as_object")))) {
        phpy_options.numeric_as_object = zend_is_true(opt);
    }
    if ((opt = phpy::php::array_get(options, ZEND_STRL("argument_as_object")))) {
        phpy_options.argument_as_object = zend_is_true(opt);
    }
    if ((opt = phpy::php::array_get(options, ZEND_STRL("display_exception")))) {
        phpy_options.display_exception = zend_is_true(opt);
    }
}

int php_class_core_init(INIT_FUNC_ARGS) {
    zend_class_entry ce;
    INIT_CLASS_ENTRY(ce, "PyCore", class_PyCore_methods);
    PyCore_ce = zend_register_internal_class(&ce);

    return SUCCESS;
}

void php_class_init_all(INIT_FUNC_ARGS) {
    // All Python built-in functions are static methods of Core class
    php_class_core_init(INIT_FUNC_ARGS_PASSTHRU);
    // PyObject is the parent class of all other classes
    php_class_object_init(INIT_FUNC_ARGS_PASSTHRU);
    php_class_str_init(INIT_FUNC_ARGS_PASSTHRU);
    php_class_module_init(INIT_FUNC_ARGS_PASSTHRU);
    php_class_dict_init(INIT_FUNC_ARGS_PASSTHRU);
    // Sequence Types — list, tuple, range
    php_class_sequence_init(INIT_FUNC_ARGS_PASSTHRU);
    php_class_list_init(INIT_FUNC_ARGS_PASSTHRU);
    php_class_tuple_init(INIT_FUNC_ARGS_PASSTHRU);
    // Hash Set
    php_class_set_init(INIT_FUNC_ARGS_PASSTHRU);
    // Type
    php_class_type_init(INIT_FUNC_ARGS_PASSTHRU);
    // Callable
    php_class_fn_init(INIT_FUNC_ARGS_PASSTHRU);
    // Iter
    php_class_iter_init(INIT_FUNC_ARGS_PASSTHRU);
    // Error
    php_class_error_init(INIT_FUNC_ARGS_PASSTHRU);
}

PyMODINIT_FUNC php_init_python_module(void) {
    return py_module_create(true);
}

PHP_MINIT_FUNCTION(phpy) {
    if (phpy_init(PHPY_PHP_EXTENSION) < 0) {
        zend_error(E_ERROR, "Error: phpy has been initialized");
        return FAILURE;
    }
    if (PyImport_AppendInittab("phpy", php_init_python_module) == -1) {
        zend_error(E_ERROR, "Error: failed to call PyImport_AppendInittab()");
        return FAILURE;
    }
    srand(time(NULL));

#if PY_VERSION_HEX >= 0x03080000
    // doc: https://docs.python.org/3/c-api/init_config.html
    PyConfig py_config;
    PyConfig_InitPythonConfig(&py_config);
    py_config.install_signal_handlers = 0;  // ignore signal
    py_config.parse_argv = 0;
    Py_InitializeFromConfig(&py_config);
    PyConfig_Clear(&py_config);
#else
    Py_InitializeEx(0);
#endif

    module_phpy = PyImport_ImportModule("phpy");
    if (!module_phpy) {
        PyErr_Print();
        zend_error(E_ERROR, "Error: could not import module 'phpy'");
        return FAILURE;
    }

    module_builtins = PyImport_ImportModule("builtins");
    if (!module_builtins) {
        PyErr_Print();
        zend_error(E_ERROR, "Error: could not import module 'builtins'");
        return FAILURE;
    }

    module_operator = PyImport_ImportModule("operator");
    if (!module_operator) {
        PyErr_Print();
        zend_error(E_ERROR, "Error: could not import module 'operator'");
        return FAILURE;
    }

    py_contains_operator = PyObject_GetAttrString(module_operator, "contains");
    if (!py_contains_operator) {
        PyErr_Print();
        zend_error(E_ERROR, "Error: could not get 'operator.contains'");
        return FAILURE;
    }

    php_class_init_all(INIT_FUNC_ARGS_PASSTHRU);
    return SUCCESS;
}

PHP_MSHUTDOWN_FUNCTION(phpy) {
    if (module_phpy) {
        Py_DECREF(module_phpy);
    }
    if (module_builtins) {
        Py_DECREF(module_builtins);
    }
    for (auto kv : builtin_functions) {
        Py_DECREF(kv.second);
    }
    builtin_functions.clear();

    for (auto kv : operator_functions) {
        Py_DECREF(kv.second);
    }
    operator_functions.clear();
    Py_DECREF(py_contains_operator);

    Py_Finalize();
    return SUCCESS;
}

namespace phpy {
namespace python {
bool contains(PyObject *obj, PyObject *key) {
    auto rs = PyObject_CallFunction(py_contains_operator, "OO", obj, key);
    return Py_IsTrue(rs);
}
}  // namespace python
namespace php {
void add_object(PyObject *pv, void (*dtor)(PyObject *)) {
    zend_objects.emplace(pv, dtor);
}

bool del_object(PyObject *pv) {
    return zend_objects.erase(pv) > 0;
}

void call_builtin_fn(const char *name, size_t l_name, zval *arguments, zval *return_value) {
    auto fn_iter = builtin_functions.find(name);
    PyObject *fn;
    if (fn_iter == builtin_functions.end()) {
        fn = PyObject_GetAttrString(module_builtins, name);
        if (!fn || !PyCallable_Check(fn)) {
            phpy::php::throw_error_if_occurred();
            return;
        }
        builtin_functions[name] = fn;
    } else {
        fn = fn_iter->second;
    }

    CallObject caller(fn, return_value, arguments);
    caller.call();
}

void call_operator_fn(const char *name, size_t l_name, zval *arguments, zval *return_value) {
    auto fn_iter = operator_functions.find(name);
    PyObject *fn;
    if (fn_iter == operator_functions.end()) {
        fn = PyObject_GetAttrString(module_operator, name);
        if (!fn || !PyCallable_Check(fn)) {
            phpy::php::throw_error_if_occurred();
            return;
        }
        operator_functions[name] = fn;
    } else {
        fn = fn_iter->second;
    }

    CallObject caller(fn, return_value, arguments);
    caller.call();
}
}  // namespace php
}  // namespace phpy

PHP_RSHUTDOWN_FUNCTION(phpy) {
    std::vector<std::pair<PyObject *, PyObjectDtor>> objects;
    objects.reserve(zend_objects.size());
    for (auto kv : zend_objects) {
        objects.push_back(std::make_pair(kv.first, kv.second));
    }
    for (auto kv : objects) {
        kv.second(kv.first);
    }
    zend_objects.clear();
    return SUCCESS;
}

BEGIN_EXTERN_C()
const char *phpy_get_python_version(void) {
    return Py_GetVersion();
}
END_EXTERN_C()

ZEND_METHOD(PyCore, __callStatic) {
    char *name;
    size_t l_name;
    zval *arguments;

    ZEND_PARSE_PARAMETERS_START(2, 2)
    Z_PARAM_STRING(name, l_name)
    Z_PARAM_ARRAY(arguments)
    ZEND_PARSE_PARAMETERS_END_EX(RETURN_FALSE);

    phpy::php::call_builtin_fn(name, l_name, arguments, return_value);
}

ZEND_METHOD(PyCore, bytes) {
    zval *zv = NULL;

    ZEND_PARSE_PARAMETERS_START(0, 1)
    Z_PARAM_OPTIONAL
    Z_PARAM_ZVAL(zv)
    ZEND_PARSE_PARAMETERS_END_EX(return );

    PyObject *pv;
    if (phpy::php::is_null(zv)) {
        pv = PyBytes_FromStringAndSize("", 0);
    } else if (phpy::php::is_string(zv)) {
        pv = PyBytes_FromStringAndSize(Z_STRVAL_P(zv), Z_STRLEN_P(zv));
    } else if (phpy::php::is_pyobject(zv)) {
        auto pyobj = phpy_object_get_handle(zv);
        pv = PyBytes_FromObject(pyobj);
    } else {
        auto s = zval_get_string(zv);
        pv = PyBytes_FromStringAndSize(Z_STRVAL_P(zv), Z_STRLEN_P(zv));
        zend_string_release(s);
    }
    phpy::php::new_object(return_value, pv);
    Py_DECREF(pv);
}

ZEND_METHOD(PyCore, fileno) {
    zval *zfp;

    ZEND_PARSE_PARAMETERS_START(1, 1)
    Z_PARAM_RESOURCE(zfp)
    ZEND_PARSE_PARAMETERS_END_EX(RETURN_FALSE);

    if (Z_TYPE_P(zfp) != IS_RESOURCE) {
        RETURN_FALSE;
    }

    php_socket_t fd = -1;
    php_stream *stream;
    FILE *fp = NULL;

    php_stream_from_zval_no_verify(stream, zfp);
    if (stream == NULL) {
        zend_throw_exception(zend_ce_exception, "Only stream type resource is supported", 0);
        RETURN_FALSE;
    }

#ifndef PHP_WIN32
    if (php_stream_is(stream, PHP_STREAM_IS_MEMORY) || php_stream_is(stream, PHP_STREAM_IS_TEMP)) {
        zend_throw_exception(zend_ce_exception, "Memory and temporary file stream is not supported", 0);
        RETURN_FALSE;
    } else
#endif
        if (php_stream_can_cast(stream, PHP_STREAM_AS_FD_FOR_SELECT | PHP_STREAM_CAST_INTERNAL) == SUCCESS) {
        if (php_stream_cast(stream, PHP_STREAM_AS_FD_FOR_SELECT | PHP_STREAM_CAST_INTERNAL, (void **) &fd, 1) !=
                SUCCESS ||
            fd < 0) {
            RETURN_FALSE;
        }
    } else if (php_stream_can_cast(stream, PHP_STREAM_AS_FD | PHP_STREAM_CAST_INTERNAL) == SUCCESS) {
        if (php_stream_cast(stream, PHP_STREAM_AS_FD | PHP_STREAM_CAST_INTERNAL, (void **) &fd, 1) != SUCCESS ||
            fd < 0) {
            RETURN_FALSE;
        }
    } else if (php_stream_can_cast(stream, PHP_STREAM_AS_STDIO | PHP_STREAM_CAST_INTERNAL) == SUCCESS) {
        if (php_stream_cast(stream, PHP_STREAM_AS_STDIO, (void **) &fp, 1) != SUCCESS) {
            RETURN_FALSE;
        }
        fd = fileno(fp);
    } else { /* STDIN, STDOUT, STDERR etc. */
        fd = Z_LVAL_P(zfp);
    }

    if (!ZEND_VALID_SOCKET(fd)) {
        zend_throw_exception(zend_ce_exception, "Invalid file descriptor", 0);
        RETURN_FALSE;
    } else {
        RETURN_LONG(fd);
    }
}

ZEND_METHOD(PyCore, raise) {
    zval *ztype, *zvalue = nullptr;

    ZEND_PARSE_PARAMETERS_START(1, 2)
    Z_PARAM_OBJECT_OF_CLASS(ztype, phpy_object_get_ce())
    Z_PARAM_OPTIONAL
    Z_PARAM_ZVAL(zvalue)
    ZEND_PARSE_PARAMETERS_END_EX(return );

    if (zvalue) {
        if (Z_TYPE_P(zvalue) == IS_OBJECT && phpy::php::is_pyobject(zvalue)) {
            PyErr_SetObject(phpy_object_get_handle(ztype), phpy_object_get_handle(zvalue));
        } else {
            zend_string *message = zval_get_string(zvalue);
            PyErr_SetString(phpy_object_get_handle(ztype), ZSTR_VAL(message));
            zend_string_release(message);
        }
    } else {
        PyErr_SetNone(phpy_object_get_handle(ztype));
    }
}
