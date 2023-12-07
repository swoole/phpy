
# 压力测试
我们使用了 `Dict` 读写来测试 `PHP` 代码和 `Python` 代码分别执行 `1000万次`，来比较性能差异。

## PHP

```php
$dict = new PyDict();
const COUNT = 10000000;

$n = COUNT;
$s = microtime(true);
while ($n--) {
    $dict['key-' . $n] = $n * 3;
}
echo 'set from dict: ' . (microtime(true) - $s) . ' seconds' . PHP_EOL;

$c = 0;
$n = COUNT;
$s = microtime(true);
while ($n--) {
    $c += $dict['key-' . $n];
}
echo 'get from dict: ' . (microtime(true) - $s) . ' seconds' . PHP_EOL;
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

print(f"set from dict: {elapsed_time:.6f} seconds")

n = COUNT

total = 0
start_time_get = time.time()
for i in range(n):
    total += my_dict["key-" + str(i)]

elapsed_time_get = time.time() - start_time_get

print(f"get from dict: {elapsed_time_get:.6f} seconds")
```

## 结果对比

```shell
(base) htf@swoole-12:~/workspace/python-php/docs/benchmark$ python dict.py 
set from dict: 5.497841 seconds
get from dict: 5.247993 seconds
(base) htf@swoole-12:~/workspace/python-php/docs/benchmark$ php dict.php 
set from dict: 11.048210859299 seconds
get from dict: 10.532639026642 seconds
(base) htf@swoole-12:~/workspace/python-php/docs/benchmark$ 
```

`PHP` 的操作方式相比直接使用 `Python` 大约损耗了 `50%` 的性能。这里主要是`zval/PyObject`类型转换、`魔术方法` 产生的开销。

