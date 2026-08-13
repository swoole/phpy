#pragma once

#include <stddef.h>
#include <stdint.h>

#include <main/php.h>

/* Public symbol visibility for phpy's C ABI. */
#ifndef PHPY_API
#ifdef PHP_WIN32
#ifdef PHPY_EXPORTS
#define PHPY_API ZEND_DLEXPORT
#else
#define PHPY_API ZEND_DLIMPORT
#endif
#elif defined(__GNUC__) && __GNUC__ >= 4
#define PHPY_API __attribute__((visibility("default")))
#else
#define PHPY_API
#endif
#endif

/*
 * Stable C ABI used by native TypePHP callers. Keep this header independent
 * of Python and C++ so consumers neither link libpython nor depend on phpy's
 * implementation classes.
 */
#define PHPY_NATIVE_ABI_VERSION 1u

typedef enum phpy_native_constructor {
    PHPY_NATIVE_CONSTRUCT_LIST = 0,
    PHPY_NATIVE_CONSTRUCT_DICT,
    PHPY_NATIVE_CONSTRUCT_TUPLE,
    PHPY_NATIVE_CONSTRUCT_SET,
    PHPY_NATIVE_CONSTRUCT_STR,
    PHPY_NATIVE_CONSTRUCT_OBJECT,
    PHPY_NATIVE_CONSTRUCT_INT,
    PHPY_NATIVE_CONSTRUCT_FLOAT,
    PHPY_NATIVE_CONSTRUCT_BYTES,
} phpy_native_constructor;

typedef struct phpy_native_api_v1 {
    uint32_t abi_version;
    size_t struct_size;

    zend_result (*configure_runtime)(zend_bool return_as_object);
    zend_result (*import_module)(const char *name, size_t name_length, zval *result);
    zend_result (*call_member)(const zval *object,
                               const char *name,
                               size_t name_length,
                               uint32_t argc,
                               zval *argv,
                               zend_array *named_args,
                               zval *result);
    zend_result (*get_attr)(const zval *object, const char *name, size_t name_length, zval *result);
    zend_result (*to_value)(const zval *object, zval *result);
    zend_result (*to_array)(const zval *object, zval *result);
    zend_result (*construct)(phpy_native_constructor constructor,
                             const zval *argument,
                             zend_bool has_argument,
                             zval *result);
    zend_result (*call)(const zval *object, uint32_t argc, zval *argv, zend_array *named_args, zval *result);
} phpy_native_api_v1;

BEGIN_EXTERN_C()
PHPY_API const char *phpy_get_python_version(void);
PHPY_API zend_result phpy_configure_runtime(zend_bool return_as_object);
PHPY_API zend_result phpy_import_module(const char *name, size_t name_length, zval *result);
PHPY_API zend_result phpy_call_member(const zval *object,
                                      const char *name,
                                      size_t name_length,
                                      uint32_t argc,
                                      zval *argv,
                                      zend_array *named_args,
                                      zval *result);
PHPY_API zend_result phpy_get_attr(const zval *object, const char *name, size_t name_length, zval *result);
PHPY_API zend_result phpy_to_value(const zval *object, zval *result);
PHPY_API zend_result phpy_to_array(const zval *object, zval *result);
PHPY_API zend_result phpy_construct(phpy_native_constructor constructor,
                                    const zval *argument,
                                    zend_bool has_argument,
                                    zval *result);
PHPY_API zend_result phpy_call(const zval *object, uint32_t argc, zval *argv, zend_array *named_args, zval *result);
PHPY_API const phpy_native_api_v1 *phpy_get_native_api(uint32_t requested_abi);
END_EXTERN_C()
