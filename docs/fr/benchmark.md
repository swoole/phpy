# Test de charge
Un script de test de charge a créé un `PyDict`, écrivant et lisant des codes `PHP` et `Python` pour exécuter `10 millions` d'opérations.

- `Version PHP` : `PHP 8.2.3 (cli) (built: Mar 17 2023 15:06:57) (NTS)`

- `Version Python` : `Python 3.11.5`

- Système d'exploitation : `Ubuntu 20.04`
- `Version GCC` : `gcc version 9.4.0 (Ubuntu 9.4.0-1ubuntu1~20.04.2)`

> Veuillez noter que ce test nécessite la construction d'un `HashTable` de `10 millions` d'éléments, nécessitant au moins `2 Go` de mémoire pour fonctionner

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
echo 'dict set: ' . round(microtime(true) - $s, 6) . ' secondes' . PHP_EOL;

$c = 0;
$n = COUNT;
$s = microtime(true);
while ($n--) {
    $c += $dict['key-' . $n];
}
echo 'dict get: ' . round(microtime(true) - $s, 6) . ' secondes' . PHP_EOL;
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
echo 'array set: ' . round(microtime(true) - $s, 6) . ' secondes' . PHP_EOL;

$c = 0;
$n = COUNT;
$s = microtime(true);
while ($n--) {
    $c += $dict['key-' . $n];
}
echo 'array get: ' . round(microtime(true) - $s, 6) . ' secondes' . PHP_EOL;
```

## Résultats comparatifs

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

En utilisant le test Python comme référence :

| Nom du script | Set  | Get |
|:----------|:----:|-----:|
| dict.php  | 114% | 125% |
| array.php | 337% | 599% |

- `phpy` écrit dans `PyDict` avec du code PHP avec une performance `14%` supérieure à celle du Python原生, et une performance de lecture `25%` supérieure.
- L'écriture dans `PHP Array` est `237%` plus rapide que l'écriture dans `Python Dict`, et la lecture est presque `500%` plus rapide.
