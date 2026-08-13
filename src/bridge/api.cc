#include "phpy.h"

#include <exception>

using phpy::CallObject;
using phpy::php::new_dict;
using phpy::php::new_list;
using phpy::php::new_module;
using phpy::php::new_object_no_addref;
using phpy::php::new_set;
using phpy::php::new_str;
using phpy::php::new_tuple;
using phpy::php::throw_error_if_occurred;
using phpy::python::LockGuard;
using phpy::python::OwnedPythonReference;

namespace {

zend_result fail_if_exception() {
    return EG(exception) == nullptr ? SUCCESS : FAILURE;
}

template <typename Function>
zend_result guard_native_call(zval *result, Function &&function) noexcept {
    ZVAL_NULL(result);
    try {
        function();
        return fail_if_exception();
    } catch (const std::exception &error) {
        zend_throw_error(nullptr, "phpy native bridge failed: %s", error.what());
    } catch (...) {
        zend_throw_error(nullptr, "phpy native bridge failed with an unknown C++ exception");
    }
    return FAILURE;
}

PyObject *checked_object(const zval *object) {
	ZVAL_DEINDIRECT(object);
    if (UNEXPECTED(object == nullptr || !phpy::php::is_pyobject(const_cast<zval *>(object)))) {
        zend_type_error("phpy native bridge expects a PyObject");
        return nullptr;
    }
    PyObject *handle = phpy_object_get_handle(const_cast<zval *>(object));
    if (UNEXPECTED(handle == nullptr)) {
        zend_throw_error(nullptr, "PyObject is not initialized");
    }
    return handle;
}

OwnedPythonReference get_attribute(PyObject *object, const char *name, size_t name_length) {
    OwnedPythonReference attribute_name(PyUnicode_FromStringAndSize(name, name_length));
    if (!attribute_name) {
        return OwnedPythonReference(nullptr);
    }
    return OwnedPythonReference(PyObject_GetAttr(object, attribute_name.get()));
}

}  // namespace


PHPY_API const char *phpy_get_python_version(void) {
    LOCK_GIL();
    return Py_GetVersion();
}

PHPY_API zend_result phpy_configure_runtime(zend_bool return_as_object) {
    phpy_options.return_as_object = return_as_object;
    return SUCCESS;
}

PHPY_API zend_result phpy_import_module(const char *name, size_t name_length, zval *result) {
    return guard_native_call(result, [&] {
        LOCK_GIL();
        const std::string module_name(name, name_length);
        OwnedPythonReference module(PyImport_ImportModule(module_name.c_str()));
        if (UNEXPECTED(!module)) {
            throw_error_if_occurred();
            return;
        }
        new_module(result, module.get());
    });
}

PHPY_API zend_result phpy_call_member(const zval *object,
                                      const char *name,
                                      size_t name_length,
                                      uint32_t argc,
                                      zval *argv,
                                      zend_array *named_args,
                                      zval *result) {
    return guard_native_call(result, [&] {
        PyObject *handle = checked_object(object);
        if (UNEXPECTED(handle == nullptr)) {
            return;
        }
        LOCK_GIL();
        OwnedPythonReference callable(get_attribute(handle, name, name_length));
        if (UNEXPECTED(!callable)) {
            throw_error_if_occurred();
            return;
        }
        if (UNEXPECTED(!PyCallable_Check(callable.get()))) {
            PyErr_Format(PyExc_TypeError, "'%.200s' object is not callable", Py_TypeName(callable.get()));
            throw_error_if_occurred();
            return;
        }
        CallObject caller(callable.get(), result, argc, argv, named_args);
        caller.call();
    });
}

PHPY_API zend_result phpy_call(const zval *object, uint32_t argc, zval *argv, zend_array *named_args, zval *result) {
    return guard_native_call(result, [&] {
        PyObject *handle = checked_object(object);
        if (UNEXPECTED(handle == nullptr)) {
            return;
        }
        LOCK_GIL();
        if (UNEXPECTED(!PyCallable_Check(handle))) {
            PyErr_Format(PyExc_TypeError, "'%.200s' object is not callable", Py_TypeName(handle));
            throw_error_if_occurred();
            return;
        }
        CallObject caller(handle, result, argc, argv, named_args);
        caller.call();
    });
}

PHPY_API zend_result phpy_get_attr(const zval *object, const char *name, size_t name_length, zval *result) {
    return guard_native_call(result, [&] {
        PyObject *handle = checked_object(object);
        if (UNEXPECTED(handle == nullptr)) {
            return;
        }
        LOCK_GIL();
        OwnedPythonReference value(get_attribute(handle, name, name_length));
        if (UNEXPECTED(!value)) {
            throw_error_if_occurred();
            return;
        }
        py2php(value.get(), result);
    });
}

PHPY_API zend_result phpy_to_value(const zval *object, zval *result) {
    return guard_native_call(result, [&] {
        PyObject *handle = checked_object(object);
        if (UNEXPECTED(handle == nullptr)) {
            return;
        }
        LOCK_GIL();
        py2php_scalar(handle, result);
    });
}

PHPY_API zend_result phpy_to_array(const zval *object, zval *result) {
    return guard_native_call(result, [&] {
        PyObject *handle = checked_object(object);
        if (UNEXPECTED(handle == nullptr)) {
            return;
        }
        LOCK_GIL();
        py2php_array(handle, result);
    });
}

PHPY_API zend_result phpy_construct(phpy_native_constructor constructor,
                                    const zval *argument,
                                    zend_bool has_argument,
                                    zval *result) {
    return guard_native_call(result, [&] {
        LOCK_GIL();
        ZVAL_DEINDIRECT(argument);
        const bool null_argument = !has_argument || argument == nullptr || Z_TYPE_P(argument) == IS_NULL;
        PyObject *value = nullptr;

        switch (constructor) {
        case PHPY_NATIVE_CONSTRUCT_LIST:
            if (null_argument || phpy::php::is_empty_array(const_cast<zval *>(argument))) {
                value = PyList_New(0);
            } else if (phpy::php::is_array(const_cast<zval *>(argument))) {
                value = array2list(const_cast<zval *>(argument));
            } else {
                zend_throw_error(nullptr, "PyList: unsupported type");
            }
            if (value != nullptr) {
                new_list(result, value);
                Py_DECREF(value);
            }
            break;
        case PHPY_NATIVE_CONSTRUCT_DICT:
            if (null_argument || phpy::php::is_empty_array(const_cast<zval *>(argument))) {
                value = PyDict_New();
            } else if (phpy::php::is_array(const_cast<zval *>(argument))) {
                value = array2dict(const_cast<zval *>(argument));
            } else {
                zend_throw_error(nullptr, "PyDict: unsupported type");
            }
            if (value != nullptr) {
                new_dict(result, value);
                Py_DECREF(value);
            }
            break;
        case PHPY_NATIVE_CONSTRUCT_TUPLE:
            if (!has_argument) {
                zend_argument_count_error("PyTuple::__construct() expects exactly 1 argument, 0 given");
            } else if (null_argument || phpy::php::is_empty_array(const_cast<zval *>(argument))) {
                value = PyTuple_New(0);
            } else if (phpy::php::is_array(const_cast<zval *>(argument))) {
                value = array2tuple(const_cast<zval *>(argument));
            } else if (phpy::php::is_pyobject(const_cast<zval *>(argument))) {
                value = PySequence_Tuple(phpy_object_get_handle(const_cast<zval *>(argument)));
            } else {
                zend_throw_error(nullptr, "PyTuple: unsupported type");
            }
            if (value != nullptr) {
                new_tuple(result, value);
                Py_DECREF(value);
            }
            break;
        case PHPY_NATIVE_CONSTRUCT_SET:
            if (null_argument || phpy::php::is_empty_array(const_cast<zval *>(argument))) {
                value = PySet_New(nullptr);
            } else if (phpy::php::is_array(const_cast<zval *>(argument))) {
                value = array2set(const_cast<zval *>(argument));
            } else {
                zend_throw_error(nullptr, "PySet: unsupported type");
            }
            if (value != nullptr) {
                new_set(result, value);
                Py_DECREF(value);
            }
            break;
        case PHPY_NATIVE_CONSTRUCT_STR:
            if (has_argument && argument != nullptr && phpy::php::is_pyobject(const_cast<zval *>(argument))) {
                value = PyUnicode_FromObject(phpy_object_get_handle(const_cast<zval *>(argument)));
            } else if (has_argument && argument != nullptr) {
                zend_string *string = zval_get_string(const_cast<zval *>(argument));
                if (UNEXPECTED(EG(exception) != nullptr)) {
                    zend_string_release(string);
                    return;
                }
                value = PyUnicode_FromStringAndSize(ZSTR_VAL(string), ZSTR_LEN(string));
                zend_string_release(string);
            } else {
                zend_argument_count_error("PyStr::__construct() expects exactly 1 argument, 0 given");
            }
            if (value != nullptr) {
                new_str(result, value);
                Py_DECREF(value);
            }
            break;
        case PHPY_NATIVE_CONSTRUCT_OBJECT:
            if (!has_argument) {
                value = Py_None;
                Py_INCREF(value);
            } else {
                value = php2py_object(const_cast<zval *>(argument));
            }
            if (value != nullptr) {
                new_object_no_addref(result, value);
            }
            break;
        case PHPY_NATIVE_CONSTRUCT_INT: {
            OwnedPythonReference converted(has_argument ? php2py(const_cast<zval *>(argument)) : nullptr);
            value = has_argument ? (converted ? PyNumber_Long(converted.get()) : nullptr) : PyLong_FromLong(0);
            if (value != nullptr) {
                new_object_no_addref(result, value);
            }
            break;
        }
        case PHPY_NATIVE_CONSTRUCT_FLOAT: {
            OwnedPythonReference converted(has_argument ? php2py(const_cast<zval *>(argument)) : nullptr);
            value = has_argument ? (converted ? PyNumber_Float(converted.get()) : nullptr) : PyFloat_FromDouble(0.0);
            if (value != nullptr) {
                new_object_no_addref(result, value);
            }
            break;
        }
        case PHPY_NATIVE_CONSTRUCT_BYTES:
            if (null_argument) {
                value = PyBytes_FromStringAndSize("", 0);
            } else if (phpy::php::is_string(const_cast<zval *>(argument))) {
                value = PyBytes_FromStringAndSize(Z_STRVAL_P(argument), Z_STRLEN_P(argument));
            } else if (phpy::php::is_pyobject(const_cast<zval *>(argument))) {
                value = PyBytes_FromObject(phpy_object_get_handle(const_cast<zval *>(argument)));
            } else {
                zend_string *string = zval_get_string(const_cast<zval *>(argument));
                if (UNEXPECTED(EG(exception) != nullptr)) {
                    zend_string_release(string);
                    return;
                }
                value = PyBytes_FromStringAndSize(ZSTR_VAL(string), ZSTR_LEN(string));
                zend_string_release(string);
            }
            if (value != nullptr) {
                new_object_no_addref(result, value);
            }
            break;
        default:
            zend_value_error("Unknown phpy native constructor");
            break;
        }

        if (UNEXPECTED(value == nullptr) && EG(exception) == nullptr) {
            throw_error_if_occurred();
        }
    });
}

namespace {

const phpy_native_api_v1 native_api = {
    PHPY_NATIVE_ABI_VERSION,
    sizeof(phpy_native_api_v1),
    phpy_configure_runtime,
    phpy_import_module,
    phpy_call_member,
    phpy_get_attr,
    phpy_to_value,
    phpy_to_array,
    phpy_construct,
    phpy_call,
};

}  // namespace

PHPY_API const phpy_native_api_v1 *phpy_get_native_api(uint32_t requested_abi) {
    return requested_abi == PHPY_NATIVE_ABI_VERSION ? &native_api : nullptr;
}
