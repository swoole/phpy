## phpunit
```shell
vendor/bin/phpunit --bootstrap tests/bootstrap.php -c phpunit.xml --colors=always --filter="ZendTest::testCallMethodInPython"
vendor/bin/phpunit --bootstrap tests/bootstrap.php -c phpunit.xml --colors=always
```

## pytest
```shell
pip install pytest
pytest -v tests/
pytest -v tests/test_array.py
```

## PHP-FPM request lifecycle

This test deliberately keeps Python carrier objects alive across two requests
handled by the same PHP-FPM worker. It verifies that request-owned Zend values
are invalidated during RSHUTDOWN and that reading an expired `zend_array`
returns `null` instead of dereferencing freed memory.

It requires `php-fpm` and `cgi-fcgi`. Override their locations when they are
not installed in the standard system paths:

```shell
PHP_FPM_BINARY=/usr/sbin/php-fpm8.4 \
CGI_FCGI_BINARY=/usr/bin/cgi-fcgi \
composer test-fpm
```
