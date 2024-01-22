/* This is a generated file, edit the .stub.php file instead.
 * Stub hash: d279316cff457073d75f1338d393b263f29b759e */

ZEND_BEGIN_ARG_WITH_RETURN_TYPE_INFO_EX(arginfo_class_PySequence_contains, 0, 1, _IS_BOOL, 0)
	ZEND_ARG_TYPE_INFO(0, v, IS_MIXED, 0)
ZEND_END_ARG_INFO()

ZEND_BEGIN_ARG_WITH_RETURN_OBJ_INFO_EX(arginfo_class_PySequence_slice, 0, 2, PyObject, 0)
	ZEND_ARG_TYPE_INFO(0, s, IS_LONG, 0)
	ZEND_ARG_TYPE_INFO(0, e, IS_LONG, 0)
ZEND_END_ARG_INFO()


ZEND_METHOD(PySequence, contains);
ZEND_METHOD(PySequence, slice);


static const zend_function_entry class_PySequence_methods[] = {
	ZEND_ME(PySequence, contains, arginfo_class_PySequence_contains, ZEND_ACC_PUBLIC)
	ZEND_ME(PySequence, slice, arginfo_class_PySequence_slice, ZEND_ACC_PUBLIC)
	ZEND_FE_END
};
