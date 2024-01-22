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
#include "stubs/phpy_sequence_arginfo.h"
END_EXTERN_C()

zend_class_entry *PySequence_ce;

using phpy::php::arg_1;

int php_class_sequence_init(INIT_FUNC_ARGS) {
    zend_class_entry ce;
    INIT_CLASS_ENTRY(ce, "PySequence", class_PySequence_methods);
    PySequence_ce = zend_register_internal_class_ex(&ce, phpy_object_get_ce());
    PySequence_ce->ce_flags |= ZEND_ACC_ABSTRACT | ZEND_ACC_NO_DYNAMIC_PROPERTIES | ZEND_ACC_NOT_SERIALIZABLE;
    return SUCCESS;
}

zend_class_entry *phpy_sequence_get_ce() {
    return PySequence_ce;
}

ZEND_METHOD(PySequence, count) {
    auto object = phpy_object_get_handle(ZEND_THIS);
    RETURN_LONG(PySequence_Size(object));
}

ZEND_METHOD(PySequence, contains) {
    auto object = phpy_object_get_handle(ZEND_THIS);
    auto pv = arg_1(INTERNAL_FUNCTION_PARAM_PASSTHRU);
    RETURN_BOOL(PySequence_Contains(object, pv));
}

ZEND_METHOD(PySequence, slice) {
    zend_long v1, v2;

    ZEND_PARSE_PARAMETERS_START(2, 2)
    Z_PARAM_LONG(v1)
    Z_PARAM_LONG(v2)
    ZEND_PARSE_PARAMETERS_END_EX(RETURN_FALSE);

    auto object = phpy_object_get_handle(ZEND_THIS);
    py2php(PySequence_GetSlice(object, v1, v2), return_value);
}
