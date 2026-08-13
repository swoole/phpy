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

## Persistent server request lifecycle

This test deliberately keeps Python carrier objects alive across two requests
handled by the same PHP built-in server process. It verifies that request-owned Zend values
are invalidated during RSHUTDOWN and that reading an expired `zend_array`
returns `null` instead of dereferencing freed memory.

It uses the current `PHP_BINARY`; no web server or FastCGI client is required:

```shell
composer test-server
```
