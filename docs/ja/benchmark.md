# ストレESSテスト
圧力テストのスクリプトでは `PyDict` を作成し、それぞれ PHP コードと Python コードで 1000 万回実行して読み書きを行います。

- `PHPバージョン`：`PHP 8.2.3 (cli) (built: Mar 17 2023 15:06:57) (NTS)`

- `Pythonバージョン`：`Python 3.11.5`

- OS：`Ubuntu 20.04`
- `GCCバージョン`：`gcc version 9.4.0 (Ubuntu 9.4.0-1ubuntu1~20.04.2)`

> このテストでは 1000 万要素の `HashTable` を構築する必要があり、少なくとも 2GB以上のメモリスペースが必要です。

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
echo 'dict set: ' . round(microtime(true) - $s, 6) . ' 秒' . PHP_EOL;

$c = 0;
$n = COUNT;
$s = microtime(true);
while ($n--) {
    $c += $dict['key-' . $n];
}
echo 'dict get: ' . round(microtime(true) - $s, 6) . ' 秒' . PHP_EOL;
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

print(f"dict set: {elapsed_time:.6f} 秒")

n = COUNT

total = 0
start_time_get = time.time()
for i in range(n):
    total += my_dict["key-" + str(i)]

elapsed_time_get = time.time() - start_time_get

print(f"dict get: {elapsed_time_get:.6f} 秒")
```

## PHP 配列
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
echo 'array set: ' . round(microtime(true) - $s, 6) . ' 秒' . PHP_EOL;

$c = 0;
$n = COUNT;
$s = microtime(true);
while ($n--) {
    $c += $dict['key-' . $n];
}
echo 'array get: ' . round(microtime(true) - $s, 6) . ' 秒' . PHP_EOL;
```

##結果の比較

```shell
(base) htf@swoole-12:~/workspace/python-php/docs/benchmark$ php dict.php 
dict set: 4.663758 秒
dict get: 3.980076 秒
(base) htf@swoole-12:~/workspace/python-php/docs/benchmark$ php array.php 
array set: 1.578963 秒
array get: 0.831129 秒
(base) htf@swoole-12:~/workspace/python-php/docs/benchmark$ python dict.py 
dict set: 5.321664 秒
dict get: 4.969081 秒
(base) htf@swoole-12:~/workspace/python-php/docs/benchmark$
```

Pythonテストを基準に：

| スクリプト名 | Set  | Get |
|:----------|:----:|-----:|
| dict.php  | 114% | 125% |
| array.php | 337% | 599% |

- `phpy`はPHPコードでPyDictを書くパフォーマンスが原生Pythonの14%高く、読み取りのパフォーマンスは25%高い
- PHPで書く配列のパフォーマンスはPythonのDictを書くパフォーマンスの237%高く、読み取りはほぼ500%高い
