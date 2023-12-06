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
#include "stubs/phpy_iter_arginfo.h"
END_EXTERN_C()

zend_class_entry *PyIter_ce;

namespace phpy {
namespace php {
void new_iter(zval *zv, PyObject *type) {
    new_object(zv, type, PyIter_ce);
}
}  // namespace php
}  // namespace phpy

int php_class_iter_init(INIT_FUNC_ARGS) {
    zend_class_entry ce;
    INIT_CLASS_ENTRY(ce, "PyIter", class_PyIter_methods);
    PyIter_ce = zend_register_internal_class_ex(&ce, phpy_object_get_ce());
    PyIter_ce->ce_flags |= ZEND_ACC_FINAL | ZEND_ACC_NO_DYNAMIC_PROPERTIES | ZEND_ACC_NOT_SERIALIZABLE;

    return SUCCESS;
}

zend_class_entry *phpy_iter_get_ce() {
    return PyIter_ce;
}

ZEND_METHOD(PyIter, __construct) {

}
