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

static PyObject *phpy_call(PyObject *self, PyObject *args) {
    Py_ssize_t TupleSize = PyTuple_Size(args);
    if (!TupleSize) {
        if (!PyErr_Occurred()) {
            PyErr_SetString(PyExc_TypeError, "must supply at least 1 parameter.");
        }
        return NULL;
    }

    PyObject *fn = PyTuple_GetItem(args, 0);
    if (!PyUnicode_Check(fn)) {
        PyErr_SetString(PyExc_TypeError, "function name must be string");
        return NULL;
    }

    uint32_t argc = TupleSize - 1;
    zval *argv = new zval[argc];

    phpy::python::tuple2argv(argv, args, TupleSize);

    zval retval;
    zval zfn;
    py2php_scalar(fn, &zfn);
    ON_SCOPE_EXIT {
        zval_ptr_dtor(&zfn);
        phpy::python::release_argv(argc, argv);
        delete[] argv;
    };
    zend_result result = phpy::php::call_fn(NULL, &zfn, &retval, argc, argv);

    if (result == FAILURE) {
        PyErr_Format(PyExc_NameError, "Function '%s' call failed", Z_STRVAL(zfn));
        return NULL;
    }
    RETURN_PYOBJ(&retval);
}

static PyObject *phpy_constant(PyObject *self, PyObject *args) {
    const char *name = 0;
    size_t l_name;
    if (!PyArg_ParseTuple(args, "s#", &name, &l_name)) {
        return NULL;
    }

    zend_string *_name = zend_string_init(name, l_name, 0);
    zval *val = zend_get_constant_ex(_name, NULL, ZEND_FETCH_CLASS_SILENT);
    zend_string_free(_name);
    if (val == NULL) {
        Py_INCREF(Py_None);
        return Py_None;
    }
    return php2py(val);
}

static PyObject *phpy_scalar(PyObject *self, PyObject *args) {
    PyObject *pv;
    if (!PyArg_ParseTuple(args, "O", &pv)) {
        return NULL;
    }
    return py2py_scalar(pv);
}

static PyObject *phpy_include(PyObject *self, PyObject *args) {
    const char *file;
    size_t l_file;
    if (!PyArg_ParseTuple(args, "s#", &file, &l_file)) {
        PyErr_SetString(PyExc_TypeError, "must supply at least 1 parameter.");
        return NULL;
    }
    zend_file_handle file_handle;
#if PHP_VERSION_ID >= 80100
    zend_stream_init_filename(&file_handle, file);
    int ret = php_stream_open_for_zend_ex(&file_handle, USE_PATH | STREAM_OPEN_FOR_INCLUDE);
#else
    int ret = php_stream_open_for_zend_ex(file, &file_handle, USE_PATH | STREAM_OPEN_FOR_INCLUDE);
#endif
    if (ret != SUCCESS) {
        return Py_False;
    }

    zend_string *opened_path;
    if (!file_handle.opened_path) {
        file_handle.opened_path = zend_string_init(file, l_file, 0);
    }
    opened_path = zend_string_copy(file_handle.opened_path);
    zval dummy;
    zend_op_array *new_op_array;
    ZVAL_NULL(&dummy);
    if (zend_hash_add(&EG(included_files), opened_path, &dummy)) {
        new_op_array = zend_compile_file(&file_handle, ZEND_REQUIRE);
    } else {
        new_op_array = NULL;
    }
    zend_destroy_file_handle(&file_handle);
    zend_string_release(opened_path);
    if (!new_op_array) {
        return Py_False;
    }

    zval retval;
    zend_execute(new_op_array, &retval);

    destroy_op_array(new_op_array);
    efree(new_op_array);
    return php2py(&retval);
}

static PyObject *phpy_globals(PyObject *self, PyObject *args) {
    const char *name = 0;
    size_t l_name;
    if (!PyArg_ParseTuple(args, "s#", &name, &l_name)) {
        PyErr_SetString(PyExc_TypeError, "must supply at least 1 parameter.");
        return NULL;
    }
    zend_string *key = zend_string_init(name, l_name, 0);
    zend_is_auto_global(key);
    zval *var = zend_hash_find_ind(&EG(symbol_table), key);
    zend_string_free(key);
    if (!var) {
        Py_INCREF(Py_None);
        return Py_None;
    }
    return php2py_object(var);
}

static PyObject *phpy_eval(PyObject *self, PyObject *args) {
    const char *script = 0;
    size_t l_script;
    int exit_status;
    char program_name[] = "phpy";
    if (!PyArg_ParseTuple(args, "s#", &script, &l_script)) {
        PyErr_SetString(PyExc_TypeError, "must supply at least 1 parameter.");
        return NULL;
    }
    zend_first_try {
        zend_eval_stringl((char *) script, l_script, NULL, program_name);
    }
    zend_catch {
        exit_status = EG(exit_status);
    }
    zend_end_try();

    return PyLong_FromLong(exit_status);
}

static PyObject *phpy_setOptions(PyObject *self, PyObject *args) {
    PyObject *options;
    if (!PyArg_ParseTuple(args, "O!", &PyDict_Type, &options)) {
        PyErr_SetString(PyExc_TypeError, "must supply at least 1 parameter.");
        return NULL;
    }

    PyObject *opt;
    if ((opt = PyDict_GetItemString(options, "numeric_as_object"))) {
        phpy_options.numeric_as_object = Py_IsTrue(opt);
        Py_DECREF(opt);
    }
    if ((opt = PyDict_GetItemString(options, "argument_as_object"))) {
        phpy_options.argument_as_object = Py_IsTrue(opt);
        Py_DECREF(opt);
    }
    if ((opt = PyDict_GetItemString(options, "display_exception"))) {
        phpy_options.display_exception = Py_IsTrue(opt);
        Py_DECREF(opt);
    }
    Py_RETURN_NONE;
}

// clang-format off

static PyMethodDef phpy_methods[] = {
    {"call", (PyCFunction) phpy_call, METH_VARARGS, "call function"},
    {"constant", (PyCFunction) phpy_constant, METH_VARARGS, "get constant"},
    {"include", (PyCFunction) phpy_include, METH_VARARGS, "include a php file"},
    {"globals", (PyCFunction) phpy_globals, METH_VARARGS, "get global variable"},
    {"eval", (PyCFunction) phpy_eval, METH_VARARGS, "execute php code"},
    {"scalar", (PyCFunction) phpy_scalar, METH_VARARGS, "convert object to php scalar type"},
    {"setOptions", (PyCFunction) phpy_setOptions, METH_VARARGS, "set options"},
    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef php_module = {
    PyModuleDef_HEAD_INIT,
    "phpy", "Embedding PHP into Python",
    -1,
    phpy_methods
};
// clang-format on

#ifdef HAVE_PHP_EMBED
/**
 * Load as a python module and inject the class into ZendVM
 */
static bool py_module_php_init(PyObject *m) {
    zend_string *lcname = zend_string_init("core", strlen("core"), 0);
    zend_module_entry *module = (zend_module_entry *) zend_hash_find_ptr(&module_registry, lcname);
    zend_string_efree(lcname);

    EG(current_module) = module;
    php_class_init_all(module->type, module->module_number);

    return true;
}

#include <sapi/embed/php_embed.h>
PyMODINIT_FUNC PyInit_phpy(void) {
    if (phpy_init(PHPY_PYTHON_MODULE) < 0) {
        PyErr_SetString(PyExc_SystemError, "Error: phpy has been initialized");
        return NULL;
    }
    char program_name[] = "phpy";
    char *argv[] = {program_name};
    php_embed_init(1, argv);
    return py_module_create(true);
}

#endif

PyObject *py_module_create(bool py_module) {
    auto m = PyModule_Create(&php_module);
    auto modules = {
        py_module_string_init,
        py_module_array_init,
        py_module_object_init,
        py_module_reference_init,
        py_module_class_init,
        py_module_resource_init,
        py_module_callable_init,
#ifdef HAVE_PHP_EMBED
        py_module_php_init,
#endif
    };
    for (auto fn : modules) {
        if (!fn(m)) {
            return NULL;
        }
    }
    return m;
}
