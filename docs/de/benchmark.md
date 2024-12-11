# Stresstest
In einem Stresstest-Skript wurde ein `PyDict` angelegt, um sowohl PHP- als auch Python-Code für die Ausführung von `10 Millionen` Mal zu lesen und zu schreiben.

- `PHP-Version`: `PHP 8.2.3 (cli) (built: Mar 17 2023 15:06:57) (NTS)`

- `Python-Version`: `Python 3.11.5`

- Betriebssystem: `Ubuntu 20.04`
- `GCC-Version`: `gcc version 9.4.0 (Ubuntu 9.4.0-1ubuntu1~20.04.2)`

> Bitte beachten Sie, dass dieser Test eine `10 Millionen` Elemente umfassende `HashTable` benötigen und mindestens `2GB` an Arbeitsspeicher für die Ausführung benötigen kann.

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
echo 'dict set: ' . round(microtime(true) - $s, 6) . ' Sekunden' . PHP_EOL;

$c = 0;
$n = COUNT;
$s = microtime(true);
while ($n--) {
    $c += $dict['key-' . $n];
}
echo 'dict get: ' . round(microtime(true) - $s, 6) . ' Sekunden' . PHP_EOL;
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

ini_set('memory_limit', '2G');
$dict = [];
const COUNT = 10000000;

$n = COUNT;
$s = microtime(true);
while ($n--) {
    $dict['key-' . $n] = $n * 3;
}
echo 'array set: ' . round(microtime(true) - $s, 6) . ' Sekunden' . PHP_EOL;

$c = 0;
$n = COUNT;
$s = microtime(true);
while ($n--) {
    $c += $dict['key-' . $n];
}
echo 'array get: ' . round(microtime(true) - $s, 6) . ' Sekunden' . PHP_EOL;
```

## Ergebnisvergleich

```shell
(base) htf@swoole-12:~/workspace/python-php/docs/benchmark$ php dict.php 
dict set: 4.663758 Sekunden
dict get: 3.980076 Sekunden
(base) htf@swoole-12:~/workspace/python-php/docs/benchmark$ php array.php 
array set: 1.578963 Sekunden
array get: 0.831129 Sekunden
(base) htf@swoole-12:~/workspace/python-php/docs/benchmark$ python dict.py 
dict set: 5.321664 Sekunden
dict get: 4.969081 Sekunden
(base) htf@swoole-12:~/workspace/python-php/docs/benchmark$
```

Mit dem `Python` Test als Basis:

| Scriptname | Set | Get |
|:----------|:----:|-----:|
| dict.php  | 114% | 125% |
| array.php | 337% | 599% |

- `phpy` schreibt PHP-Code in `PyDict` mit einer Leistung, die 14% höher ist als die native Python-Leistung und 25% höher für das Lesen.
- Die Leistung von PHP beim Schreiben in ein PHP-Array ist 237% höher als die Leistung von Python beim Schreiben in ein Dict und fast 500% höher für das Lesen.
