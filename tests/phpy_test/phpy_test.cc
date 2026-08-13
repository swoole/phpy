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

PHP_FUNCTION(phpy_test_native_configure_runtime) {
    bool return_as_object;

    ZEND_PARSE_PARAMETERS_START(1, 1)
    Z_PARAM_BOOL(return_as_object)
    ZEND_PARSE_PARAMETERS_END();

    const phpy_native_api_v1 *api = native_api();
    if (api == nullptr) {
        RETURN_THROWS();
    }
    RETURN_BOOL(api->configure_runtime(return_as_object) == SUCCESS);
}

PHP_FUNCTION(phpy_test_native_construct) {
    zend_long constructor;
    zval *argument = nullptr;

    ZEND_PARSE_PARAMETERS_START(1, 2)
    Z_PARAM_LONG(constructor)
    Z_PARAM_OPTIONAL
    Z_PARAM_ZVAL(argument)
    ZEND_PARSE_PARAMETERS_END();

    const phpy_native_api_v1 *api = native_api();
    if (api == nullptr) {
        RETURN_THROWS();
    }
    api->construct(static_cast<phpy_native_constructor>(constructor),
                   argument,
                   argument != nullptr,
                   return_value);
}

PHP_FUNCTION(phpy_test_native_indirect_inputs) {
    zval *member_object;
    zval *callable;
    zval *scalar;
    zval *list;

    ZEND_PARSE_PARAMETERS_START(4, 4)
    Z_PARAM_OBJECT(member_object)
    Z_PARAM_OBJECT(callable)
    Z_PARAM_OBJECT(scalar)
    Z_PARAM_OBJECT(list)
    ZEND_PARSE_PARAMETERS_END();

    const phpy_native_api_v1 *api = native_api();
    if (api == nullptr) {
        RETURN_THROWS();
    }

    zval indirect_member_object;
    zval indirect_callable;
    zval indirect_scalar;
    zval indirect_list;
    ZVAL_INDIRECT(&indirect_member_object, member_object);
    ZVAL_INDIRECT(&indirect_callable, callable);
    ZVAL_INDIRECT(&indirect_scalar, scalar);
    ZVAL_INDIRECT(&indirect_list, list);

    zval prefix;
    zval suffix;
    ZVAL_STRING(&prefix, "hello");
    ZVAL_STRING(&suffix, "?");
    zend_array *named_args = zend_new_array(1);
    Z_TRY_ADDREF(suffix);
    zend_hash_str_add_new(named_args, ZEND_STRL("suffix"), &suffix);

    zval member_result;
    ZVAL_UNDEF(&member_result);
    api->call_member(&indirect_member_object,
                     ZEND_STRL("greet"),
                     1,
                     &prefix,
                     named_args,
                     &member_result);
    zend_array_release(named_args);
    zval_ptr_dtor(&prefix);
    zval_ptr_dtor(&suffix);
    if (UNEXPECTED(EG(exception) != nullptr)) {
        zval_ptr_dtor(&member_result);
        RETURN_THROWS();
    }

    zval call_args[2];
    ZVAL_LONG(&call_args[0], 3);
    ZVAL_LONG(&call_args[1], 4);
    zval call_result;
    ZVAL_UNDEF(&call_result);
    api->call(&indirect_callable, 2, call_args, nullptr, &call_result);
    if (UNEXPECTED(EG(exception) != nullptr)) {
        zval_ptr_dtor(&member_result);
        zval_ptr_dtor(&call_result);
        RETURN_THROWS();
    }

    zval source;
    zval indirect_source;
    array_init(&source);
    add_next_index_long(&source, 1);
    add_next_index_long(&source, 2);
    add_next_index_long(&source, 3);
    ZVAL_INDIRECT(&indirect_source, &source);
    zval construct_result;
    ZVAL_UNDEF(&construct_result);
    api->construct(PHPY_NATIVE_CONSTRUCT_LIST, &indirect_source, true, &construct_result);
    zval_ptr_dtor(&source);
    if (UNEXPECTED(EG(exception) != nullptr)) {
        zval_ptr_dtor(&member_result);
        zval_ptr_dtor(&call_result);
        zval_ptr_dtor(&construct_result);
        RETURN_THROWS();
    }

    zval scalar_result;
    zval list_result;
    ZVAL_UNDEF(&scalar_result);
    ZVAL_UNDEF(&list_result);
    api->to_value(&indirect_scalar, &scalar_result);
    api->to_array(&indirect_list, &list_result);
    if (UNEXPECTED(EG(exception) != nullptr)) {
        zval_ptr_dtor(&member_result);
        zval_ptr_dtor(&call_result);
        zval_ptr_dtor(&construct_result);
        zval_ptr_dtor(&scalar_result);
        zval_ptr_dtor(&list_result);
        RETURN_THROWS();
    }

    array_init(return_value);
    add_assoc_zval(return_value, "member", &member_result);
    add_assoc_zval(return_value, "call", &call_result);
    add_assoc_zval(return_value, "constructed", &construct_result);
    add_assoc_zval(return_value, "scalar", &scalar_result);
    add_assoc_zval(return_value, "list", &list_result);
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

PHP_FUNCTION(phpy_test_new_reference) {
    zval *value;
    ZEND_PARSE_PARAMETERS_START(1, 1)
    Z_PARAM_ZVAL(value)
    ZEND_PARSE_PARAMETERS_END();

    LOCK_GIL();
    PyObject *reference = phpy::python::new_reference(value);
    phpy::php::new_object_no_addref(return_value, reference);
}

PHP_FUNCTION(phpy_test_reference_is_same) {
    zval *object;
    zval *value;
    ZEND_PARSE_PARAMETERS_START(2, 2)
    Z_PARAM_OBJECT_OF_CLASS(object, phpy_object_get_ce())
    Z_PARAM_ZVAL(value)
    ZEND_PARSE_PARAMETERS_END();

    PyObject *handle = phpy_object_get_handle(object);
    if (UNEXPECTED(!ZendReference_Check(handle) || !Z_ISREF_P(value))) {
        RETURN_FALSE;
    }
    RETURN_BOOL(Z_REF_P(zend_reference_cast(handle)) == Z_REF_P(value));
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

ZEND_BEGIN_ARG_WITH_RETURN_TYPE_INFO_EX(arginfo_phpy_test_native_configure_runtime, 0, 1, _IS_BOOL, 0)
ZEND_ARG_TYPE_INFO(0, returnAsObject, _IS_BOOL, 0)
ZEND_END_ARG_INFO()

ZEND_BEGIN_ARG_WITH_RETURN_TYPE_INFO_EX(arginfo_phpy_test_native_construct, 0, 1, IS_OBJECT, 0)
ZEND_ARG_TYPE_INFO(0, constructor, IS_LONG, 0)
ZEND_ARG_TYPE_INFO_WITH_DEFAULT_VALUE(0, argument, IS_MIXED, 0, "null")
ZEND_END_ARG_INFO()

ZEND_BEGIN_ARG_WITH_RETURN_TYPE_INFO_EX(arginfo_phpy_test_native_indirect_inputs, 0, 4, IS_ARRAY, 0)
ZEND_ARG_TYPE_INFO(0, memberObject, IS_OBJECT, 0)
ZEND_ARG_TYPE_INFO(0, callable, IS_OBJECT, 0)
ZEND_ARG_TYPE_INFO(0, scalar, IS_OBJECT, 0)
ZEND_ARG_TYPE_INFO(0, list, IS_OBJECT, 0)
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

ZEND_BEGIN_ARG_WITH_RETURN_OBJ_INFO_EX(arginfo_phpy_test_new_reference, 0, 1, PyObject, 0)
ZEND_ARG_INFO(1, value)
ZEND_END_ARG_INFO()

ZEND_BEGIN_ARG_WITH_RETURN_TYPE_INFO_EX(arginfo_phpy_test_reference_is_same, 0, 2, _IS_BOOL, 0)
ZEND_ARG_OBJ_INFO(0, object, PyObject, 0)
ZEND_ARG_INFO(1, value)
ZEND_END_ARG_INFO()

static const zend_function_entry phpy_test_functions[] = {
    PHP_FE(phpy_test_native_call_member, arginfo_phpy_test_native_call_member)
    PHP_FE(phpy_test_native_call, arginfo_phpy_test_native_call)
    PHP_FE(phpy_test_native_configure_runtime, arginfo_phpy_test_native_configure_runtime)
    PHP_FE(phpy_test_native_construct, arginfo_phpy_test_native_construct)
    PHP_FE(phpy_test_native_indirect_inputs, arginfo_phpy_test_native_indirect_inputs)
    PHP_FE(phpy_test_bridge_mode, arginfo_phpy_test_bridge_mode)
    PHP_FE(phpy_test_bridge_number_to_long, arginfo_phpy_test_bridge_number_to_long)
    PHP_FE(phpy_test_bridge_env_equals, arginfo_phpy_test_bridge_env_equals)
    PHP_FE(phpy_test_bridge_dump_helpers, arginfo_phpy_test_bridge_dump_helpers)
    PHP_FE(phpy_test_new_reference, arginfo_phpy_test_new_reference)
    PHP_FE(phpy_test_reference_is_same, arginfo_phpy_test_reference_is_same)
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
