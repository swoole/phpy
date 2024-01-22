/* This is a generated file, edit the .stub.php file instead.
 * Stub hash: 419f0997878e604e5e6f79d80e7d9d27b9c6229d */

ZEND_BEGIN_ARG_INFO_EX(arginfo_class_PySet___construct, 0, 0, 0)
	ZEND_ARG_TYPE_INFO_WITH_DEFAULT_VALUE(0, data, IS_ARRAY, 0, "null")
ZEND_END_ARG_INFO()

ZEND_BEGIN_ARG_WITH_RETURN_TYPE_INFO_EX(arginfo_class_PySet_count, 0, 0, IS_LONG, 0)
ZEND_END_ARG_INFO()

ZEND_BEGIN_ARG_WITH_RETURN_TYPE_INFO_EX(arginfo_class_PySet_contains, 0, 1, _IS_BOOL, 0)
	ZEND_ARG_TYPE_INFO(0, v, IS_MIXED, 0)
ZEND_END_ARG_INFO()


ZEND_METHOD(PySet, __construct);
ZEND_METHOD(PySet, count);
ZEND_METHOD(PySet, contains);


static const zend_function_entry class_PySet_methods[] = {
	ZEND_ME(PySet, __construct, arginfo_class_PySet___construct, ZEND_ACC_PUBLIC)
	ZEND_ME(PySet, count, arginfo_class_PySet_count, ZEND_ACC_PUBLIC)
	ZEND_ME(PySet, contains, arginfo_class_PySet_contains, ZEND_ACC_PUBLIC)
	ZEND_FE_END
};
