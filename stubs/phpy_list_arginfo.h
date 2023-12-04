/* This is a generated file, edit the .stub.php file instead.
 * Stub hash: 436fd5ef30d110a5462ca57bdb433b0df41a6bf4 */

ZEND_BEGIN_ARG_INFO_EX(arginfo_class_PyList___construct, 0, 0, 0)
ZEND_END_ARG_INFO()

ZEND_BEGIN_ARG_WITH_RETURN_TYPE_INFO_EX(arginfo_class_PyList_offsetGet, 0, 1, IS_MIXED, 0)
	ZEND_ARG_TYPE_INFO(0, offset, IS_MIXED, 0)
ZEND_END_ARG_INFO()

ZEND_BEGIN_ARG_WITH_RETURN_TYPE_INFO_EX(arginfo_class_PyList_offsetSet, 0, 2, IS_VOID, 0)
	ZEND_ARG_TYPE_INFO(0, offset, IS_MIXED, 0)
	ZEND_ARG_TYPE_INFO(0, value, IS_MIXED, 0)
ZEND_END_ARG_INFO()

ZEND_BEGIN_ARG_WITH_RETURN_TYPE_INFO_EX(arginfo_class_PyList_offsetUnset, 0, 1, IS_VOID, 0)
	ZEND_ARG_TYPE_INFO(0, offset, IS_MIXED, 0)
ZEND_END_ARG_INFO()

ZEND_BEGIN_ARG_WITH_RETURN_TYPE_INFO_EX(arginfo_class_PyList_offsetExists, 0, 1, _IS_BOOL, 0)
	ZEND_ARG_TYPE_INFO(0, offset, IS_MIXED, 0)
ZEND_END_ARG_INFO()


ZEND_METHOD(PyList, __construct);
ZEND_METHOD(PyList, offsetGet);
ZEND_METHOD(PyList, offsetSet);
ZEND_METHOD(PyList, offsetUnset);
ZEND_METHOD(PyList, offsetExists);


static const zend_function_entry class_PyList_methods[] = {
	ZEND_ME(PyList, __construct, arginfo_class_PyList___construct, ZEND_ACC_PUBLIC)
	ZEND_ME(PyList, offsetGet, arginfo_class_PyList_offsetGet, ZEND_ACC_PUBLIC)
	ZEND_ME(PyList, offsetSet, arginfo_class_PyList_offsetSet, ZEND_ACC_PUBLIC)
	ZEND_ME(PyList, offsetUnset, arginfo_class_PyList_offsetUnset, ZEND_ACC_PUBLIC)
	ZEND_ME(PyList, offsetExists, arginfo_class_PyList_offsetExists, ZEND_ACC_PUBLIC)
	ZEND_FE_END
};
