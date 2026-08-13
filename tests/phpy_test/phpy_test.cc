#ifdef HAVE_CONFIG_H
#include "config.h"
#endif

#include "php.h"
#include "phpy.h"
#include "phpy_api.h"

static const phpy_native_api_v1 *native_api() {
    const phpy_native_api_v1 *api = phpy_get_native_api(PHPY_NATIVE_ABI_VERSION);
    if (api == nullptr || api->struct_size < sizeof(phpy_native_api_v1)) {
        zend_throw_error(nullptr, "The phpy native bridge ABI is unavailable");
        return nullptr;
    }
    return api;
}

PHP_FUNCTION(phpy_test_native_call_member) {
    zval *object;
    zend_string *name;
    zval *arguments = nullptr;
    int argument_count = 0;
    zend_array *named_arguments = nullptr;

    ZEND_PARSE_PARAMETERS_START(2, -1)
    Z_PARAM_OBJECT(object)
    Z_PARAM_STR(name)
    Z_PARAM_OPTIONAL
    Z_PARAM_VARIADIC_WITH_NAMED(arguments, argument_count, named_arguments)
    ZEND_PARSE_PARAMETERS_END();

    const phpy_native_api_v1 *api = native_api();
    if (api == nullptr) {
        RETURN_THROWS();
    }
    api->call_member(object,
                     ZSTR_VAL(name),
                     ZSTR_LEN(name),
                     static_cast<uint32_t>(argument_count),
                     arguments,
                     named_arguments,
                     return_value);
}

PHP_FUNCTION(phpy_test_native_call) {
    zval *object;
    zval *arguments = nullptr;
    int argument_count = 0;
    zend_array *named_arguments = nullptr;

    ZEND_PARSE_PARAMETERS_START(1, -1)
    Z_PARAM_OBJECT(object)
    Z_PARAM_OPTIONAL
    Z_PARAM_VARIADIC_WITH_NAMED(arguments, argument_count, named_arguments)
    ZEND_PARSE_PARAMETERS_END();

    const phpy_native_api_v1 *api = native_api();
    if (api == nullptr) {
        RETURN_THROWS();
    }
    api->call(object,
              static_cast<uint32_t>(argument_count),
              arguments,
              named_arguments,
              return_value);
}

PHP_FUNCTION(phpy_test_bridge_mode) {
    ZEND_PARSE_PARAMETERS_NONE();
    RETURN_LONG(phpy_get_mode());
}

PHP_FUNCTION(phpy_test_bridge_number_to_long) {
    zval *value;
    ZEND_PARSE_PARAMETERS_START(1, 1)
    Z_PARAM_ZVAL(value)
    ZEND_PARSE_PARAMETERS_END();

    LOCK_GIL();
    phpy::python::OwnedPythonReference converted(php_number_to_python_long(value));
    if (!converted) {
        phpy::php::throw_error_if_occurred();
        RETURN_THROWS();
    }
    py2php_scalar(converted.get(), return_value);
}

PHP_FUNCTION(phpy_test_bridge_env_equals) {
    zend_string *name;
    zend_string *value;
    ZEND_PARSE_PARAMETERS_START(2, 2)
    Z_PARAM_STR(name)
    Z_PARAM_STR(value)
    ZEND_PARSE_PARAMETERS_END();

    RETURN_BOOL(phpy::php::env_equals(
        ZSTR_VAL(name), ZSTR_LEN(name), ZSTR_VAL(value), ZSTR_LEN(value)));
}

PHP_FUNCTION(phpy_test_bridge_dump_helpers) {
    zval *value;
    ZEND_PARSE_PARAMETERS_START(1, 1)
    Z_PARAM_ZVAL(value)
    ZEND_PARSE_PARAMETERS_END();

    LOCK_GIL();
    phpy::python::OwnedPythonReference python_value(php2py(value));
    if (!python_value) {
        phpy::php::throw_error_if_occurred();
        RETURN_THROWS();
    }

    debug_dump(0, value);
    debug_dump(1, python_value.get());
    var_dump(value);
    debug_var_dump(value);
    debug_print_refcnt("phpy-test", python_value.get());
}

ZEND_BEGIN_ARG_WITH_RETURN_TYPE_INFO_EX(arginfo_phpy_test_native_call_member, 0, 2, IS_MIXED, 0)
ZEND_ARG_TYPE_INFO(0, object, IS_OBJECT, 0)
ZEND_ARG_TYPE_INFO(0, name, IS_STRING, 0)
ZEND_ARG_VARIADIC_TYPE_INFO(0, arguments, IS_MIXED, 0)
ZEND_END_ARG_INFO()

ZEND_BEGIN_ARG_WITH_RETURN_TYPE_INFO_EX(arginfo_phpy_test_native_call, 0, 1, IS_MIXED, 0)
ZEND_ARG_TYPE_INFO(0, object, IS_OBJECT, 0)
ZEND_ARG_VARIADIC_TYPE_INFO(0, arguments, IS_MIXED, 0)
ZEND_END_ARG_INFO()

ZEND_BEGIN_ARG_WITH_RETURN_TYPE_INFO_EX(arginfo_phpy_test_bridge_mode, 0, 0, IS_LONG, 0)
ZEND_END_ARG_INFO()

ZEND_BEGIN_ARG_WITH_RETURN_TYPE_INFO_EX(arginfo_phpy_test_bridge_number_to_long, 0, 1, IS_MIXED, 0)
ZEND_ARG_TYPE_INFO(0, value, IS_MIXED, 0)
ZEND_END_ARG_INFO()

ZEND_BEGIN_ARG_WITH_RETURN_TYPE_INFO_EX(arginfo_phpy_test_bridge_env_equals, 0, 2, _IS_BOOL, 0)
ZEND_ARG_TYPE_INFO(0, name, IS_STRING, 0)
ZEND_ARG_TYPE_INFO(0, value, IS_STRING, 0)
ZEND_END_ARG_INFO()

ZEND_BEGIN_ARG_WITH_RETURN_TYPE_INFO_EX(arginfo_phpy_test_bridge_dump_helpers, 0, 1, IS_VOID, 0)
ZEND_ARG_TYPE_INFO(0, value, IS_MIXED, 0)
ZEND_END_ARG_INFO()

static const zend_function_entry phpy_test_functions[] = {
    PHP_FE(phpy_test_native_call_member, arginfo_phpy_test_native_call_member)
    PHP_FE(phpy_test_native_call, arginfo_phpy_test_native_call)
    PHP_FE(phpy_test_bridge_mode, arginfo_phpy_test_bridge_mode)
    PHP_FE(phpy_test_bridge_number_to_long, arginfo_phpy_test_bridge_number_to_long)
    PHP_FE(phpy_test_bridge_env_equals, arginfo_phpy_test_bridge_env_equals)
    PHP_FE(phpy_test_bridge_dump_helpers, arginfo_phpy_test_bridge_dump_helpers)
    PHP_FE_END
};

zend_module_entry phpy_test_module_entry = {
    STANDARD_MODULE_HEADER,
    "phpy_test",
    phpy_test_functions,
    nullptr,
    nullptr,
    nullptr,
    nullptr,
    nullptr,
    "1.0.0",
    STANDARD_MODULE_PROPERTIES
};

extern "C" {
ZEND_GET_MODULE(phpy_test)
}
