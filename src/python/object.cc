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

#define CTOR_NAME "__construct"

struct ZendObject;
static int Object_init(ZendObject *self, PyObject *args, PyObject *kwds);
static PyObject *Object_call(ZendObject *self, PyObject *args);
static PyObject *Object_get(ZendObject *self, PyObject *args);
static PyObject *Object_set(ZendObject *self, PyObject *args);
static void Object_destroy(ZendObject *self);

// clang-format off
struct ZendObject {
    PyObject_HEAD
    zval object;
};

static PyMethodDef Object_methods[] = {
    {"call", (PyCFunction) Object_call, METH_VARARGS, "Call object method" },
    {"get", (PyCFunction) Object_get, METH_VARARGS, "Get object property" },
    {"set", (PyCFunction) Object_set, METH_VARARGS, "Set object property" },
    {NULL}  /* Sentinel */
};

static PyTypeObject ZendObjectType = {
    .ob_base = PyVarObject_HEAD_INIT(NULL, 0)
    .tp_name = "zend.Object",
    .tp_basicsize = sizeof(ZendObject),
    .tp_itemsize = 0,
    .tp_dealloc = (destructor) Object_destroy,
    .tp_flags = Py_TPFLAGS_DEFAULT,
    .tp_doc = PyDoc_STR("zend_object"),
    .tp_methods = Object_methods,
    .tp_init = (initproc) Object_init,
    .tp_new = PyType_GenericNew,
};
// clang-format on

static int Object_init(ZendObject *self, PyObject *args, PyObject *kwds) {
    Py_ssize_t TupleSize = PyTuple_Size(args);
    if (!TupleSize) {
        PyErr_SetString(PyExc_TypeError, "must supply at least 1 parameter.");
        return -1;
    }

    PyObject *name = PyTuple_GetItem(args, 0);
    if (!PyUnicode_Check(name)) {
        PyErr_SetString(PyExc_TypeError, "class name must be string");
        return -1;
    }

    zend_string *_class_name = zend_string_cast(name);
    zend_class_entry *ce = zend_lookup_class(_class_name);
    zend_string_release(_class_name);

    if (ce == NULL) {
        PyErr_Format(PyExc_TypeError, "Class \"%s\" not found", ZSTR_VAL(_class_name));
        return -1;
    }
    if (object_create((PyObject *) self, ce, args, TupleSize - 1, 1) == NULL) {
        return -1;
    }
    return 0;
}

static void Object_destroy(ZendObject *self) {
    zval_ptr_dtor(&self->object);
    ZVAL_NULL(&self->object);
    Py_TYPE(self)->tp_free((PyObject *) self);
}

static PyObject *Object_call(ZendObject *self, PyObject *args) {
    Py_ssize_t TupleSize = PyTuple_Size(args);
    if (!TupleSize) {
        if (!PyErr_Occurred()) {
            PyErr_SetString(PyExc_TypeError, "must supply at least 1 parameter.");
        }
        return NULL;
    }

    PyObject *fn = PyTuple_GetItem(args, 0);
    if (!PyUnicode_Check(fn)) {
        PyErr_SetString(PyExc_TypeError, "method name must be string");
        return NULL;
    }

    uint32_t argc = TupleSize - 1;
    zval argv[argc];
    tuple2argv(argv, args, TupleSize);

    zval retval;
    zval zfn;
    py2php(fn, &zfn, true);
    zend_result result = call_user_function(NULL, &self->object, &zfn, &retval, argc, argv);
    ON_SCOPE_EXIT {
        zval_ptr_dtor(&zfn);
        release_argv(argc, argv);
    };

    if (result == FAILURE) {
        PyErr_Format(PyExc_NameError, "Function '%s' call failed", Z_STRVAL(zfn));
        Py_INCREF(Py_None);
        return Py_None;
    }

    RETURN_PYOBJ(&retval);
}

static PyObject *Object_get(ZendObject *self, PyObject *args) {
    char *name;
    size_t l_name;
    if (!PyArg_ParseTuple(args, "s#", &name, &l_name)) {
        return NULL;
    }
    zval rv;
    return php2py(zend_read_property(Z_OBJCE(self->object), Z_OBJ(self->object), name, l_name, 0, &rv));
}

static PyObject *Object_set(ZendObject *self, PyObject *args) {
    char *name;
    size_t l_name;
    PyObject *value;
    if (!PyArg_ParseTuple(args, "s#O", &name, &l_name, &value)) {
        return NULL;
    }

    zval rv;
    py2php(value, &rv);
    zend_update_property(Z_OBJCE(self->object), Z_OBJ(self->object), name, l_name, &rv);

    Py_INCREF(Py_None);
    return Py_None;
}

bool ZendObject_Check(PyObject *pv) {
    return Py_IS_TYPE(pv, &ZendObjectType);
}

zval *zend_object_cast(PyObject *pv) {
    ZendObject *obj = (ZendObject *) pv;
    return &obj->object;
}

PyObject *object2py(zval *zv) {
    if (instanceof_function(Z_OBJCE_P(zv), phpy_object_get_ce())) {
        PyObject *obj = phpy_object_get_handle(zv);
        Py_INCREF(obj);
        return obj;
    } else {
        ZendObject *obj = PyObject_New(ZendObject, &ZendObjectType);
        obj->object = *zv;
        zval_add_ref(&obj->object);
        return (PyObject *) obj;
    }
}

const char *object2str(PyObject *pv, ssize_t *len) {
    return PyUnicode_AsUTF8AndSize(pv, len);
}

PyObject *object_create(zend_class_entry *ce, PyObject *args, uint32_t argc, int begin) {
    ZendObject *obj = PyObject_New(ZendObject, &ZendObjectType);
    return object_create((PyObject *) obj, ce, args, argc, begin);
}

PyObject *object_create(PyObject *pv, zend_class_entry *ce, PyObject *args, uint32_t argc, int begin) {
    ZendObject *obj = (ZendObject *) pv;
    if (object_init_ex(&obj->object, ce) == FAILURE) {
        PyErr_SetString(PyExc_TypeError, "failed to init object");
        return NULL;
    }
    if (ce->constructor) {
        zval retval;
        zval zfn;
        ZVAL_STRINGL(&zfn, CTOR_NAME, sizeof(CTOR_NAME) - 1);
        zval argv[argc];
        tuple2argv(argv, args, argc, begin);
        zend_result result = call_user_function(NULL, &obj->object, &zfn, &retval, argc, argv);
        ON_SCOPE_EXIT {
            zval_ptr_dtor(&zfn);
            zval_ptr_dtor(&retval);
            release_argv(argc, argv);
        };
        if (result == FAILURE) {
            return NULL;
        }
    }
    return (PyObject *) obj;
}

bool py_module_object_init(PyObject *m) {
    if (PyType_Ready(&ZendObjectType) < 0) {
        return false;
    }
    Py_INCREF(&ZendObjectType);
    if (PyModule_AddObject(m, "Object", (PyObject *) &ZendObjectType) < 0) {
        Py_DECREF(&ZendObjectType);
        Py_DECREF(m);
        return false;
    }
    return true;
}
