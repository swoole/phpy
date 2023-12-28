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
#include "stubs/phpy_set_arginfo.h"
END_EXTERN_C()

zend_class_entry *PySet_ce;

using phpy::php::arg_1;

int php_class_set_init(INIT_FUNC_ARGS) {
    zend_class_entry ce;
    INIT_CLASS_ENTRY(ce, "PySet", class_PySet_methods);
    PySet_ce = zend_register_internal_class_ex(&ce, phpy_object_get_ce());
    PySet_ce->ce_flags |= ZEND_ACC_FINAL | ZEND_ACC_NO_DYNAMIC_PROPERTIES | ZEND_ACC_NOT_SERIALIZABLE;
    zend_class_implements(PySet_ce, 2, zend_ce_iterator, zend_ce_countable);
    return SUCCESS;
}

namespace phpy {
namespace php {
void new_set(zval *zv, PyObject *list) {
    new_object(zv, list, PySet_ce);
}
}  // namespace php
}  // namespace phpy

ZEND_METHOD(PySet, __construct) {
    zval *zset = NULL;
    ZEND_PARSE_PARAMETERS_START(0, 1)
    Z_PARAM_OPTIONAL
    Z_PARAM_ZVAL(zset)
    ZEND_PARSE_PARAMETERS_END_EX(RETURN_FALSE);

    PyObject *pset;
    if (phpy::php::is_null(zset)) {
        pset = PySet_New(0);
    } else {
        pset = array2set(zset);
    }
    phpy_object_ctor(ZEND_THIS, pset);
}

ZEND_METHOD(PySet, rewind) {
    phpy_object_iterator_reset(ZEND_THIS);
}

ZEND_METHOD(PySet, next) {
    phpy_object_iterator_next(ZEND_THIS);
}

ZEND_METHOD(PySet, valid) {
    RETURN_BOOL(phpy_object_iterator_valid(ZEND_THIS));
}

ZEND_METHOD(PySet, key) {}

ZEND_METHOD(PySet, current) {
    auto current = phpy_object_iterator_current(ZEND_THIS);
    if (current == NULL) {
        return;
    }
    py2php(current, return_value);
}

ZEND_METHOD(PySet, count) {
    auto object = phpy_object_get_handle(ZEND_THIS);
    RETURN_LONG(PySet_Size(object));
}

ZEND_METHOD(PySet, contains) {
    auto object = phpy_object_get_handle(ZEND_THIS);
    auto pk = arg_1(INTERNAL_FUNCTION_PARAM_PASSTHRU);
    RETURN_BOOL(PySet_Contains(object, pk));
}
