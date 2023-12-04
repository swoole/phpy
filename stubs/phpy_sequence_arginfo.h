/* This is a generated file, edit the .stub.php file instead.
 * Stub hash: ecbc31dbd9410c1dd3f3e8715df55e6bc4d8b70b */

ZEND_BEGIN_ARG_WITH_RETURN_TYPE_INFO_EX(arginfo_class_PySequence_key, 0, 0, IS_MIXED, 0)
ZEND_END_ARG_INFO()

ZEND_BEGIN_ARG_WITH_RETURN_TYPE_INFO_EX(arginfo_class_PySequence_next, 0, 0, IS_VOID, 0)
ZEND_END_ARG_INFO()

#define arginfo_class_PySequence_rewind arginfo_class_PySequence_next

ZEND_BEGIN_ARG_WITH_RETURN_TYPE_INFO_EX(arginfo_class_PySequence_valid, 0, 0, _IS_BOOL, 0)
ZEND_END_ARG_INFO()

#define arginfo_class_PySequence_current arginfo_class_PySequence_key

ZEND_BEGIN_ARG_WITH_RETURN_TYPE_INFO_EX(arginfo_class_PySequence_count, 0, 0, IS_LONG, 0)
ZEND_END_ARG_INFO()

ZEND_BEGIN_ARG_WITH_RETURN_TYPE_INFO_EX(arginfo_class_PySequence_contains, 0, 1, _IS_BOOL, 0)
	ZEND_ARG_TYPE_INFO(0, v, IS_MIXED, 0)
ZEND_END_ARG_INFO()

ZEND_BEGIN_ARG_WITH_RETURN_OBJ_INFO_EX(arginfo_class_PySequence_slice, 0, 2, PyObject, 0)
	ZEND_ARG_TYPE_INFO(0, s, IS_LONG, 0)
	ZEND_ARG_TYPE_INFO(0, e, IS_LONG, 0)
ZEND_END_ARG_INFO()


ZEND_METHOD(PySequence, key);
ZEND_METHOD(PySequence, next);
ZEND_METHOD(PySequence, rewind);
ZEND_METHOD(PySequence, valid);
ZEND_METHOD(PySequence, current);
ZEND_METHOD(PySequence, count);
ZEND_METHOD(PySequence, contains);
ZEND_METHOD(PySequence, slice);


static const zend_function_entry class_PySequence_methods[] = {
	ZEND_ME(PySequence, key, arginfo_class_PySequence_key, ZEND_ACC_PUBLIC)
	ZEND_ME(PySequence, next, arginfo_class_PySequence_next, ZEND_ACC_PUBLIC)
	ZEND_ME(PySequence, rewind, arginfo_class_PySequence_rewind, ZEND_ACC_PUBLIC)
	ZEND_ME(PySequence, valid, arginfo_class_PySequence_valid, ZEND_ACC_PUBLIC)
	ZEND_ME(PySequence, current, arginfo_class_PySequence_current, ZEND_ACC_PUBLIC)
	ZEND_ME(PySequence, count, arginfo_class_PySequence_count, ZEND_ACC_PUBLIC)
	ZEND_ME(PySequence, contains, arginfo_class_PySequence_contains, ZEND_ACC_PUBLIC)
	ZEND_ME(PySequence, slice, arginfo_class_PySequence_slice, ZEND_ACC_PUBLIC)
	ZEND_FE_END
};
