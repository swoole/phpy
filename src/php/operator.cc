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
using phpy::python::LockGuard;
using phpy::python::OwnedPythonReference;

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

static int opcode_handler_number_op(NumberProtocolFn fn, zend_execute_data *execute_data) {
    const zend_op *opline = EX(opline);
    zval *left, *right;
    GET_OP_VAR(1, left);
    GET_OP_VAR(2, right);

    OwnedPythonReference result;
    LOCK_GIL();

    if (Z_TYPE_P(left) == IS_OBJECT && is_pyobject(left)) {
        PyObject *obj = phpy_object_get_handle(left);
        OwnedPythonReference obj_right(php2py(right));
        if (obj_right) {
            result = OwnedPythonReference(fn(obj, obj_right.get()));
        }
    } else if (Z_TYPE_P(right) == IS_OBJECT && is_pyobject(right)) {
        PyObject *obj = phpy_object_get_handle(right);
        OwnedPythonReference obj_left(php2py(left));
        if (obj_left) {
            result = OwnedPythonReference(fn(obj_left.get(), obj));
        }
    }

    // The `result` must be a new reference.
    if (result) {
        if (result.get() == Py_None && !phpy_options.return_as_object) {
            ZVAL_NULL(EX_VAR(opline->result.var));
        } else {
            new_object_no_addref(EX_VAR(opline->result.var), result.release());
        }
        FREE_OP_VAR(1, left);
        FREE_OP_VAR(2, right);
        EX(opline)++;
        return ZEND_USER_OPCODE_CONTINUE;
    }

    if (PyErr_Occurred()) {
        throw_error_if_occurred();
        ZVAL_NULL(EX_VAR(opline->result.var));
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

    LOCK_GIL();
    bool is_pyobj = false;
    int result;

    if (Z_TYPE_P(left) == IS_OBJECT && is_pyobject(left)) {
        PyObject *obj_left = phpy_object_get_handle(left);
        OwnedPythonReference obj_right(php2py(right));
        result = obj_right ? PyObject_RichCompareBool(obj_left, obj_right.get(), op) : -1;
        is_pyobj = true;
    } else if (Z_TYPE_P(right) == IS_OBJECT && is_pyobject(right)) {
        PyObject *obj_right = phpy_object_get_handle(right);
        OwnedPythonReference obj_left(php2py(left));
        result = obj_left ? PyObject_RichCompareBool(obj_left.get(), obj_right, op) : -1;
        is_pyobj = true;
    }

    if (is_pyobj) {
        if (result == -1) {
            throw_error_if_occurred();
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

static int opcode_handler_identity_op(bool negate, zend_execute_data *execute_data) {
    const zend_op *opline = EX(opline);
    zval *left, *right;
    GET_OP_VAR(1, left);
    GET_OP_VAR(2, right);

    const bool left_is_python = Z_TYPE_P(left) == IS_OBJECT && is_pyobject(left);
    const bool right_is_python = Z_TYPE_P(right) == IS_OBJECT && is_pyobject(right);
    if (!left_is_python && !right_is_python) {
        return ZEND_USER_OPCODE_DISPATCH;
    }

    LOCK_GIL();
    OwnedPythonReference converted_left;
    OwnedPythonReference converted_right;
    PyObject *left_object;
    PyObject *right_object;

    if (left_is_python) {
        left_object = phpy_object_get_handle(left);
    } else {
        converted_left = OwnedPythonReference(php2py(left));
        left_object = converted_left.get();
    }
    if (right_is_python) {
        right_object = phpy_object_get_handle(right);
    } else {
        converted_right = OwnedPythonReference(php2py(right));
        right_object = converted_right.get();
    }

    if (UNEXPECTED(left_object == nullptr || right_object == nullptr)) {
        throw_error_if_occurred();
        ZVAL_FALSE(EX_VAR(opline->result.var));
    } else {
        const bool identical = left_object == right_object;
        ZVAL_BOOL(EX_VAR(opline->result.var), negate ? !identical : identical);
    }

    FREE_OP_VAR(1, left);
    FREE_OP_VAR(2, right);
    EX(opline)++;
    return ZEND_USER_OPCODE_CONTINUE;
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
    return opcode_handler_number_op(PyNumber_TrueDivide, execute_data);
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
    LOCK_GIL();

    if (Z_TYPE_P(left) == IS_OBJECT && is_pyobject(left)) {
        // See: zend_binary_op
        size_t opcode = (size_t) opline->extended_value - ZEND_ADD;
        PyObject *left_obj = phpy_object_get_handle(left);
        zval *right;
        GET_OP_VAR(2, right);
        OwnedPythonReference obj_right(php2py(right));
        if (!obj_right) {
            throw_error_if_occurred();
            if (UNEXPECTED(RETURN_VALUE_USED(opline))) {
                ZVAL_NULL(EX_VAR(opline->result.var));
            }
            FREE_OP_VAR(1, left);
            FREE_OP_VAR(2, right);
            EX(opline)++;
            return ZEND_USER_OPCODE_CONTINUE;
        }

        OwnedPythonReference result;

        switch (opcode) {
        case add_op:
            result = OwnedPythonReference(PyNumber_InPlaceAdd(left_obj, obj_right.get()));
            break;
        case sub_op:
            result = OwnedPythonReference(PyNumber_InPlaceSubtract(left_obj, obj_right.get()));
            break;
        case mul_op:
            result = OwnedPythonReference(PyNumber_InPlaceMultiply(left_obj, obj_right.get()));
            break;
        case div_op:
            result = OwnedPythonReference(PyNumber_InPlaceTrueDivide(left_obj, obj_right.get()));
            break;
        case mod_op:
            result = OwnedPythonReference(PyNumber_InPlaceRemainder(left_obj, obj_right.get()));
            break;
        case shift_left_op:
            result = OwnedPythonReference(PyNumber_InPlaceLshift(left_obj, obj_right.get()));
            break;
        case shift_right_op:
            result = OwnedPythonReference(PyNumber_InPlaceRshift(left_obj, obj_right.get()));
            break;
        case concat_op:
            zend_error(E_WARNING, "PyObject do not support string concat operation");
            break;
        case bitwise_or_op:
            result = OwnedPythonReference(PyNumber_InPlaceOr(left_obj, obj_right.get()));
            break;
        case bitwise_and_op:
            result = OwnedPythonReference(PyNumber_InPlaceAnd(left_obj, obj_right.get()));
            break;
        case bitwise_xor_op:
            result = OwnedPythonReference(PyNumber_InPlaceXor(left_obj, obj_right.get()));
            break;
        case pow_op:
            result = OwnedPythonReference(PyNumber_InPlacePower(left_obj, obj_right.get(), Py_None));
            break;
        default:
            abort();
            break;
        }

        if (!result) {
            throw_error_if_occurred();
            if (UNEXPECTED(RETURN_VALUE_USED(opline))) {
                ZVAL_NULL(EX_VAR(opline->result.var));
            }
        } else {
            zval replacement;
            if (result.get() == Py_None && !phpy_options.return_as_object) {
                ZVAL_NULL(&replacement);
            } else {
                ZVAL_UNDEF(&replacement);
                new_object_no_addref(&replacement, result.release());
            }
            zval_ptr_dtor(left);
            ZVAL_COPY_VALUE(left, &replacement);
            if (UNEXPECTED(RETURN_VALUE_USED(opline))) {
                ZVAL_COPY(EX_VAR(opline->result.var), left);
            }
        }
        FREE_OP_VAR(1, left);
        FREE_OP_VAR(2, right);
        EX(opline)++;
        return ZEND_USER_OPCODE_CONTINUE;
    }
    return ZEND_USER_OPCODE_DISPATCH;
}

static int opcode_handler_bitwise_not(zend_execute_data *execute_data) {
    const zend_op *opline = EX(opline);
    zval *left;
    GET_OP_VAR(1, left);
    LOCK_GIL();

    if (Z_TYPE_P(left) == IS_OBJECT && is_pyobject(left)) {
        PyObject *obj = phpy_object_get_handle(left);
        OwnedPythonReference result(PyNumber_Invert(obj));
        if (!result) {
            throw_error_if_occurred();
            ZVAL_NULL(EX_VAR(opline->result.var));
        } else if (result.get() == Py_None && !phpy_options.return_as_object) {
            ZVAL_NULL(EX_VAR(opline->result.var));
        } else {
            new_object_no_addref(EX_VAR(opline->result.var), result.release());
        }
        FREE_OP_VAR(1, left);
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

static int opcode_handler_identical(zend_execute_data *execute_data) {
    return opcode_handler_identity_op(false, execute_data);
}

static int opcode_handler_not_identical(zend_execute_data *execute_data) {
    return opcode_handler_identity_op(true, execute_data);
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
    zend_set_user_opcode_handler(ZEND_IS_IDENTICAL, opcode_handler_identical);
    zend_set_user_opcode_handler(ZEND_IS_NOT_IDENTICAL, opcode_handler_not_identical);
    zend_set_user_opcode_handler(ZEND_IS_SMALLER, opcode_handler_smaller);
    zend_set_user_opcode_handler(ZEND_IS_SMALLER_OR_EQUAL, opcode_handler_smaller_or_equal);

    return SUCCESS;
}
