#include "phpy_api.h"

static const char *(*get_python_version_fn)(void) = phpy_get_python_version;
static zend_result (*configure_runtime_fn)(zend_bool) = phpy_configure_runtime;
static zend_result (*import_module_fn)(const char *, size_t, zval *) = phpy_import_module;
static zend_result (*call_member_fn)(const zval *,
                                     const char *,
                                     size_t,
                                     uint32_t,
                                     zval *,
                                     zend_array *,
                                     zval *) = phpy_call_member;
static zend_result (*get_attr_fn)(const zval *, const char *, size_t, zval *) = phpy_get_attr;
static zend_result (*to_value_fn)(const zval *, zval *) = phpy_to_value;
static zend_result (*to_array_fn)(const zval *, zval *) = phpy_to_array;
static zend_result (*construct_fn)(phpy_native_constructor, const zval *, zend_bool, zval *) = phpy_construct;
static zend_result (*call_fn)(const zval *, uint32_t, zval *, zend_array *, zval *) = phpy_call;
static const phpy_native_api_v1 *(*get_native_api_fn)(uint32_t) = phpy_get_native_api;

int main(void) {
    return get_python_version_fn == NULL || configure_runtime_fn == NULL || import_module_fn == NULL
        || call_member_fn == NULL
        || get_attr_fn == NULL || to_value_fn == NULL || to_array_fn == NULL || construct_fn == NULL
        || call_fn == NULL || get_native_api_fn == NULL;
}
