/* phpy extension for PHP */

#ifndef PHP_PHPY_H
# define PHP_PHPY_H

extern zend_module_entry phpy_module_entry;
# define phpext_phpy_ptr &phpy_module_entry

# define PHP_PHPY_VERSION "1.0.11"

BEGIN_EXTERN_C()
extern const char *phpy_get_python_version(void);
END_EXTERN_C()

# if defined(ZTS) && defined(COMPILE_DL_PHPY)
ZEND_TSRMLS_CACHE_EXTERN()
# endif

#endif	/* PHP_PHPY_H */
