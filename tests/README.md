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
