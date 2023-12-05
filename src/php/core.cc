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

#include "stubs/phpy_core_arginfo.h"

static zend_class_entry *PyCore_ce;

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
    py2php(vars, return_value);
    Py_DECREF(vars);
}

ZEND_METHOD(PyCore, locals) {
    auto vars = PyEval_GetLocals();
    py2php(vars, return_value);
    Py_DECREF(vars);
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
}

PyMODINIT_FUNC php_init_python_module(void) {
    return py_module_create(true);
}

PHP_MINIT_FUNCTION(phpy) {
    if (PyImport_AppendInittab("phpy", php_init_python_module) == -1) {
        zend_error(E_ERROR, "Error: failed to call PyImport_AppendInittab()");
        return FAILURE;
    }
    Py_Initialize();
    PyObject *pmodule = PyImport_ImportModule("phpy");
    if (!pmodule) {
        PyErr_Print();
        zend_error(E_ERROR, "Error: could not import module 'phpy'");
        return FAILURE;
    }
    php_class_init_all(INIT_FUNC_ARGS_PASSTHRU);
    return SUCCESS;
}

PHP_MSHUTDOWN_FUNCTION(phpy) {
    Py_Finalize();
    return SUCCESS;
}
