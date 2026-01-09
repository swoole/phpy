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
#include "zend_exceptions.h"

BEGIN_EXTERN_C()
#include "stubs/phpy_error_arginfo.h"
END_EXTERN_C()

zend_class_entry *PyError_ce;

namespace phpy {
namespace php {
/**
 * PyErr_Occurred(): Return value: Borrowed reference
 */
void new_error(zval *zv, PyObject *error) {
    object_init_ex(zv, PyError_ce);
    zval zerror;
    new_object(&zerror, error);
    zend_update_property(PyError_ce, Z_OBJ_P(zv), STR_AND_LEN("error"), &zerror);
    zval_ptr_dtor(&zerror);

    PyObject *ptype, *pvalue, *ptraceback;
    PyErr_Fetch(&ptype, &pvalue, &ptraceback);
    if (pvalue) {
        zval zvalue;
        new_object(&zvalue, pvalue);
        zend_update_property(PyError_ce, Z_OBJ_P(zv), STR_AND_LEN("value"), &zvalue);
        zval_ptr_dtor(&zvalue);

        PyObject *pstr = PyObject_Str(pvalue);
        if (pstr) {
            phpy::StrObject msg(pstr);
            zend_update_property_stringl(PyError_ce, Z_OBJ_P(zv), STR_AND_LEN("message"), msg.val(), msg.len());
        }
    }
    if (ptype) {
        zval ztype;
        new_object(&ztype, ptype);
        zend_update_property(PyError_ce, Z_OBJ_P(zv), STR_AND_LEN("type"), &ztype);
        zval_ptr_dtor(&ztype);
    }
    if (ptraceback) {
        zval ztraceback;
        new_object(&ztraceback, ptraceback);
        zend_update_property(PyError_ce, Z_OBJ_P(zv), STR_AND_LEN("traceback"), &ztraceback);
        zval_ptr_dtor(&ztraceback);
    }
}

void throw_error(PyObject *error) {
    zval exception;
    new_error(&exception, error);
    zend_throw_exception_object(&exception);
}
}  // namespace php
}  // namespace phpy

int php_class_error_init(INIT_FUNC_ARGS) {
    zend_class_entry ce;
    INIT_CLASS_ENTRY(ce, "PyError", class_PyError_methods);
    PyError_ce = zend_register_internal_class_ex(&ce, zend_ce_exception);
    PyError_ce->ce_flags |= ZEND_ACC_FINAL | ZEND_ACC_NO_DYNAMIC_PROPERTIES | ZEND_ACC_NOT_SERIALIZABLE;

    zend_declare_property_null(PyError_ce, STR_AND_LEN("error"), ZEND_ACC_PUBLIC);
    zend_declare_property_null(PyError_ce, STR_AND_LEN("type"), ZEND_ACC_PUBLIC);
    zend_declare_property_null(PyError_ce, STR_AND_LEN("value"), ZEND_ACC_PUBLIC);
    zend_declare_property_null(PyError_ce, STR_AND_LEN("traceback"), ZEND_ACC_PUBLIC);

    return SUCCESS;
}
