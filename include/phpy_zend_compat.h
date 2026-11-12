#pragma once

#include <Zend/zend_exceptions.h>
#include <Zend/zend_interfaces.h>

#if PHP_VERSION_ID < 80000
// PHP 7.4 has no mixed or union declarations in internal arginfo.
#define IS_MIXED 0
#define ZEND_ARG_TYPE_INFO_WITH_DEFAULT_VALUE(ref, name, type, nullable, value) \
    ZEND_ARG_TYPE_INFO(ref, name, type, nullable)
#define ZEND_BEGIN_ARG_WITH_RETURN_TYPE_MASK_EX(name, ref, required, mask) \
    ZEND_BEGIN_ARG_INFO_EX(name, 0, ref, required)
#endif

namespace phpy {
namespace zend_compat {

inline zval *read_property(zend_class_entry *ce, zval *object, const char *name, size_t length, bool silent, zval *rv) {
#if PHP_VERSION_ID < 80000
    return zend_read_property(ce, object, name, length, silent, rv);
#else
    return zend_read_property(ce, Z_OBJ_P(object), name, length, silent, rv);
#endif
}

inline zval *read_exception_message(zend_object *exception, zval *rv) {
    zval object;
    ZVAL_OBJ(&object, exception);
    return read_property(exception->ce, &object, ZEND_STRL("message"), true, rv);
}

inline void update_property(zend_class_entry *ce, zval *object, const char *name, size_t length, zval *value) {
#if PHP_VERSION_ID < 80000
    zend_update_property(ce, object, name, length, value);
#else
    zend_update_property(ce, Z_OBJ_P(object), name, length, value);
#endif
}

inline void update_property_stringl(zend_class_entry *ce, zval *object, const char *name, size_t length,
                                    const char *value, size_t value_length) {
#if PHP_VERSION_ID < 80000
    zend_update_property_stringl(ce, object, name, length, value, value_length);
#else
    zend_update_property_stringl(ce, Z_OBJ_P(object), name, length, value, value_length);
#endif
}

inline void restrict_class(zend_class_entry *ce) {
#if PHP_VERSION_ID < 80100
    ce->serialize = zend_class_serialize_deny;
    ce->unserialize = zend_class_unserialize_deny;
#else
    ce->ce_flags |= ZEND_ACC_NO_DYNAMIC_PROPERTIES | ZEND_ACC_NOT_SERIALIZABLE;
#endif
}

inline bool array_is_list(zend_array *array) {
#if PHP_VERSION_ID < 80100
    zend_ulong expected = 0;
    zend_ulong index;
    zend_string *key;
    ZEND_HASH_FOREACH_KEY(array, index, key) {
        if (key != nullptr || index != expected++) {
            return false;
        }
    } ZEND_HASH_FOREACH_END();
    return true;
#else
    return zend_array_is_list(array);
#endif
}

inline void argument_count_error(const char *message) {
#if PHP_VERSION_ID < 80000
    zend_throw_exception(zend_ce_argument_count_error, message, 0);
#else
    zend_argument_count_error("%s", message);
#endif
}

inline void value_error(const char *message) {
#if PHP_VERSION_ID < 80000
    zend_throw_exception(zend_ce_exception, message, 0);
#else
    zend_value_error("%s", message);
#endif
}

}  // namespace zend_compat
}  // namespace phpy
