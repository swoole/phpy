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
#include "stubs/phpy_fn_arginfo.h"
END_EXTERN_C()

using phpy::python::LockGuard;
zend_class_entry *PyFn_ce;

namespace phpy {
namespace php {
void new_fn(zval *zv, PyObject *fn) {
    new_object(zv, fn, PyFn_ce);
}
}  // namespace php
}  // namespace phpy

int php_class_fn_init(INIT_FUNC_ARGS) {
    PyFn_ce = phpy::php::register_internal_class("PyFn", class_PyFn_methods, phpy_object_get_ce());

    return SUCCESS;
}

ZEND_METHOD(PyFn, __construct) {
    zval *zfn;
    ZEND_PARSE_PARAMETERS_START(1, 1)
    Z_PARAM_ZVAL(zfn)
    ZEND_PARSE_PARAMETERS_END_EX(RETURN_FALSE);

    LOCK_GIL();
    PyObject *pv = phpy::python::new_callable(zfn);
    phpy_object_ctor(ZEND_THIS, pv);
}
