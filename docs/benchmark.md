
# 压力测试
压测脚本中创建了一个 `PyDict` ，分别读写 `PHP` 代码和 `Python` 代码执行 `1000万次`。

- `PHP 版本`：`PHP 8.2.3 (cli) (built: Mar 17 2023 15:06:57) (NTS)`
- `Python 版本`：`Python 3.11.5`
- 操作系统：`Ubuntu 20.04`
- `GCC 版本`：`gcc version 9.4.0 (Ubuntu 9.4.0-1ubuntu1~20.04.2)`

> 请注意设需要构造一个 `1000` 万个元素的 `HashTable`，需要至少 `2G` 以上内存空间才可以运行此测试

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

## PHP 数组
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

## 结果对比

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

以 `Python` 测试为基准：

| 脚本名称      | Set  | 	Get |
|:----------|:----:|-----:|
| dict.php  | 114% | 125% |
| array.php | 337% | 599% |


- `phpy` 以 `PHP` 代码写入 `PyDict` 的性能比原生 `Python` 高 `14%`，读取性能高 `25%`
- `PHP` 写入 `PHP Array` 的性能比 `Python 写入 Dict` 高 `237%`，读取高出了近 `500%`
