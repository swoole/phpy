/* This is a generated file, edit the .stub.php file instead.
 * Stub hash: cf5bf8017d5b71cae005534cc88f718b113589b0 */

ZEND_BEGIN_ARG_INFO_EX(arginfo_class_PySet___construct, 0, 0, 0)
	ZEND_ARG_TYPE_INFO_WITH_DEFAULT_VALUE(0, data, IS_ARRAY, 0, "null")
ZEND_END_ARG_INFO()

ZEND_BEGIN_ARG_WITH_RETURN_TYPE_INFO_EX(arginfo_class_PySet_key, 0, 0, IS_MIXED, 0)
ZEND_END_ARG_INFO()

ZEND_BEGIN_ARG_WITH_RETURN_TYPE_INFO_EX(arginfo_class_PySet_next, 0, 0, IS_VOID, 0)
ZEND_END_ARG_INFO()

#define arginfo_class_PySet_rewind arginfo_class_PySet_next

ZEND_BEGIN_ARG_WITH_RETURN_TYPE_INFO_EX(arginfo_class_PySet_valid, 0, 0, _IS_BOOL, 0)
ZEND_END_ARG_INFO()

#define arginfo_class_PySet_current arginfo_class_PySet_key

ZEND_BEGIN_ARG_WITH_RETURN_TYPE_INFO_EX(arginfo_class_PySet_count, 0, 0, IS_LONG, 0)
ZEND_END_ARG_INFO()

ZEND_BEGIN_ARG_WITH_RETURN_TYPE_INFO_EX(arginfo_class_PySet_contains, 0, 1, _IS_BOOL, 0)
	ZEND_ARG_TYPE_INFO(0, v, IS_MIXED, 0)
ZEND_END_ARG_INFO()


ZEND_METHOD(PySet, __construct);
ZEND_METHOD(PySet, key);
ZEND_METHOD(PySet, next);
ZEND_METHOD(PySet, rewind);
ZEND_METHOD(PySet, valid);
ZEND_METHOD(PySet, current);
ZEND_METHOD(PySet, count);
ZEND_METHOD(PySet, contains);


static const zend_function_entry class_PySet_methods[] = {
	ZEND_ME(PySet, __construct, arginfo_class_PySet___construct, ZEND_ACC_PUBLIC)
	ZEND_ME(PySet, key, arginfo_class_PySet_key, ZEND_ACC_PUBLIC)
	ZEND_ME(PySet, next, arginfo_class_PySet_next, ZEND_ACC_PUBLIC)
	ZEND_ME(PySet, rewind, arginfo_class_PySet_rewind, ZEND_ACC_PUBLIC)
	ZEND_ME(PySet, valid, arginfo_class_PySet_valid, ZEND_ACC_PUBLIC)
	ZEND_ME(PySet, current, arginfo_class_PySet_current, ZEND_ACC_PUBLIC)
	ZEND_ME(PySet, count, arginfo_class_PySet_count, ZEND_ACC_PUBLIC)
	ZEND_ME(PySet, contains, arginfo_class_PySet_contains, ZEND_ACC_PUBLIC)
	ZEND_FE_END
};
