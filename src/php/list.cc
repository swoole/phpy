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
using phpy::python::LockGuard;

int php_class_list_init(INIT_FUNC_ARGS) {
    zend_class_entry ce;
    INIT_CLASS_ENTRY(ce, "PyList", class_PyList_methods);
    PyList_ce = zend_register_internal_class_ex(&ce, phpy_sequence_get_ce());
    PyList_ce->ce_flags |= ZEND_ACC_FINAL | ZEND_ACC_NO_DYNAMIC_PROPERTIES | ZEND_ACC_NOT_SERIALIZABLE;
    return SUCCESS;
}

namespace phpy {
namespace php {
void new_list(zval *zv, PyObject *list) {
    new_object(zv, list, PyList_ce);
}
}  // namespace php
}  // namespace phpy

static ssize_t get_key(INTERNAL_FUNCTION_PARAMETERS) {
    zend_long k;

    ZEND_PARSE_PARAMETERS_START(1, 1)
    Z_PARAM_LONG(k)
    ZEND_PARSE_PARAMETERS_END_EX(return 0);

    return (ssize_t) k;
}

static bool normalize_index(PyObject *list, ssize_t index, ssize_t *normalized) {
    const auto size = PyList_GET_SIZE(list);
    if (index < 0) {
        index += size;
    }
    if (index < 0 || index >= size) {
        return false;
    }
    *normalized = index;
    return true;
}

ZEND_METHOD(PyList, __construct) {
    zval *zlist = NULL;
    ZEND_PARSE_PARAMETERS_START(0, 1)
    Z_PARAM_OPTIONAL
    Z_PARAM_ZVAL(zlist)
    ZEND_PARSE_PARAMETERS_END_EX(RETURN_FALSE);

    LOCK_GIL();
    PyObject *plist;
    if (phpy::php::is_null(zlist) || phpy::php::is_empty_array(zlist)) {
        plist = PyList_New(0);
    } else if (phpy::php::is_array(zlist)) {
        plist = array2list(zlist);
    } else {
        zend_throw_error(NULL, "PyList: unsupported type");
        return;
    }
    phpy_object_ctor(ZEND_THIS, plist);
}

ZEND_METHOD(PyList, offsetGet) {
    auto pk = get_key(INTERNAL_FUNCTION_PARAM_PASSTHRU);
    auto object = phpy_object_get_handle(ZEND_THIS);
    LOCK_GIL();
    ssize_t index;
    if (!normalize_index(object, pk, &index)) {
        zend_throw_error(NULL, "PyList: index[%ld] out of range", pk);
        return;
    }
    // PyList_GetItem()
    // Return value: Borrowed reference
    auto value = PyList_GetItem(object, index);
    if (value != NULL) {
        py2php(value, return_value);
    }
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
    PyObject *pv = php2py(zv);
    int result;
    if (zk == NULL || ZVAL_IS_NULL(zk)) {
        result = PyList_Append(object, pv);
    } else {
        const auto requested = static_cast<ssize_t>(zval_get_long(zk));
        ssize_t index;
        if (!normalize_index(object, requested, &index)) {
            Py_DECREF(pv);
            zend_throw_error(NULL, "PyList: index[%ld] out of range", requested);
            return;
        }
        Py_INCREF(pv);
        // PyList_SetItem()
        // Not increase reference count of the value
        result = PyList_SetItem(object, index, pv);
    }
    Py_DECREF(pv);
    if (result < 0) {
        phpy::php::throw_error_if_occurred();
    }
}

ZEND_METHOD(PyList, offsetUnset) {
    auto requested = get_key(INTERNAL_FUNCTION_PARAM_PASSTHRU);
    auto object = phpy_object_get_handle(ZEND_THIS);
    LOCK_GIL();
    ssize_t index;
    if (!normalize_index(object, requested, &index)) {
        return;
    }
    if (PySequence_DelItem(object, index) < 0) {
        phpy::php::throw_error_if_occurred();
    }
}

ZEND_METHOD(PyList, offsetExists) {
    auto pk = get_key(INTERNAL_FUNCTION_PARAM_PASSTHRU);
    auto object = phpy_object_get_handle(ZEND_THIS);
    LOCK_GIL();
    ssize_t index;
    if (!normalize_index(object, pk, &index)) {
        RETURN_FALSE;
    }
    RETVAL_BOOL(!Py_IsNone(PyList_GET_ITEM(object, index)));
}
