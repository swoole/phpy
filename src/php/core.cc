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

#include "stubs/phpy_core_arginfo.h"

static zend_class_entry *PyCore_ce;
static PyObject *module_builtins = nullptr;
static PyObject *module_phpy = nullptr;
static std::unordered_map<const char *, PyObject *> builtin_functions;
static std::unordered_map<const char *, PyObject *> global_objects;

using phpy::CallObject;
using phpy::php::arg_1;
using phpy::php::arg_2;

ZEND_METHOD(PyCore, import) {
    size_t l_module;
    char *module;
    ZEND_PARSE_PARAMETERS_START(1, 1)
    Z_PARAM_STRING(module, l_module)
    ZEND_PARSE_PARAMETERS_END_EX(RETURN_FALSE);

    auto m = PyImport_ImportModule(module);
    if (m == NULL) {
        PyErr_Print();
        RETURN_FALSE;
    }
    phpy::php::new_module(return_value, m);
}

ZEND_METHOD(PyCore, dir) {
    auto pyobj = arg_1(INTERNAL_FUNCTION_PARAM_PASSTHRU, phpy_object_get_ce());
    CHECK_ARG(pyobj);
    py2php(PyObject_Dir(pyobj), return_value);
    Py_DECREF(pyobj);
}

ZEND_METHOD(PyCore, str) {
    auto pyobj = arg_1(INTERNAL_FUNCTION_PARAM_PASSTHRU, phpy_object_get_ce());
    CHECK_ARG(pyobj);
    py2php(PyObject_Str(pyobj), return_value);
    Py_DECREF(pyobj);
}

ZEND_METHOD(PyCore, eval) {
    size_t l_input_code;
    char *input_code;
    zval *global_params = NULL;
    //第一个参数是要执行的代码，第二个参数是传入的变量（可选）
    ZEND_PARSE_PARAMETERS_START(1, 2)
    Z_PARAM_STRING(input_code, l_input_code)
    Z_PARAM_OPTIONAL
    Z_PARAM_ARRAY(global_params)
    ZEND_PARSE_PARAMETERS_END_EX(RETURN_FALSE);
    

    size_t module_name_length = 64;
    char module_name[module_name_length + 1];
    rand_string(module_name, module_name_length);

    PyObject *module = PyModule_New(module_name);
    if (module == NULL) {
        PyErr_Print();
        Py_DECREF(input_code);
        RETURN_FALSE;
    }
    // PyModule_GetDict 是取 module 的一个成员指针 *md_dict，也就是返回 module->md_dict
    // link:
    // https://github.com/python/cpython/blob/16448cab44e23d350824e9ac75e699f5bcc48a14/Include/internal/pycore_moduleobject.h#L37
    PyObject *globals = PyModule_GetDict(module);

    //如果传入了global_params，则把他合并到 globals 中（非覆盖的方式合并）
    if (!phpy::php::is_null(global_params)) {
        auto status = PyDict_Merge(globals, array2dict(global_params), 0);
        Py_DECREF(global_params);
        if (status != 0) {
            PyErr_Print();
            Py_DECREF(module);
            Py_DECREF(input_code);
            RETURN_FALSE;
        }
    }
    // globals 最终会形成 PyFrameConstructor.fc_globals 对象传给 _PyEval_Vector
    // locals 可以传 NULL，底层会自动赋值成 globals
    // link: 
    // https://github.com/python/cpython/blob/16448cab44e23d350824e9ac75e699f5bcc48a14/Python/ceval.c#L566
    PyObject *result = PyRun_StringFlags(input_code, Py_file_input, globals, NULL, NULL);
    if (result == NULL) {
        PyErr_Print();
        Py_DECREF(module);
        Py_DECREF(input_code);
        RETURN_FALSE;
    }
    phpy::php::new_module(return_value, module);
    // globals 是module的一个指针，存放了全局的变量，后面php中可能会访问到，如果释放会出现segmentation fault
    Py_DECREF(module);
    Py_DECREF(result);
    Py_DECREF(input_code);
}

ZEND_METHOD(PyCore, repr) {
    auto pyobj = arg_1(INTERNAL_FUNCTION_PARAM_PASSTHRU, phpy_object_get_ce());
    CHECK_ARG(pyobj);
    py2php(PyObject_Repr(pyobj), return_value);
    Py_DECREF(pyobj);
}

ZEND_METHOD(PyCore, type) {
    auto pyobj = arg_1(INTERNAL_FUNCTION_PARAM_PASSTHRU, phpy_object_get_ce());
    CHECK_ARG(pyobj);
    py2php(PyObject_Type(pyobj), return_value);
    Py_DECREF(pyobj);
}

ZEND_METHOD(PyCore, hash) {
    auto pyobj = arg_1(INTERNAL_FUNCTION_PARAM_PASSTHRU, phpy_object_get_ce());
    CHECK_ARG(pyobj);
    RETVAL_LONG(PyObject_Hash(pyobj));
    Py_DECREF(pyobj);
}

ZEND_METHOD(PyCore, hasattr) {
    auto objs = arg_2(INTERNAL_FUNCTION_PARAM_PASSTHRU);
    CHECK_ARG(std::get<0>(objs));
    CHECK_ARG(std::get<1>(objs));
    RETVAL_BOOL(PyObject_HasAttr(std::get<0>(objs), std::get<1>(objs)));
    Py_DECREF(std::get<0>(objs));
    Py_DECREF(std::get<1>(objs));
}

ZEND_METHOD(PyCore, id) {
    auto pyobj = arg_1(INTERNAL_FUNCTION_PARAM_PASSTHRU, phpy_object_get_ce());
    CHECK_ARG(pyobj);
    RETVAL_LONG((intptr_t) pyobj);
    Py_DECREF(pyobj);
}

ZEND_METHOD(PyCore, len) {
    auto pyobj = arg_1(INTERNAL_FUNCTION_PARAM_PASSTHRU, phpy_object_get_ce());
    CHECK_ARG(pyobj);
    RETVAL_LONG(PyObject_Size(pyobj));
    Py_DECREF(pyobj);
}

ZEND_METHOD(PyCore, globals) {
    auto vars = PyEval_GetGlobals();
    if (vars == NULL) {
        return;
    }
    py2php(vars, return_value);
    Py_DECREF(vars);
}

ZEND_METHOD(PyCore, locals) {
    auto vars = PyEval_GetLocals();
    if (vars == NULL) {
        return;
    }
    py2php(vars, return_value);
    Py_DECREF(vars);
}

ZEND_METHOD(PyCore, iter) {
    auto pyobj = arg_1(INTERNAL_FUNCTION_PARAM_PASSTHRU, phpy_object_get_ce());
    CHECK_ARG(pyobj);
    auto iter = PyObject_GetIter(pyobj);
    if (iter == NULL) {
        return;
    }
    phpy::php::new_iter(return_value, iter);
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

    PyObject *pv = callable2py(zv);
    phpy::php::new_fn(return_value, pv);
    Py_DECREF(pv);
}

ZEND_METHOD(PyCore, scalar) {
    auto pyobj = arg_1(INTERNAL_FUNCTION_PARAM_PASSTHRU, phpy_object_get_ce());
    CHECK_ARG(pyobj);
    py2php(pyobj, return_value, true);
    Py_DECREF(pyobj);
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
}

PyMODINIT_FUNC php_init_python_module(void) {
    return py_module_create(true);
}

PHP_MINIT_FUNCTION(phpy) {
    if (PyImport_AppendInittab("phpy", php_init_python_module) == -1) {
        zend_error(E_ERROR, "Error: failed to call PyImport_AppendInittab()");
        return FAILURE;
    }
    srand(time(NULL));
    Py_InitializeEx(0);
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
    Py_Finalize();
    return SUCCESS;
}

ZEND_METHOD(PyCore, callable) {
    auto pyobj = arg_1(INTERNAL_FUNCTION_PARAM_PASSTHRU, phpy_object_get_ce());
    CHECK_ARG(pyobj);
    RETVAL_BOOL(PyCallable_Check(pyobj));
    Py_DECREF(pyobj);
}

ZEND_METHOD(PyCore, __callStatic) {
    char *name;
    size_t l_name;
    zval *arguments;

    ZEND_PARSE_PARAMETERS_START(2, 2)
    Z_PARAM_STRING(name, l_name)
    Z_PARAM_ARRAY(arguments)
    ZEND_PARSE_PARAMETERS_END_EX(RETURN_FALSE);

    auto fn_iter = builtin_functions.find(name);
    PyObject *fn;
    if (fn_iter == builtin_functions.end()) {
        fn = PyObject_GetAttrString(module_builtins, name);
        if (!fn || !PyCallable_Check(fn)) {
            zend_throw_error(NULL, "PyCore: has no builtin function '%s'", name);
            return;
        }
        builtin_functions[name] = fn;
    } else {
        fn = fn_iter->second;
    }

    CallObject caller(fn, return_value, arguments);
    caller.call();
}

ZEND_METHOD(PyCore, storage) {
    char *name;
    size_t l_name;
    zval *zobj;

    ZEND_PARSE_PARAMETERS_START(2, 2)
    Z_PARAM_STRING(name, l_name)
    Z_PARAM_OBJECT_OF_CLASS(zobj, phpy_object_get_ce())
    ZEND_PARSE_PARAMETERS_END_EX(RETURN_FALSE);

    auto pyobj = php2py(zobj);
    CHECK_ARG(pyobj);

    auto iter = global_objects.find(name);
    if (iter != global_objects.end()) {
        phpy::php::new_object(return_value, iter->second);
        Py_DECREF(iter->second);
        global_objects.erase(iter);
    }
    Py_INCREF(pyobj);
    global_objects.emplace(name, pyobj);
}

ZEND_METHOD(PyCore, fetch) {
    char *name;
    size_t l_name;

    ZEND_PARSE_PARAMETERS_START(1, 1)
    Z_PARAM_STRING(name, l_name)
    ZEND_PARSE_PARAMETERS_END_EX(RETURN_FALSE);

    auto iter = global_objects.find(name);
    if (iter != global_objects.end()) {
        py2php(iter->second, return_value);
    }
}

ZEND_METHOD(PyCore, remove) {
    char *name;
    size_t l_name;

    ZEND_PARSE_PARAMETERS_START(1, 1)
    Z_PARAM_STRING(name, l_name)
    ZEND_PARSE_PARAMETERS_END_EX(RETURN_FALSE);

    auto iter = global_objects.find(name);
    if (iter != global_objects.end()) {
        Py_DECREF(iter->second);
        global_objects.erase(iter);
        RETURN_TRUE;
    } else {
        RETURN_FALSE;
    }
}
