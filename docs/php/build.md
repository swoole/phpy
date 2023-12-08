# 编译

> 目前仅支持 `Python 3.10` 或更高版本

- 修改 `config.m4` 设置 `Python` 的路径，默认为：`/opt/anaconda3`


```shell
phpize
./configure
make install
```

设置 `php.ini` 增加 `extension=phpy.so`

使用 `php -m` 查看是否出现在列表中，可使用 `php --ri phpy` 查看信息，使用 `php --re phpy` 查看扩展中定义的类和方法。

php -m
----
```
php -m
[PHP Modules]
bcmath
bz2
Core
...
phpy
...

[Zend Modules]
Zend OPcache
```

编译参数
----
### `--with-python-dir`

指定 `Python` 的安装路径，例如 `/usr/bin/python` 应该设置为 `--with-python-dir=/usr`。
若使用 `conda` 安装 `Python`，应设置为 `/opt/anaconda3`

### `--with-python-version`
指定 `Python` 的版本，例如 `3.10`、`3.11`、`3.12`，默认将使用 `$python-dir/bin/python -V` 来获取版本。



