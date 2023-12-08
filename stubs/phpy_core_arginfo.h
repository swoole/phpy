/* This is a generated file, edit the .stub.php file instead.
 * Stub hash: 7a78523705f8bb18ce36a8d90f628ce6a91640f1 */

ZEND_BEGIN_ARG_WITH_RETURN_TYPE_INFO_EX(arginfo_class_PyCore_import, 0, 1, IS_MIXED, 0)
	ZEND_ARG_TYPE_INFO(0, name, IS_STRING, 0)
ZEND_END_ARG_INFO()

ZEND_BEGIN_ARG_WITH_RETURN_TYPE_INFO_EX(arginfo_class_PyCore_eval, 0, 1, IS_MIXED, 0)
	ZEND_ARG_TYPE_INFO(0, code, IS_STRING, 0)
ZEND_END_ARG_INFO()

ZEND_BEGIN_ARG_WITH_RETURN_OBJ_INFO_EX(arginfo_class_PyCore_int, 0, 1, PyObject, 0)
	ZEND_ARG_TYPE_INFO(0, value, IS_MIXED, 0)
ZEND_END_ARG_INFO()

#define arginfo_class_PyCore_float arginfo_class_PyCore_int

ZEND_BEGIN_ARG_WITH_RETURN_OBJ_INFO_EX(arginfo_class_PyCore_fn, 0, 1, PyObject, 0)
	ZEND_ARG_TYPE_INFO(0, cb, IS_CALLABLE, 0)
ZEND_END_ARG_INFO()

ZEND_BEGIN_ARG_WITH_RETURN_TYPE_INFO_EX(arginfo_class_PyCore_scalar, 0, 1, IS_MIXED, 0)
	ZEND_ARG_TYPE_INFO(0, value, IS_MIXED, 0)
ZEND_END_ARG_INFO()

ZEND_BEGIN_ARG_WITH_RETURN_OBJ_INFO_EX(arginfo_class_PyCore_iter, 0, 1, PyObject, 1)
	ZEND_ARG_OBJ_INFO(0, value, PyObject, 0)
ZEND_END_ARG_INFO()

ZEND_BEGIN_ARG_WITH_RETURN_OBJ_INFO_EX(arginfo_class_PyCore_next, 0, 1, PyObject, 1)
	ZEND_ARG_OBJ_INFO(0, iter, PyObject, 0)
ZEND_END_ARG_INFO()

ZEND_BEGIN_ARG_WITH_RETURN_TYPE_INFO_EX(arginfo_class_PyCore___callStatic, 0, 2, IS_MIXED, 0)
	ZEND_ARG_TYPE_INFO(0, name, IS_STRING, 0)
	ZEND_ARG_TYPE_INFO(0, arguments, IS_ARRAY, 0)
ZEND_END_ARG_INFO()


ZEND_METHOD(PyCore, import);
ZEND_METHOD(PyCore, eval);
ZEND_METHOD(PyCore, int);
ZEND_METHOD(PyCore, float);
ZEND_METHOD(PyCore, fn);
ZEND_METHOD(PyCore, scalar);
ZEND_METHOD(PyCore, iter);
ZEND_METHOD(PyCore, next);
ZEND_METHOD(PyCore, __callStatic);


static const zend_function_entry class_PyCore_methods[] = {
	ZEND_ME(PyCore, import, arginfo_class_PyCore_import, ZEND_ACC_PUBLIC|ZEND_ACC_STATIC)
	ZEND_ME(PyCore, eval, arginfo_class_PyCore_eval, ZEND_ACC_PUBLIC|ZEND_ACC_STATIC)
	ZEND_ME(PyCore, int, arginfo_class_PyCore_int, ZEND_ACC_PUBLIC|ZEND_ACC_STATIC)
	ZEND_ME(PyCore, float, arginfo_class_PyCore_float, ZEND_ACC_PUBLIC|ZEND_ACC_STATIC)
	ZEND_ME(PyCore, fn, arginfo_class_PyCore_fn, ZEND_ACC_PUBLIC|ZEND_ACC_STATIC)
	ZEND_ME(PyCore, scalar, arginfo_class_PyCore_scalar, ZEND_ACC_PUBLIC|ZEND_ACC_STATIC)
	ZEND_ME(PyCore, iter, arginfo_class_PyCore_iter, ZEND_ACC_PUBLIC|ZEND_ACC_STATIC)
	ZEND_ME(PyCore, next, arginfo_class_PyCore_next, ZEND_ACC_PUBLIC|ZEND_ACC_STATIC)
	ZEND_ME(PyCore, __callStatic, arginfo_class_PyCore___callStatic, ZEND_ACC_PUBLIC|ZEND_ACC_STATIC)
	ZEND_FE_END
};
