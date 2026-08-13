# Compilation

> Currently only supports `Python 3.10` or higher.

- Modify `config.m4` to set the path of `Python`, which is `/opt/anaconda3` by default.

```shell
phpize
./configure
make install
```

Add `extension=phpy.so` to `php.ini`

Use `php -m` to check if it appears in the list. Use `php --ri phpy` to view information. Use `php --re phpy` to view the classes and methods defined in the extension.

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

Compilation parameters
----
### `--with-python-dir`

Specify the installation path of `Python`. For example, if it is `/usr/bin/python`, set it as `--with-python-dir=/usr`.
If `Python` is installed using `conda`, it should be set to `/opt/anaconda3`.

### `--with-python-version`
Specify the version of `Python`, for example, `3.10`, `3.11`, `3.12`. By default, `$python-dir/bin/python -V` will be used to get the version.

### `--with-python-config`
Set the path of the `python-config` executable. This option takes precedence over `--with-python-dir` and `--with-python-version`.

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
