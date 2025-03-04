/* This is a generated file, edit the .stub.php file instead.
 * Stub hash: 0e7198dc700f1de9b5150dd732c8ee62e736b517 */

ZEND_BEGIN_ARG_WITH_RETURN_TYPE_INFO_EX(arginfo_class_PyCore_import, 0, 1, IS_MIXED, 0)
	ZEND_ARG_TYPE_INFO(0, name, IS_STRING, 0)
ZEND_END_ARG_INFO()

ZEND_BEGIN_ARG_WITH_RETURN_TYPE_INFO_EX(arginfo_class_PyCore_eval, 0, 1, IS_MIXED, 0)
	ZEND_ARG_TYPE_INFO(0, code, IS_STRING, 0)
	ZEND_ARG_TYPE_INFO_WITH_DEFAULT_VALUE(0, globals, IS_ARRAY, 1, "null")
ZEND_END_ARG_INFO()

ZEND_BEGIN_ARG_WITH_RETURN_OBJ_INFO_EX(arginfo_class_PyCore_int, 0, 1, PyObject, 0)
	ZEND_ARG_TYPE_INFO(0, value, IS_MIXED, 0)
ZEND_END_ARG_INFO()

#define arginfo_class_PyCore_float arginfo_class_PyCore_int

ZEND_BEGIN_ARG_WITH_RETURN_OBJ_INFO_EX(arginfo_class_PyCore_bytes, 0, 0, PyObject, 0)
	ZEND_ARG_TYPE_INFO_WITH_DEFAULT_VALUE(0, value, IS_MIXED, 0, "null")
ZEND_END_ARG_INFO()

#define arginfo_class_PyCore_object arginfo_class_PyCore_bytes

ZEND_BEGIN_ARG_WITH_RETURN_OBJ_INFO_EX(arginfo_class_PyCore_fn, 0, 1, PyObject, 0)
	ZEND_ARG_TYPE_INFO(0, cb, IS_CALLABLE, 0)
ZEND_END_ARG_INFO()

ZEND_BEGIN_ARG_WITH_RETURN_TYPE_INFO_EX(arginfo_class_PyCore_scalar, 0, 1, IS_MIXED, 0)
	ZEND_ARG_TYPE_INFO(0, value, IS_MIXED, 0)
ZEND_END_ARG_INFO()

ZEND_BEGIN_ARG_WITH_RETURN_TYPE_INFO_EX(arginfo_class_PyCore_next, 0, 1, IS_MIXED, 0)
	ZEND_ARG_OBJ_INFO(0, iter, PyObject, 0)
ZEND_END_ARG_INFO()

ZEND_BEGIN_ARG_WITH_RETURN_TYPE_MASK_EX(arginfo_class_PyCore_fileno, 0, 1, MAY_BE_LONG|MAY_BE_FALSE)
	ZEND_ARG_INFO(0, fp)
ZEND_END_ARG_INFO()

ZEND_BEGIN_ARG_WITH_RETURN_TYPE_INFO_EX(arginfo_class_PyCore_setOptions, 0, 1, IS_VOID, 0)
	ZEND_ARG_TYPE_INFO(0, options, IS_ARRAY, 0)
ZEND_END_ARG_INFO()

ZEND_BEGIN_ARG_WITH_RETURN_TYPE_INFO_EX(arginfo_class_PyCore_raise, 0, 1, IS_VOID, 0)
	ZEND_ARG_OBJ_INFO(0, type, PyObject, 0)
	ZEND_ARG_TYPE_INFO_WITH_DEFAULT_VALUE(0, value, IS_MIXED, 0, "null")
ZEND_END_ARG_INFO()

ZEND_BEGIN_ARG_WITH_RETURN_TYPE_INFO_EX(arginfo_class_PyCore___callStatic, 0, 2, IS_MIXED, 0)
	ZEND_ARG_TYPE_INFO(0, name, IS_STRING, 0)
	ZEND_ARG_TYPE_INFO(0, arguments, IS_ARRAY, 0)
ZEND_END_ARG_INFO()


ZEND_METHOD(PyCore, import);
ZEND_METHOD(PyCore, eval);
ZEND_METHOD(PyCore, int);
ZEND_METHOD(PyCore, float);
ZEND_METHOD(PyCore, bytes);
ZEND_METHOD(PyCore, object);
ZEND_METHOD(PyCore, fn);
ZEND_METHOD(PyCore, scalar);
ZEND_METHOD(PyCore, next);
ZEND_METHOD(PyCore, fileno);
ZEND_METHOD(PyCore, setOptions);
ZEND_METHOD(PyCore, raise);
ZEND_METHOD(PyCore, __callStatic);


static const zend_function_entry class_PyCore_methods[] = {
	ZEND_ME(PyCore, import, arginfo_class_PyCore_import, ZEND_ACC_PUBLIC|ZEND_ACC_STATIC)
	ZEND_ME(PyCore, eval, arginfo_class_PyCore_eval, ZEND_ACC_PUBLIC|ZEND_ACC_STATIC)
	ZEND_ME(PyCore, int, arginfo_class_PyCore_int, ZEND_ACC_PUBLIC|ZEND_ACC_STATIC)
	ZEND_ME(PyCore, float, arginfo_class_PyCore_float, ZEND_ACC_PUBLIC|ZEND_ACC_STATIC)
	ZEND_ME(PyCore, bytes, arginfo_class_PyCore_bytes, ZEND_ACC_PUBLIC|ZEND_ACC_STATIC)
	ZEND_ME(PyCore, object, arginfo_class_PyCore_object, ZEND_ACC_PUBLIC|ZEND_ACC_STATIC)
	ZEND_ME(PyCore, fn, arginfo_class_PyCore_fn, ZEND_ACC_PUBLIC|ZEND_ACC_STATIC)
	ZEND_ME(PyCore, scalar, arginfo_class_PyCore_scalar, ZEND_ACC_PUBLIC|ZEND_ACC_STATIC)
	ZEND_ME(PyCore, next, arginfo_class_PyCore_next, ZEND_ACC_PUBLIC|ZEND_ACC_STATIC)
	ZEND_ME(PyCore, fileno, arginfo_class_PyCore_fileno, ZEND_ACC_PUBLIC|ZEND_ACC_STATIC)
	ZEND_ME(PyCore, setOptions, arginfo_class_PyCore_setOptions, ZEND_ACC_PUBLIC|ZEND_ACC_STATIC)
	ZEND_ME(PyCore, raise, arginfo_class_PyCore_raise, ZEND_ACC_PUBLIC|ZEND_ACC_STATIC)
	ZEND_ME(PyCore, __callStatic, arginfo_class_PyCore___callStatic, ZEND_ACC_PUBLIC|ZEND_ACC_STATIC)
	ZEND_FE_END
};
