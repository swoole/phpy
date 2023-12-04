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

struct ZendResource;
static void Resource_destroy(ZendResource *self);

// clang-format off
struct ZendResource {
    PyObject_HEAD
    zval resource;
};

static PyTypeObject ZendResourceType = {
    .ob_base = PyVarObject_HEAD_INIT(NULL, 0)
    .tp_name = "zend_resource",
    .tp_basicsize = sizeof(ZendResource),
    .tp_itemsize = 0,
    .tp_dealloc = (destructor) Resource_destroy,
    .tp_flags = Py_TPFLAGS_DEFAULT,
    .tp_doc = PyDoc_STR("zend_resource"),
    .tp_new = PyType_GenericNew,
};

//  clang-format on

PyObject* resource2py(zval *zv) {
    ZendResource *res = PyObject_New(ZendResource, &ZendResourceType);
    res->resource = *zv;
    zval_add_ref(&res->resource);
    return (PyObject*) res;
}

zval *zend_resource_cast(PyObject *pv) {
    ZendResource *obj = (ZendResource *) pv;
    return &obj->resource;
}

bool ZendResource_Check(PyObject *pv) {
    return Py_IS_TYPE(pv, &ZendResourceType);
}

static void Resource_destroy(ZendResource *self) {
    zval_ptr_dtor(&self->resource);
}

bool py_module_resource_init(PyObject *m) {
    if (PyType_Ready(&ZendResourceType) < 0) {
        return false;
    }
    Py_INCREF(&ZendResourceType);
    if (PyModule_AddObject(m, "Resource", (PyObject *) &ZendResourceType) < 0) {
        Py_DECREF(&ZendResourceType);
        Py_DECREF(m);
        return false;
    }
    return true;
}
