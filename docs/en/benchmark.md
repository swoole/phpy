# Performance Testing

The performance testing script creates a `PyDict` in order to read and write code in both `PHP` and `Python` for `10 million` iterations.

- `PHP Version`: `PHP 8.2.3 (cli) (built: Mar 17 2023 15:06:57) (NTS)`
- `Python Version`: `Python 3.11.5`
- Operating System: `Ubuntu 20.04`
- `GCC Version`: `gcc version 9.4.0 (Ubuntu 9.4.0-1ubuntu1~20.04.2)`

> Please note that this test requires constructing a `10 million` element `HashTable` and requires at least `2GB` of memory to run.

## PHP

```php
<?php

$dict = new PyDict();
const COUNT = 10000000;

$n = COUNT;
$s = microtime(true);
while ($n--) {
    $dict['key-' . $n] = $n * 3;
}
echo 'dict set: ' . round(microtime(true) - $s, 6) . ' seconds' . PHP_EOL;

$c = 0;
$n = COUNT;
$s = microtime(true);
while ($n--) {
    $c += $dict['key-' . $n];
}
echo 'dict get: ' . round(microtime(true) - $s, 6) . ' seconds' . PHP_EOL;
```


## Python
```python
import time

my_dict = {}
COUNT = 10000000

n = COUNT
start_time = time.time()


for i in range(n):
    my_dict["key-" + str(i)] = i * 3

elapsed_time = time.time() - start_time

print(f"dict set: {elapsed_time:.6f} seconds")

n = COUNT

total = 0
start_time_get = time.time()
for i in range(n):
    total += my_dict["key-" + str(i)]

elapsed_time_get = time.time() - start_time_get

print(f"dict get: {elapsed_time_get:.6f} seconds")
```

## PHP Array
```php
<?php

```ini_set('memory_limit', '2G');
$dict = [];
const COUNT = 10000000;

$n = COUNT;
$s = microtime(true);
while ($n--) {
    $dict['key-' . $n] = $n * 3;
}
echo 'array set: ' . round(microtime(true) - $s, 6) . ' seconds' . PHP_EOL;

$c = 0;
$n = COUNT;
$s = microtime(true);
while ($n--) {
    $c += $dict['key-' . $n];
}
echo 'array get: ' . round(microtime(true) - $s, 6) . ' seconds' . PHP_EOL;
```

## Result Comparison

```shell
(base) htf@swoole-12:~/workspace/python-php/docs/benchmark$ php dict.php 
dict set: 4.663758 seconds
dict get: 3.980076 seconds
(base) htf@swoole-12:~/workspace/python-php/docs/benchmark$ php array.php 
array set: 1.578963 seconds
array get: 0.831129 seconds
(base) htf@swoole-12:~/workspace/python-php/docs/benchmark$ python dict.py 
dict set: 5.321664 seconds
dict get: 4.969081 seconds
(base) htf@swoole-12:~/workspace/python-php/docs/benchmark$
```

With `Python` benchmark as the baseline:

| Script Name   | Set  | 	Get |
|:----------|:----:|-----:|
| dict.php  | 114% | 125% |
| array.php | 337% | 599% |


- `phpy` performs `14%` faster in writing to `PyDict` compared to native `Python`, and `25%` faster in reading from `PyDict`.
- Writing to `PHP Array` is `237%` faster than writing to `Python Dict`, and reading from `PHP Array` is almost `500%` faster.
