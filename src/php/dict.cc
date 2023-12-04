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
#include "zend_interfaces.h"

BEGIN_EXTERN_C()
#include "stubs/phpy_dict_arginfo.h"
END_EXTERN_C()

zend_class_entry *PyDict_ce;

int php_class_dict_init(INIT_FUNC_ARGS) {
    zend_class_entry ce;
    INIT_CLASS_ENTRY(ce, "PyDict", class_PyDict_methods);
    PyDict_ce = zend_register_internal_class_ex(&ce, phpy_object_get_ce());
    PyDict_ce->ce_flags |= ZEND_ACC_FINAL | ZEND_ACC_NO_DYNAMIC_PROPERTIES | ZEND_ACC_NOT_SERIALIZABLE;
    zend_class_implements(PyDict_ce, 3, zend_ce_iterator, zend_ce_arrayaccess, zend_ce_countable);
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

ZEND_METHOD(PyDict, __construct) {
    zval *zdict = NULL;
    ZEND_PARSE_PARAMETERS_START(0, 1)
    Z_PARAM_OPTIONAL
    Z_PARAM_ZVAL(zdict)
    ZEND_PARSE_PARAMETERS_END_EX(RETURN_FALSE);

    PyObject *pdict;
    if (phpy::php::is_null(zdict)) {
        pdict = PyDict_New();
    } else {
        pdict = array2dict(zdict);
    }
    phpy_object_ctor(ZEND_THIS, pdict);
}

ZEND_METHOD(PyDict, offsetGet) {
    auto pk = arg_1(INTERNAL_FUNCTION_PARAM_PASSTHRU);
    auto object = phpy_object_get_handle(ZEND_THIS);
    ON_SCOPE_EXIT {
        Py_DECREF(pk);
    };
    auto value = PyDict_GetItem(object, pk);
    if (value == NULL) {
        ssize_t len;
        zend_throw_error(NULL, "PyDict: error key [%s]", object2str(pk, &len));
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
    PyObject *pv = php2py(zv);
    PyObject *pk = php2py(zk);
    ON_SCOPE_EXIT {
        Py_DECREF(pv);
        Py_DECREF(pk);
    };
    auto value = PyDict_SetItem(object, pk, pv);
    if (value < 0) {
        zend_throw_error(NULL, "PyDict: cannot write attribute");
    }
}

ZEND_METHOD(PyDict, offsetUnset) {
    auto pk = arg_1(INTERNAL_FUNCTION_PARAM_PASSTHRU);
    auto object = phpy_object_get_handle(ZEND_THIS);
    PyDict_DelItem(object, pk);
    Py_DECREF(pk);
}

ZEND_METHOD(PyDict, offsetExists) {
    auto pk = arg_1(INTERNAL_FUNCTION_PARAM_PASSTHRU);
    auto object = phpy_object_get_handle(ZEND_THIS);
    RETVAL_BOOL(PyDict_Contains(object, pk));
    Py_DECREF(pk);
}

ZEND_METHOD(PyDict, rewind) {
    phpy_object_iterator_reset(ZEND_THIS);
}

ZEND_METHOD(PyDict, next) {
    phpy_object_iterator_next(ZEND_THIS);
}

ZEND_METHOD(PyDict, valid) {
    RETURN_BOOL(phpy_object_iterator_valid(ZEND_THIS));
}

ZEND_METHOD(PyDict, key) {
    auto current = phpy_object_iterator_current(ZEND_THIS);
    py2php(current, return_value);
}

ZEND_METHOD(PyDict, current) {
    auto object = phpy_object_get_handle(ZEND_THIS);
    auto current = phpy_object_iterator_current(ZEND_THIS);
    auto value = PyDict_GetItem(object, current);
    if (value != NULL) {
        py2php(value, return_value);
    }
}

ZEND_METHOD(PyDict, count) {
    auto object = phpy_object_get_handle(ZEND_THIS);
    RETURN_LONG(PyDict_Size(object));
}
