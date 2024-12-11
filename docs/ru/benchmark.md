# Тестирование под нагрузкой
В скрипте нагрузочного тестирования был создан объект `PyDict`, который использовался для чтения и写入 `PHP`-кода и `Python`-кода, выполняя операции `10 миллионов` раз.

- `Версия PHP`: `PHP 8.2.3 (cli) (built: Mar 17 2023 15:06:57) (NTS)`

- `Версия Python`: `Python 3.11.5`

- операционная система: `Ubuntu 20.04`
- `Версия GCC`: `gcc version 9.4.0 (Ubuntu 9.4.0-1ubuntu1~20.04.2)`

> Обратите внимание, что для выполнения этого теста необходимо создать `HashTable` из `10 миллионов` элементов, что требует не менее `2 ГБ` памяти.

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

## PHP массив
```php
<?php

ini_set('memory_limit', '2G');
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

## Сравнение результатов

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

На основе результатов тестирования на `Python`:

| Название скрипта | Set  | Get |
|:----------|:----:|-----:|
| dict.php  | 114% | 125% |
| array.php | 337% | 599% |

- `phpy` показывает производительность в `PHP`, когда данные写入 `PyDict`, на `14%` выше, чем у нативного `Python`, а при чтении на `25%` выше.
- `PHP` показывает производительность при написании данных в `PHP Array` в `337%` выше, чем при написании в `Python Dict`, а при чтении в почти `500%` выше.
