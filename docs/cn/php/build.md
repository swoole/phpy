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

### `--with-python-config`
设置 `python-config` 可执行文件的路径， 此选项的优先级高于 `--with-python-dir` 和 `--with-python-version`

```shell
(base) htf@swoole-12:~/workspace/python-php$ which python3.11-config
/opt/anaconda3/bin/python3.11-config
(base) htf@swoole-12:~/workspace/python-php$ python3.11-config
Usage: /opt/anaconda3/bin/python3.11-config --prefix|--exec-prefix|--includes|--libs|--cflags|--ldflags|--extension-suffix|--help|--abiflags|--configdir|--embed
(base) htf@swoole-12:~/workspace/python-php$ ./configure --wi
--with-gnu-ld          --with-libdir=         --without-PACKAGE      --with-PACKAGE         --with-php-config=     --with-pic             --with-python-config   --with-python-dir      --with-python-version  --with-tags=
(base) htf@swoole-12:~/workspace/python-php$ ./configure --with-python-config=python3.11-config
checking for grep that handles long lines and -e... /bin/grep
checking for egrep... /bin/grep -E
checking for a sed that does not truncate output... /bin/sed
checking for pkg-config... /usr/bin/pkg-config
checking pkg-config is at least version 0.9.0... yes
```
