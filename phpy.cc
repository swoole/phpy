/* phpy extension for PHP */

#ifdef HAVE_CONFIG_H
# include "config.h"
#endif

#include "php.h"
#include "ext/standard/info.h"
#include "php_phpy.h"

/* {{{ PHP_RINIT_FUNCTION */
PHP_RINIT_FUNCTION(phpy)
{
#if defined(ZTS) && defined(COMPILE_DL_PHPY)
	ZEND_TSRMLS_CACHE_UPDATE();
#endif

	return SUCCESS;
}
/* }}} */

extern PHP_MINIT_FUNCTION(phpy);
extern PHP_MSHUTDOWN_FUNCTION(phpy);
extern PHP_RSHUTDOWN_FUNCTION(phpy);

/* {{{ PHP_MINFO_FUNCTION */
PHP_MINFO_FUNCTION(phpy)
{
    php_info_print_table_start();
    php_info_print_table_header(2, "phpy support", "enabled");
    php_info_print_table_row(2, "Copyright", "上海识沃网络科技有限公司");
    php_info_print_table_row(2, "Email", "service@swoole.com");
    php_info_print_table_row(2, "Website", "https://www.swoole.com/");
    php_info_print_table_row(2, "Extension Version", PHP_PHPY_VERSION);
    php_info_print_table_row(2, "Python Version", phpy_get_python_version());
    php_info_print_table_end();
}
/* }}} */

/* {{{ phpy_module_entry */
zend_module_entry phpy_module_entry = {
	STANDARD_MODULE_HEADER,
	"phpy",					    /* Extension name */
	NULL,					    /* zend_function_entry */
	PHP_MINIT(phpy),		    /* PHP_MINIT - Module initialization */
	PHP_MSHUTDOWN(phpy),		/* PHP_MSHUTDOWN - Module shutdown */
	PHP_RINIT(phpy),			/* PHP_RINIT - Request initialization */
	PHP_RSHUTDOWN(phpy),    	/* PHP_RSHUTDOWN - Request shutdown */
	PHP_MINFO(phpy),			/* PHP_MINFO - Module info */
	PHP_PHPY_VERSION,		    /* Version */
	STANDARD_MODULE_PROPERTIES
};
/* }}} */

#ifdef COMPILE_DL_PHPY
# ifdef ZTS
ZEND_TSRMLS_CACHE_DEFINE()
# endif
ZEND_GET_MODULE(phpy)
#endif
