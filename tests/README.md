## phpunit
```shell
vendor/bin/phpunit --bootstrap tests/bootstrap.php -c phpunit.xml --colors=always --filter="ZendTest::testCallMethodInPython"
vendor/bin/phpunit --bootstrap tests/bootstrap.php -c phpunit.xml --colors=always
```

## Native PHP compatibility tests

The PHPT tests use the extension build's PHP runtime and do not require Composer.
To build and run them with the local PHP 7.4 toolchain:

```shell
phpize-74
./configure --enable-phpy --with-php-config="$(command -v php-config-74)"
make
NO_INTERACTION=1 REPORT_EXIT_STATUS=1 make test TESTS=tests/phpt
```

Use the same `make test` command in a build configured for PHP 8 to check both Zend API branches.

## pytest
```shell
pip install pytest
pytest -v tests/
pytest -v tests/test_array.py
```

## Persistent server request lifecycle

This test deliberately keeps Python carrier objects alive across two requests
handled by the same PHP built-in server process. It verifies that request-owned Zend values
are invalidated during RSHUTDOWN and that reading an expired `zend_array`
returns `null` instead of dereferencing freed memory.

It uses the current `PHP_BINARY`; no web server or FastCGI client is required:

```shell
composer test-server
```
