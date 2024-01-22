/* This is a generated file, edit the .stub.php file instead.
 * Stub hash: 6a407b4c43fb5a083640beb41396d4fd75faf604 */

ZEND_BEGIN_ARG_INFO_EX(arginfo_class_PyDict___construct, 0, 0, 0)
	ZEND_ARG_TYPE_INFO_WITH_DEFAULT_VALUE(0, value, IS_ARRAY, 0, "null")
ZEND_END_ARG_INFO()

ZEND_BEGIN_ARG_WITH_RETURN_TYPE_INFO_EX(arginfo_class_PyDict_offsetGet, 0, 1, IS_MIXED, 0)
	ZEND_ARG_TYPE_INFO(0, offset, IS_MIXED, 0)
ZEND_END_ARG_INFO()

ZEND_BEGIN_ARG_WITH_RETURN_TYPE_INFO_EX(arginfo_class_PyDict_offsetSet, 0, 2, IS_VOID, 0)
	ZEND_ARG_TYPE_INFO(0, offset, IS_MIXED, 0)
	ZEND_ARG_TYPE_INFO(0, value, IS_MIXED, 0)
ZEND_END_ARG_INFO()

ZEND_BEGIN_ARG_WITH_RETURN_TYPE_INFO_EX(arginfo_class_PyDict_offsetUnset, 0, 1, IS_VOID, 0)
	ZEND_ARG_TYPE_INFO(0, offset, IS_MIXED, 0)
ZEND_END_ARG_INFO()

ZEND_BEGIN_ARG_WITH_RETURN_TYPE_INFO_EX(arginfo_class_PyDict_offsetExists, 0, 1, _IS_BOOL, 0)
	ZEND_ARG_TYPE_INFO(0, offset, IS_MIXED, 0)
ZEND_END_ARG_INFO()

ZEND_BEGIN_ARG_WITH_RETURN_TYPE_INFO_EX(arginfo_class_PyDict_key, 0, 0, IS_MIXED, 0)
ZEND_END_ARG_INFO()

#define arginfo_class_PyDict_current arginfo_class_PyDict_key

ZEND_BEGIN_ARG_WITH_RETURN_TYPE_INFO_EX(arginfo_class_PyDict_count, 0, 0, IS_LONG, 0)
ZEND_END_ARG_INFO()


ZEND_METHOD(PyDict, __construct);
ZEND_METHOD(PyDict, offsetGet);
ZEND_METHOD(PyDict, offsetSet);
ZEND_METHOD(PyDict, offsetUnset);
ZEND_METHOD(PyDict, offsetExists);
ZEND_METHOD(PyDict, key);
ZEND_METHOD(PyDict, current);
ZEND_METHOD(PyDict, count);


static const zend_function_entry class_PyDict_methods[] = {
	ZEND_ME(PyDict, __construct, arginfo_class_PyDict___construct, ZEND_ACC_PUBLIC)
	ZEND_ME(PyDict, offsetGet, arginfo_class_PyDict_offsetGet, ZEND_ACC_PUBLIC)
	ZEND_ME(PyDict, offsetSet, arginfo_class_PyDict_offsetSet, ZEND_ACC_PUBLIC)
	ZEND_ME(PyDict, offsetUnset, arginfo_class_PyDict_offsetUnset, ZEND_ACC_PUBLIC)
	ZEND_ME(PyDict, offsetExists, arginfo_class_PyDict_offsetExists, ZEND_ACC_PUBLIC)
	ZEND_ME(PyDict, key, arginfo_class_PyDict_key, ZEND_ACC_PUBLIC)
	ZEND_ME(PyDict, current, arginfo_class_PyDict_current, ZEND_ACC_PUBLIC)
	ZEND_ME(PyDict, count, arginfo_class_PyDict_count, ZEND_ACC_PUBLIC)
	ZEND_FE_END
};
