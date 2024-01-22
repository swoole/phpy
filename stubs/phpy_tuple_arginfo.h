/* This is a generated file, edit the .stub.php file instead.
 * Stub hash: 815afffaa8deaedd0e553dd377b8945c1328ae47 */

ZEND_BEGIN_ARG_INFO_EX(arginfo_class_PyTuple___construct, 0, 0, 1)
	ZEND_ARG_TYPE_INFO(0, data, IS_MIXED, 0)
ZEND_END_ARG_INFO()

ZEND_BEGIN_ARG_WITH_RETURN_TYPE_INFO_EX(arginfo_class_PyTuple_offsetGet, 0, 1, IS_MIXED, 0)
	ZEND_ARG_TYPE_INFO(0, offset, IS_MIXED, 0)
ZEND_END_ARG_INFO()

ZEND_BEGIN_ARG_WITH_RETURN_TYPE_INFO_EX(arginfo_class_PyTuple_offsetSet, 0, 2, IS_VOID, 0)
	ZEND_ARG_TYPE_INFO(0, offset, IS_MIXED, 0)
	ZEND_ARG_TYPE_INFO(0, value, IS_MIXED, 0)
ZEND_END_ARG_INFO()

ZEND_BEGIN_ARG_WITH_RETURN_TYPE_INFO_EX(arginfo_class_PyTuple_offsetUnset, 0, 1, IS_VOID, 0)
	ZEND_ARG_TYPE_INFO(0, offset, IS_MIXED, 0)
ZEND_END_ARG_INFO()

ZEND_BEGIN_ARG_WITH_RETURN_TYPE_INFO_EX(arginfo_class_PyTuple_offsetExists, 0, 1, _IS_BOOL, 0)
	ZEND_ARG_TYPE_INFO(0, offset, IS_MIXED, 0)
ZEND_END_ARG_INFO()


ZEND_METHOD(PyTuple, __construct);
ZEND_METHOD(PyTuple, offsetGet);
ZEND_METHOD(PyTuple, offsetSet);
ZEND_METHOD(PyTuple, offsetUnset);
ZEND_METHOD(PyTuple, offsetExists);


static const zend_function_entry class_PyTuple_methods[] = {
	ZEND_ME(PyTuple, __construct, arginfo_class_PyTuple___construct, ZEND_ACC_PUBLIC)
	ZEND_ME(PyTuple, offsetGet, arginfo_class_PyTuple_offsetGet, ZEND_ACC_PUBLIC)
	ZEND_ME(PyTuple, offsetSet, arginfo_class_PyTuple_offsetSet, ZEND_ACC_PUBLIC)
	ZEND_ME(PyTuple, offsetUnset, arginfo_class_PyTuple_offsetUnset, ZEND_ACC_PUBLIC)
	ZEND_ME(PyTuple, offsetExists, arginfo_class_PyTuple_offsetExists, ZEND_ACC_PUBLIC)
	ZEND_FE_END
};
