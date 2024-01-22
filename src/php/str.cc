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
#include "stubs/phpy_str_arginfo.h"
END_EXTERN_C()

zend_class_entry *PyStr_ce;

namespace phpy {
namespace php {
void new_str(zval *zv, PyObject *str) {
    new_object(zv, str, PyStr_ce);
}
}  // namespace php
}  // namespace phpy

int php_class_str_init(INIT_FUNC_ARGS) {
    zend_class_entry ce;
    INIT_CLASS_ENTRY(ce, "PyStr", class_PyStr_methods);
    PyStr_ce = zend_register_internal_class_ex(&ce, phpy_object_get_ce());
    PyStr_ce->ce_flags |= ZEND_ACC_FINAL | ZEND_ACC_NO_DYNAMIC_PROPERTIES | ZEND_ACC_NOT_SERIALIZABLE;

    return SUCCESS;
}

ZEND_METHOD(PyStr, __construct) {
    zval *zstr;
    ZEND_PARSE_PARAMETERS_START(1, 1)
    Z_PARAM_ZVAL(zstr)
    ZEND_PARSE_PARAMETERS_END_EX(RETURN_FALSE);

    if (Z_TYPE_P(zstr) == IS_OBJECT && instanceof_function(Z_OBJCE_P(zstr), phpy_object_get_ce())) {
        PyObject *pyobj = phpy_object_get_handle(zstr);
        PyObject *pStr = PyUnicode_FromObject(pyobj);
        if (pStr == NULL) {
            phpy_object_ctor(ZEND_THIS, Py_None);
            Py_INCREF(Py_None);
            phpy::php::throw_error_if_occurred();
            return;
        }
        phpy_object_ctor(ZEND_THIS, pStr);
    } else {
        phpy_object_ctor(ZEND_THIS, PyUnicode_FromStringAndSize(Z_STRVAL_P(zstr), Z_STRLEN_P(zstr)));
    }
}
