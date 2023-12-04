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

BEGIN_EXTERN_C()
#include "stubs/{{project_name}}_{{class_name_lower}}_arginfo.h"
END_EXTERN_C()

zend_class_entry *{{project_name}}_{{module_name}}_ce;
static zend_object_handlers object_handlers;

struct {{type_name}} {
    {{class_name}} *{{var_name}};
    zend_object std;
};

static zend_always_inline {{class_name}} *{{project_name}}_{{module_name}}_get_handle(zend_object *object) {
    return (({{type_name}} *) ((char *) object - object_handlers.offset))->{{var_name}};
}

static zend_always_inline {{type_name}} *{{project_name}}_{{module_name}}_get_object(zend_object *object) {
    return ({{type_name}} *) ((char *) object - object_handlers.offset);
}

static zend_always_inline {{class_name}} *{{project_name}}_{{module_name}}_get_handle(zval *zobject) {
    return (({{type_name}} *) ((char *) Z_OBJ_P(zobject) - object_handlers.offset))->{{var_name}};
}

static zend_always_inline {{type_name}} *{{project_name}}_{{module_name}}_get_object(zval *zobject) {
    return ({{type_name}} *) ((char *) Z_OBJ_P(zobject) - object_handlers.offset);
}

static zend_always_inline {{type_name}} *{{project_name}}_{{module_name}}_get_object_safe(zval *zobject) {
    {{class_name}} *{{var_name}} = {{project_name}}_{{module_name}}_get_handle(zobject);
    if (!{{var_name}}) {
        php_error(E_ERROR, "must call {{module_name}} constructor first");
    }
    return {{project_name}}_{{module_name}}_get_object(zobject);
}

static zend_always_inline {{type_name}} *{{project_name}}_{{module_name}}_get_object_safe(zend_object *object) {
    {{class_name}} *{{var_name}} = {{project_name}}_{{module_name}}_get_handle(object);
    if (!{{var_name}}) {
        php_error(E_ERROR, "must call {{module_name}} constructor first");
    }
    return {{project_name}}_{{module_name}}_get_object(object);
}

static zend_object *{{project_name}}_{{module_name}}_create_object(zend_class_entry *ce) {
    {{type_name}} *{{php_var_name}} = ({{type_name}} *) zend_object_alloc(sizeof(*{{php_var_name}}), ce);

    zend_object_std_init(&{{php_var_name}}->std, ce);
    object_properties_init(&{{php_var_name}}->std, ce);
    {{php_var_name}}->std.handlers = &object_handlers;
    {{php_var_name}}->{{var_name}} = new {{class_name}};

    return &{{php_var_name}}->std;
}

static void {{project_name}}_{{module_name}}_free_object(zend_object *object) {
    {{type_name}} *{{php_var_name}} = {{project_name}}_{{module_name}}_get_object(object);
    zend_object_std_dtor(&{{php_var_name}}->std);
}

int php_class_{{module_name}}_init(INIT_FUNC_ARGS) {
    zend_class_entry ce;
	INIT_CLASS_ENTRY(ce, "{{class_name}}", class_{{project_name}}_{{class_name}}_methods);
	{{project_name}}_{{module_name}}_ce = zend_register_internal_class_ex(&ce, NULL);
	{{project_name}}_{{module_name}}_ce->ce_flags |= ZEND_ACC_FINAL|ZEND_ACC_NO_DYNAMIC_PROPERTIES|ZEND_ACC_NOT_SERIALIZABLE;

	{{project_name}}_{{module_name}}_ce->create_object = {{project_name}}_{{module_name}}_create_object;

	memcpy(&object_handlers, &std_object_handlers, sizeof(zend_object_handlers));
	object_handlers.offset = XtOffsetOf({{type_name}}, std);
	object_handlers.free_obj = {{project_name}}_{{module_name}}_free_object;

    return SUCCESS;
}
