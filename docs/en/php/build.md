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
(base) htf@swoole-12:~/workspace/python-php$ ./configure --wi--with-gnu-ld: This option indicates that the GNU linker should be used.
--with-libdir=: This option is used to specify the directory where the libraries are located.
--without-PACKAGE: This option is used to specify that a particular package should not be included.
--with-PACKAGE: This option is used to specify that a particular package should be included.
--with-php-config=: This option is used to specify the location of the PHP configuration script.
--with-pic: This option is used to enable position-independent code generation.
--with-python-config: This option is used to specify the location of the Python configuration script.
--with-python-dir: This option is used to specify the directory where the Python libraries are located.
--with-python-version: This option is used to specify the version of Python to use.
--with-tags=: This option is used to specify additional tags.
