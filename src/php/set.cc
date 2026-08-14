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
#include "stubs/phpy_set_arginfo.h"
END_EXTERN_C()

zend_class_entry *PySet_ce;

using phpy::php::arg_1;
using phpy::php::construct_container;
using phpy::python::LockGuard;
using phpy::python::OwnedPythonReference;

int php_class_set_init(INIT_FUNC_ARGS) {
    PySet_ce = phpy::php::register_internal_class("PySet", class_PySet_methods, phpy_object_get_ce());
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

    LOCK_GIL();
    PyObject *pset = construct_container(
        zset, "PySet", []() { return PySet_New(nullptr); }, [](zval *arg) { return array2set(arg); });
    if (pset == NULL) {
        phpy::php::throw_error_if_occurred();
        return;
    }
    phpy_object_ctor(ZEND_THIS, pset);
}

ZEND_METHOD(PySet, count) {
    auto object = phpy_object_get_handle(ZEND_THIS);
    LOCK_GIL();
    RETURN_LONG(PySet_Size(object));
}

ZEND_METHOD(PySet, contains) {
    auto object = phpy_object_get_handle(ZEND_THIS);
    LOCK_GIL();
    OwnedPythonReference key(arg_1(INTERNAL_FUNCTION_PARAM_PASSTHRU));
    CHECK_ARG(key.get());
    const int result = PySet_Contains(object, key.get());
    if (result < 0) {
        phpy::php::throw_error_if_occurred();
        return;
    }
    RETURN_BOOL(result);
}
