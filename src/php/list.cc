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
#include "stubs/phpy_list_arginfo.h"
END_EXTERN_C()

zend_class_entry *PyList_ce;

using phpy::php::arg_1;
using phpy::php::construct_container;
using phpy::php::sequence_offset_get;
using phpy::python::LockGuard;
using phpy::python::OwnedPythonReference;

int php_class_list_init(INIT_FUNC_ARGS) {
    PyList_ce = phpy::php::register_internal_class("PyList", class_PyList_methods, phpy_sequence_get_ce());
    return SUCCESS;
}

namespace phpy {
namespace php {
void new_list(zval *zv, PyObject *list) {
    new_object(zv, list, PyList_ce);
}
}  // namespace php
}  // namespace phpy

ZEND_METHOD(PyList, __construct) {
    zval *zlist = NULL;
    ZEND_PARSE_PARAMETERS_START(0, 1)
    Z_PARAM_OPTIONAL
    Z_PARAM_ZVAL(zlist)
    ZEND_PARSE_PARAMETERS_END_EX(RETURN_FALSE);

    LOCK_GIL();
    PyObject *plist =
        construct_container(zlist, "PyList", []() { return PyList_New(0); }, [](zval *arg) { return array2list(arg); });
    if (plist == NULL) {
        phpy::php::throw_error_if_occurred();
        return;
    }
    phpy_object_ctor(ZEND_THIS, plist);
}

ZEND_METHOD(PyList, offsetGet) {
    auto pk = phpy::php::get_key(INTERNAL_FUNCTION_PARAM_PASSTHRU);
    auto object = phpy_object_get_handle(ZEND_THIS);
    LOCK_GIL();
    sequence_offset_get(
        object, pk, "PyList", [](PyObject *o) { return PyList_GET_SIZE(o); }, PyList_GetItem, return_value);
}

ZEND_METHOD(PyList, offsetSet) {
    zval *zv;
    zval *zk;

    ZEND_PARSE_PARAMETERS_START(2, 2)
    Z_PARAM_ZVAL(zk)
    Z_PARAM_ZVAL(zv)
    ZEND_PARSE_PARAMETERS_END_EX(RETURN_FALSE);

    auto object = phpy_object_get_handle(ZEND_THIS);
    LOCK_GIL();
    OwnedPythonReference value(php2py(zv));
    if (!value) {
        phpy::php::throw_error_if_occurred();
        return;
    }
    int result;
    if (zk == NULL || ZVAL_IS_NULL(zk)) {
        result = PyList_Append(object, value.get());
    } else {
        const auto requested = static_cast<ssize_t>(zval_get_long(zk));
        ssize_t index;
        if (!phpy::php::normalize_index(object, PyList_GET_SIZE(object), requested, &index)) {
            zend_throw_error(NULL, "PyList: index[%ld] out of range", requested);
            return;
        }
        Py_INCREF(value.get());
        // PyList_SetItem()
        // Not increase reference count of the value
        result = PyList_SetItem(object, index, value.get());
    }
    if (result < 0) {
        phpy::php::throw_error_if_occurred();
    }
}

ZEND_METHOD(PyList, offsetUnset) {
    auto requested = phpy::php::get_key(INTERNAL_FUNCTION_PARAM_PASSTHRU);
    auto object = phpy_object_get_handle(ZEND_THIS);
    LOCK_GIL();
    ssize_t index;
    if (!phpy::php::normalize_index(object, PyList_GET_SIZE(object), requested, &index)) {
        return;
    }
    if (PySequence_DelItem(object, index) < 0) {
        phpy::php::throw_error_if_occurred();
    }
}

ZEND_METHOD(PyList, offsetExists) {
    auto pk = phpy::php::get_key(INTERNAL_FUNCTION_PARAM_PASSTHRU);
    auto object = phpy_object_get_handle(ZEND_THIS);
    LOCK_GIL();
    ssize_t index;
    if (!phpy::php::normalize_index(object, PyList_GET_SIZE(object), pk, &index)) {
        RETURN_FALSE;
    }
    RETVAL_BOOL(!Py_IsNone(PyList_GET_ITEM(object, index)));
}
