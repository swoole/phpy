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

static PyTypeObject ZendResourceType = { PyVarObject_HEAD_INIT(NULL, 0) };

// clang-format on

static void Resource_dtor(PyObject *pv) {
    ZendResource *self = (ZendResource *) pv;
    zval_ptr_dtor(&self->resource);
    ZVAL_NULL(&self->resource);
}

namespace phpy {
namespace python {
PyObject *new_resource(zval *zv) {
    ZendResource *pyobj = PyObject_New(ZendResource, &ZendResourceType);
    pyobj->resource = *zv;
    phpy::php::add_object((PyObject *) pyobj, Resource_dtor);
    zval_add_ref(&pyobj->resource);
    return (PyObject *) pyobj;
}
}  // namespace python
}  // namespace phpy

zval *zend_resource_cast(PyObject *pv) {
    ZendResource *obj = (ZendResource *) pv;
    return &obj->resource;
}

bool ZendResource_Check(PyObject *pv) {
    return Py_IS_TYPE(pv, &ZendResourceType);
}

static void Resource_destroy(ZendResource *self) {
    if (phpy::php::del_object((PyObject *) self)) {
        Resource_dtor((PyObject *) self);
    }
}

bool py_module_resource_init(PyObject *m) {
    ZendResourceType.tp_name = "zend_resource";
    ZendResourceType.tp_basicsize = sizeof(ZendResource);
    ZendResourceType.tp_itemsize = 0;
    ZendResourceType.tp_dealloc = (destructor) Resource_destroy;
    ZendResourceType.tp_flags = Py_TPFLAGS_DEFAULT;
    ZendResourceType.tp_doc = PyDoc_STR("zend_resource");
    ZendResourceType.tp_new = PyType_GenericNew;

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
