/* This is a generated file, edit the .stub.php file instead.
 * Stub hash: 6c2b1214662b2b65bab2468fcd8c505dd8dca9a0 */

ZEND_BEGIN_ARG_INFO_EX(arginfo_class_PyObject___construct, 0, 0, 0)
	ZEND_ARG_TYPE_INFO_WITH_DEFAULT_VALUE(0, value, IS_MIXED, 0, "null")
ZEND_END_ARG_INFO()

ZEND_BEGIN_ARG_WITH_RETURN_TYPE_INFO_EX(arginfo_class_PyObject___call, 0, 2, IS_MIXED, 0)
	ZEND_ARG_TYPE_INFO(0, name, IS_STRING, 0)
	ZEND_ARG_TYPE_INFO(0, arguments, IS_ARRAY, 0)
ZEND_END_ARG_INFO()

ZEND_BEGIN_ARG_WITH_RETURN_TYPE_INFO_EX(arginfo_class_PyObject___get, 0, 1, IS_MIXED, 0)
	ZEND_ARG_TYPE_INFO(0, name, IS_STRING, 0)
ZEND_END_ARG_INFO()

ZEND_BEGIN_ARG_WITH_RETURN_TYPE_INFO_EX(arginfo_class_PyObject___set, 0, 2, IS_VOID, 0)
	ZEND_ARG_TYPE_INFO(0, name, IS_STRING, 0)
	ZEND_ARG_TYPE_INFO(0, value, IS_MIXED, 0)
ZEND_END_ARG_INFO()

ZEND_BEGIN_ARG_WITH_RETURN_TYPE_INFO_EX(arginfo_class_PyObject___toString, 0, 0, IS_STRING, 0)
ZEND_END_ARG_INFO()

ZEND_BEGIN_ARG_WITH_RETURN_TYPE_INFO_EX(arginfo_class_PyObject___invoke, 0, 0, IS_MIXED, 0)
	ZEND_ARG_VARIADIC_TYPE_INFO(0, arguments, IS_MIXED, 0)
ZEND_END_ARG_INFO()

ZEND_BEGIN_ARG_WITH_RETURN_TYPE_INFO_EX(arginfo_class_PyObject_offsetGet, 0, 1, IS_MIXED, 0)
	ZEND_ARG_TYPE_INFO(0, offset, IS_MIXED, 0)
ZEND_END_ARG_INFO()

ZEND_BEGIN_ARG_WITH_RETURN_TYPE_INFO_EX(arginfo_class_PyObject_offsetSet, 0, 2, IS_VOID, 0)
	ZEND_ARG_TYPE_INFO(0, offset, IS_MIXED, 0)
	ZEND_ARG_TYPE_INFO(0, value, IS_MIXED, 0)
ZEND_END_ARG_INFO()

ZEND_BEGIN_ARG_WITH_RETURN_TYPE_INFO_EX(arginfo_class_PyObject_offsetUnset, 0, 1, IS_VOID, 0)
	ZEND_ARG_TYPE_INFO(0, offset, IS_MIXED, 0)
ZEND_END_ARG_INFO()

ZEND_BEGIN_ARG_WITH_RETURN_TYPE_INFO_EX(arginfo_class_PyObject_offsetExists, 0, 1, _IS_BOOL, 0)
	ZEND_ARG_TYPE_INFO(0, offset, IS_MIXED, 0)
ZEND_END_ARG_INFO()

ZEND_BEGIN_ARG_WITH_RETURN_TYPE_INFO_EX(arginfo_class_PyObject_key, 0, 0, IS_MIXED, 0)
ZEND_END_ARG_INFO()

ZEND_BEGIN_ARG_WITH_RETURN_TYPE_INFO_EX(arginfo_class_PyObject_next, 0, 0, IS_VOID, 0)
ZEND_END_ARG_INFO()

#define arginfo_class_PyObject_rewind arginfo_class_PyObject_next

ZEND_BEGIN_ARG_WITH_RETURN_TYPE_INFO_EX(arginfo_class_PyObject_valid, 0, 0, _IS_BOOL, 0)
ZEND_END_ARG_INFO()

#define arginfo_class_PyObject_current arginfo_class_PyObject_key

ZEND_BEGIN_ARG_WITH_RETURN_TYPE_INFO_EX(arginfo_class_PyObject_count, 0, 0, IS_LONG, 0)
ZEND_END_ARG_INFO()


ZEND_METHOD(PyObject, __construct);
ZEND_METHOD(PyObject, __call);
ZEND_METHOD(PyObject, __get);
ZEND_METHOD(PyObject, __set);
ZEND_METHOD(PyObject, __toString);
ZEND_METHOD(PyObject, __invoke);
ZEND_METHOD(PyObject, offsetGet);
ZEND_METHOD(PyObject, offsetSet);
ZEND_METHOD(PyObject, offsetUnset);
ZEND_METHOD(PyObject, offsetExists);
ZEND_METHOD(PyObject, key);
ZEND_METHOD(PyObject, next);
ZEND_METHOD(PyObject, rewind);
ZEND_METHOD(PyObject, valid);
ZEND_METHOD(PyObject, current);
ZEND_METHOD(PyObject, count);


static const zend_function_entry class_PyObject_methods[] = {
	ZEND_ME(PyObject, __construct, arginfo_class_PyObject___construct, ZEND_ACC_PUBLIC)
	ZEND_ME(PyObject, __call, arginfo_class_PyObject___call, ZEND_ACC_PUBLIC)
	ZEND_ME(PyObject, __get, arginfo_class_PyObject___get, ZEND_ACC_PUBLIC)
	ZEND_ME(PyObject, __set, arginfo_class_PyObject___set, ZEND_ACC_PUBLIC)
	ZEND_ME(PyObject, __toString, arginfo_class_PyObject___toString, ZEND_ACC_PUBLIC)
	ZEND_ME(PyObject, __invoke, arginfo_class_PyObject___invoke, ZEND_ACC_PUBLIC)
	ZEND_ME(PyObject, offsetGet, arginfo_class_PyObject_offsetGet, ZEND_ACC_PUBLIC)
	ZEND_ME(PyObject, offsetSet, arginfo_class_PyObject_offsetSet, ZEND_ACC_PUBLIC)
	ZEND_ME(PyObject, offsetUnset, arginfo_class_PyObject_offsetUnset, ZEND_ACC_PUBLIC)
	ZEND_ME(PyObject, offsetExists, arginfo_class_PyObject_offsetExists, ZEND_ACC_PUBLIC)
	ZEND_ME(PyObject, key, arginfo_class_PyObject_key, ZEND_ACC_PUBLIC)
	ZEND_ME(PyObject, next, arginfo_class_PyObject_next, ZEND_ACC_PUBLIC)
	ZEND_ME(PyObject, rewind, arginfo_class_PyObject_rewind, ZEND_ACC_PUBLIC)
	ZEND_ME(PyObject, valid, arginfo_class_PyObject_valid, ZEND_ACC_PUBLIC)
	ZEND_ME(PyObject, current, arginfo_class_PyObject_current, ZEND_ACC_PUBLIC)
	ZEND_ME(PyObject, count, arginfo_class_PyObject_count, ZEND_ACC_PUBLIC)
	ZEND_FE_END
};
