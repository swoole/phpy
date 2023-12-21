/* This is a generated file, edit the .stub.php file instead.
 * Stub hash: c9bd2974ad735b66577b33d9fe2dfeb2684e647b */

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


ZEND_METHOD(PyObject, __construct);
ZEND_METHOD(PyObject, __call);
ZEND_METHOD(PyObject, __get);
ZEND_METHOD(PyObject, __set);
ZEND_METHOD(PyObject, __toString);
ZEND_METHOD(PyObject, __invoke);


static const zend_function_entry class_PyObject_methods[] = {
	ZEND_ME(PyObject, __construct, arginfo_class_PyObject___construct, ZEND_ACC_PUBLIC)
	ZEND_ME(PyObject, __call, arginfo_class_PyObject___call, ZEND_ACC_PUBLIC)
	ZEND_ME(PyObject, __get, arginfo_class_PyObject___get, ZEND_ACC_PUBLIC)
	ZEND_ME(PyObject, __set, arginfo_class_PyObject___set, ZEND_ACC_PUBLIC)
	ZEND_ME(PyObject, __toString, arginfo_class_PyObject___toString, ZEND_ACC_PUBLIC)
	ZEND_ME(PyObject, __invoke, arginfo_class_PyObject___invoke, ZEND_ACC_PUBLIC)
	ZEND_FE_END
};
