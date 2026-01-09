/*
  +----------------------------------------------------------------------+
  | Phpy                                                                 |
  +----------------------------------------------------------------------+
  | This source file is subject to version 2.0 of the Apache license,    |
  | that is bundled with this package in the file LICENSE, and is        |
  | available through the world-wide-web at the following url:           |
  | http://www.apache.org/licenses/LICENSE-2.0.html                      |
  | If you did not receive a copy of the Apache2.0 license and are unable|
  | to obtain it through the world-wide-web, please send a note to       |
  | license@swoole.com so we can mail you a copy immediately.            |
  +----------------------------------------------------------------------+
  | Author: Tianfeng Han  <rango@swoole.com>                             |
  | Copyright: 上海识沃网络科技有限公司                                       |
  +----------------------------------------------------------------------+
 */

#include "phpy.h"

using namespace phpy::php;

#define GET_OP_VAR(n, v)                                                                                               \
    if (opline->op##n##_type == IS_CONST) {                                                                            \
        v = RT_CONSTANT(opline, opline->op##n);                                                                        \
    } else if (UNEXPECTED(opline->op##n##_type == IS_UNUSED)) {                                                        \
        return ZEND_USER_OPCODE_DISPATCH;                                                                              \
    } else {                                                                                                           \
        v = EX_VAR(opline->op##n.var);                                                                                 \
    }                                                                                                                  \
    ZVAL_DEREF(v);

#define RETURN_VALUE_USED(opline) ((opline)->result_type != IS_UNUSED)

#define FREE_OP_VAR(n, zv)                                                                                             \
    if (opline->op##n##_type & (IS_TMP_VAR | IS_VAR)) {                                                                \
        zval_ptr_dtor_nogc(zv);                                                                                        \
    }

typedef PyObject *(*NumberProtocolFn)(PyObject *o1, PyObject *o2);

static void print_error() {
	PyObject *ptype, *pvalue, *ptraceback;
	PyErr_Fetch(&ptype, &pvalue, &ptraceback);
	if (pvalue == NULL) {
		return;
	}

	PyObject* str_obj = PyObject_Repr(pvalue);
	Py_XDECREF(ptype);
	Py_XDECREF(ptraceback);
	PyErr_Clear();

	if (!str_obj) {
		return;
	}

	zend_error(E_WARNING, "PyError: %s", PyUnicode_AsUTF8(str_obj));
	Py_DECREF(str_obj);
}

static int opcode_handler_number_op(NumberProtocolFn fn, zend_execute_data *execute_data) {
    const zend_op *opline = EX(opline);
    zval *left, *right;
    GET_OP_VAR(1, left);
    GET_OP_VAR(2, right);

    PyObject *result = nullptr;

    if (Z_TYPE_P(left) == IS_OBJECT && is_pyobject(left)) {
        PyObject *obj = phpy_object_get_handle(left);
        PyObject *obj_right = php2py(right);
        result = fn(obj, obj_right);
        Py_DECREF(obj_right);
    } else if (Z_TYPE_P(right) == IS_OBJECT && is_pyobject(right)) {
        PyObject *obj = phpy_object_get_handle(right);
        PyObject *obj_left = php2py(left);
        result = fn(obj_left, obj);
        Py_DECREF(obj_left);
    }

    // The `result` must be a new reference.
    if (result) {
        if (result == Py_None) {
        	print_error();
            Py_DECREF(result);
            ZVAL_NULL(EX_VAR(opline->result.var));
        } else {
            new_object_no_addref(EX_VAR(opline->result.var), result);
        }
        FREE_OP_VAR(1, left);
        FREE_OP_VAR(2, right);
        EX(opline)++;
        return ZEND_USER_OPCODE_CONTINUE;
    }

    return ZEND_USER_OPCODE_DISPATCH;
}

static int opcode_handler_compare_op(int op, zend_execute_data *execute_data) {
    const zend_op *opline = EX(opline);
    zval *left, *right;
    GET_OP_VAR(1, left);
    GET_OP_VAR(2, right);

    bool is_pyobj = false;
    int result;

    if (Z_TYPE_P(left) == IS_OBJECT && is_pyobject(left)) {
        PyObject *obj_left = phpy_object_get_handle(left);
        PyObject *obj_right = php2py(right);
        result = PyObject_RichCompareBool(obj_left, obj_right, op);
        Py_DECREF(obj_right);
        is_pyobj = true;
    } else if (Z_TYPE_P(right) == IS_OBJECT && is_pyobject(right)) {
        PyObject *obj_right = phpy_object_get_handle(right);
        PyObject *obj_left = php2py(left);
        result = PyObject_RichCompareBool(obj_left, obj_right, op);
        Py_DECREF(obj_left);
        is_pyobj = true;
    }

    if (is_pyobj) {
        if (result == -1) {
        	print_error();
            ZVAL_NULL(EX_VAR(opline->result.var));
        } else {
            ZVAL_BOOL(EX_VAR(opline->result.var), result == 1);
        }
        FREE_OP_VAR(1, left);
        FREE_OP_VAR(2, right);
        EX(opline)++;
        return ZEND_USER_OPCODE_CONTINUE;
    }

    return ZEND_USER_OPCODE_DISPATCH;
}

static int opcode_handler_add(zend_execute_data *execute_data) {
    return opcode_handler_number_op(PyNumber_Add, execute_data);
}

static int opcode_handler_sub(zend_execute_data *execute_data) {
    return opcode_handler_number_op(PyNumber_Subtract, execute_data);
}

static int opcode_handler_mul(zend_execute_data *execute_data) {
    return opcode_handler_number_op(PyNumber_Multiply, execute_data);
}

static int opcode_handler_div(zend_execute_data *execute_data) {
    return opcode_handler_number_op(PyNumber_FloorDivide, execute_data);
}

static int opcode_handler_mod(zend_execute_data *execute_data) {
    return opcode_handler_number_op(PyNumber_Remainder, execute_data);
}

static PyObject *py_pow(PyObject *o1, PyObject *o2) {
    return PyNumber_Power(o1, o2, Py_None);
}

static int opcode_handler_pow(zend_execute_data *execute_data) {
    return opcode_handler_number_op(py_pow, execute_data);
}

static int opcode_handler_left_shift(zend_execute_data *execute_data) {
    return opcode_handler_number_op(PyNumber_Lshift, execute_data);
}

static int opcode_handler_right_shift(zend_execute_data *execute_data) {
    return opcode_handler_number_op(PyNumber_Rshift, execute_data);
}

static int opcode_handler_bitwise_and(zend_execute_data *execute_data) {
    return opcode_handler_number_op(PyNumber_And, execute_data);
}

static int opcode_handler_bitwise_or(zend_execute_data *execute_data) {
    return opcode_handler_number_op(PyNumber_Or, execute_data);
}

static int opcode_handler_bitwise_xor(zend_execute_data *execute_data) {
    return opcode_handler_number_op(PyNumber_Xor, execute_data);
}

enum binary_ops {
    add_op = 0,
    sub_op,
    mul_op,
    div_op,
    mod_op,
    shift_left_op,
    shift_right_op,
    concat_op,
    bitwise_or_op,
    bitwise_and_op,
    bitwise_xor_op,
    pow_op,
};

static int opcode_handler_assign_op(zend_execute_data *execute_data) {
    const zend_op *opline = EX(opline);
    zval *left;
    GET_OP_VAR(1, left);

    if (Z_TYPE_P(left) == IS_OBJECT && is_pyobject(left)) {
        // See: zend_binary_op
        size_t opcode = (size_t) opline->extended_value - ZEND_ADD;
        PyObject *result = nullptr;
        PyObject *left_obj = phpy_object_get_handle(left);
        zval *right;
        GET_OP_VAR(2, right);
        PyObject *obj_right = php2py(right);

        switch (opcode) {
        case add_op:
            result = PyNumber_InPlaceAdd(left_obj, obj_right);
            break;
        case sub_op:
            result = PyNumber_InPlaceSubtract(left_obj, obj_right);
            break;
        case mul_op:
            result = PyNumber_InPlaceMultiply(left_obj, obj_right);
            break;
        case div_op:
            result = PyNumber_InPlaceFloorDivide(left_obj, obj_right);
            break;
        case mod_op:
            result = PyNumber_InPlaceRemainder(left_obj, obj_right);
            break;
        case shift_left_op:
            result = PyNumber_InPlaceLshift(left_obj, obj_right);
            break;
        case shift_right_op:
            result = PyNumber_InPlaceRshift(left_obj, obj_right);
            break;
        case concat_op:
            zend_error(E_WARNING, "PyObject do not support string concat operation");
            break;
        case bitwise_or_op:
            result = PyNumber_InPlaceOr(left_obj, obj_right);
            break;
        case bitwise_and_op:
            result = PyNumber_InPlaceAnd(left_obj, obj_right);
            break;
        case bitwise_xor_op:
            result = PyNumber_InPlaceXor(left_obj, obj_right);
            break;
        case pow_op:
            result = PyNumber_InPlacePower(left_obj, obj_right, Py_None);
            break;
        default:
            abort();
            break;
        }

        Py_DECREF(obj_right);
        FREE_OP_VAR(1, left);
        FREE_OP_VAR(2, right);

        if (result == nullptr || result == Py_None) {
			print_error();
        }
        if (UNEXPECTED(RETURN_VALUE_USED(opline))) {
            ZVAL_COPY(EX_VAR(opline->result.var), left);
        }
        EX(opline)++;
        return ZEND_USER_OPCODE_CONTINUE;
    }
    return ZEND_USER_OPCODE_DISPATCH;
}

static int opcode_handler_bitwise_not(zend_execute_data *execute_data) {
    const zend_op *opline = EX(opline);
    zval *left;
    GET_OP_VAR(1, left);

    if (Z_TYPE_P(left) == IS_OBJECT && is_pyobject(left)) {
        PyObject *obj = phpy_object_get_handle(left);
        PyObject *result = PyNumber_Invert(obj);
        if (result == Py_None) {
        	print_error();
            Py_DECREF(result);
            ZVAL_NULL(EX_VAR(opline->result.var));
        } else {
            new_object_no_addref(EX_VAR(opline->result.var), result);
        }
        if (opline->op1_type & (IS_TMP_VAR | IS_VAR)) {
            zval_ptr_dtor(left);
        }
        EX(opline)++;
        return ZEND_USER_OPCODE_CONTINUE;
    }
    return ZEND_USER_OPCODE_DISPATCH;
}

static int opcode_handler_equal(zend_execute_data *execute_data) {
    return opcode_handler_compare_op(Py_EQ, execute_data);
}

static int opcode_handler_not_equal(zend_execute_data *execute_data) {
    return opcode_handler_compare_op(Py_NE, execute_data);
}

static int opcode_handler_smaller(zend_execute_data *execute_data) {
    return opcode_handler_compare_op(Py_LT, execute_data);
}

static int opcode_handler_smaller_or_equal(zend_execute_data *execute_data) {
    return opcode_handler_compare_op(Py_LE, execute_data);
}

int php_python_operator_init(INIT_FUNC_ARGS) {
    zend_set_user_opcode_handler(ZEND_ADD, opcode_handler_add);
    zend_set_user_opcode_handler(ZEND_SUB, opcode_handler_sub);
    zend_set_user_opcode_handler(ZEND_MUL, opcode_handler_mul);
    zend_set_user_opcode_handler(ZEND_DIV, opcode_handler_div);
    zend_set_user_opcode_handler(ZEND_MOD, opcode_handler_mod);
    zend_set_user_opcode_handler(ZEND_POW, opcode_handler_pow);

    zend_set_user_opcode_handler(ZEND_SL, opcode_handler_left_shift);
    zend_set_user_opcode_handler(ZEND_SR, opcode_handler_right_shift);
    zend_set_user_opcode_handler(ZEND_BW_AND, opcode_handler_bitwise_and);
    zend_set_user_opcode_handler(ZEND_BW_OR, opcode_handler_bitwise_or);
    zend_set_user_opcode_handler(ZEND_BW_XOR, opcode_handler_bitwise_xor);
    zend_set_user_opcode_handler(ZEND_BW_NOT, opcode_handler_bitwise_not);

    zend_set_user_opcode_handler(ZEND_ASSIGN_OP, opcode_handler_assign_op);

    zend_set_user_opcode_handler(ZEND_IS_EQUAL, opcode_handler_equal);
    zend_set_user_opcode_handler(ZEND_IS_NOT_EQUAL, opcode_handler_not_equal);
    zend_set_user_opcode_handler(ZEND_IS_SMALLER, opcode_handler_smaller);
    zend_set_user_opcode_handler(ZEND_IS_SMALLER_OR_EQUAL, opcode_handler_smaller_or_equal);

    return SUCCESS;
}
