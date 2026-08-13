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
#include "stubs/phpy_dict_arginfo.h"
END_EXTERN_C()

zend_class_entry *PyDict_ce;

int php_class_dict_init(INIT_FUNC_ARGS) {
    zend_class_entry ce;
    INIT_CLASS_ENTRY(ce, "PyDict", class_PyDict_methods);
    PyDict_ce = zend_register_internal_class_ex(&ce, phpy_object_get_ce());
    PyDict_ce->ce_flags |= ZEND_ACC_FINAL | ZEND_ACC_NO_DYNAMIC_PROPERTIES | ZEND_ACC_NOT_SERIALIZABLE;
    return SUCCESS;
}

namespace phpy {
namespace php {
void new_dict(zval *zv, PyObject *dict) {
    new_object(zv, dict, PyDict_ce);
}
}  // namespace php
}  // namespace phpy

using phpy::php::arg_1;
using phpy::python::LockGuard;

ZEND_METHOD(PyDict, __construct) {
    zval *zdict = NULL;
    ZEND_PARSE_PARAMETERS_START(0, 1)
    Z_PARAM_OPTIONAL
    Z_PARAM_ZVAL(zdict)
    ZEND_PARSE_PARAMETERS_END_EX(RETURN_FALSE);

    PyObject *pdict;
    LOCK_GIL();
    if (phpy::php::is_null(zdict) || phpy::php::is_empty_array(zdict)) {
        pdict = PyDict_New();
    } else if (phpy::php::is_array(zdict)) {
        pdict = array2dict(zdict);
    } else {
        zend_throw_error(NULL, "PyDict: unsupported type");
        return;
    }
    if (pdict == NULL) {
        phpy::php::throw_error_if_occurred();
        return;
    }
    phpy_object_ctor(ZEND_THIS, pdict);
}

ZEND_METHOD(PyDict, offsetGet) {
    LOCK_GIL();
    phpy::python::OwnedPythonReference key(arg_1(INTERNAL_FUNCTION_PARAM_PASSTHRU));
    CHECK_ARG(key.get());
    auto object = phpy_object_get_handle(ZEND_THIS);
    auto value = PyDict_GetItemWithError(object, key.get());
    if (value == NULL) {
        phpy::php::throw_error_if_occurred();
        return;
    }
    py2php(value, return_value);
}

ZEND_METHOD(PyDict, offsetSet) {
    zval *zv;
    zval *zk;

    ZEND_PARSE_PARAMETERS_START(2, 2)
    Z_PARAM_ZVAL(zk)
    Z_PARAM_ZVAL(zv)
    ZEND_PARSE_PARAMETERS_END_EX(RETURN_FALSE);

    auto object = phpy_object_get_handle(ZEND_THIS);
    LOCK_GIL();
    phpy::python::OwnedPythonReference key(php2py(zk));
    if (!key) {
        phpy::php::throw_error_if_occurred();
        return;
    }
    phpy::python::OwnedPythonReference value(php2py(zv));
    if (!value) {
        phpy::php::throw_error_if_occurred();
        return;
    }
    auto result = PyDict_SetItem(object, key.get(), value.get());
    if (result < 0) {
        phpy::php::throw_error_if_occurred();
    }
}

ZEND_METHOD(PyDict, offsetUnset) {
    LOCK_GIL();
    phpy::python::OwnedPythonReference key(arg_1(INTERNAL_FUNCTION_PARAM_PASSTHRU));
    CHECK_ARG(key.get());
    auto object = phpy_object_get_handle(ZEND_THIS);
    auto result = PyDict_DelItem(object, key.get());
    if (result < 0) {
        if (PyErr_ExceptionMatches(PyExc_KeyError)) {
            PyErr_Clear();
            return;
        }
        phpy::php::throw_error_if_occurred();
    }
}

ZEND_METHOD(PyDict, offsetExists) {
    LOCK_GIL();
    phpy::python::OwnedPythonReference key(arg_1(INTERNAL_FUNCTION_PARAM_PASSTHRU));
    CHECK_ARG(key.get());
    auto object = phpy_object_get_handle(ZEND_THIS);
    auto value = PyDict_GetItemWithError(object, key.get());
    if (value == NULL && PyErr_Occurred()) {
        phpy::php::throw_error_if_occurred();
        return;
    }
    RETVAL_BOOL(value != NULL && !Py_IsNone(value));
}

ZEND_METHOD(PyDict, key) {
    auto current = phpy_object_iterator_current(ZEND_THIS);
    if (current == NULL) {
        return;
    }
    zval key_zv;
    LOCK_GIL();
    py2php(current, &key_zv);
    if (Z_TYPE(key_zv) == IS_LONG || Z_TYPE(key_zv) == IS_STRING) {
        RETURN_ZVAL(&key_zv, 0, 0);
    } else {
        convert_to_string(&key_zv);
        RETURN_ZVAL(&key_zv, 0, 0);
    }
}

ZEND_METHOD(PyDict, current) {
    auto object = phpy_object_get_handle(ZEND_THIS);
    auto current = phpy_object_iterator_current(ZEND_THIS);
    if (current == NULL) {
        return;
    }
    LOCK_GIL();
    auto value = PyDict_GetItem(object, current);
    if (value != NULL) {
        py2php(value, return_value);
    }
}

ZEND_METHOD(PyDict, count) {
    auto object = phpy_object_get_handle(ZEND_THIS);
    LOCK_GIL();
    RETURN_LONG(PyDict_Size(object));
}
