# Сборка для Linux/macOS/Unix

> В настоящее время поддерживается только версия `Python 3.10` или выше.


- Измените путь к `Python` в `config.m4`, по умолчанию: `/opt/anaconda3`


```shell
phpize
./configure
make install
```

Измените `php.ini`, чтобы добавить `extension=phpy.so`

Используйте `php -m` чтобы проверить, появляется ли в списке, используйте `php --ri phpy` чтобы узнать информацию, используйте `php --re phpy` чтобы посмотреть классы и методы, определенные в расширении.


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


Параметры сборки
----

### `--with-python-dir`

Указать путь к установке `Python`, например, `/usr/bin/python` должен быть установлен как `--with-python-dir=/usr`
Если использовать `conda` для установки `Python`, следует установить как `/opt/anaconda3`


### `--with-python-version`
Указать версию `Python`, например, `3.10`, `3.11`, `3.12`, по умолчанию будет использоваться `$python-dir/bin/python -V` для получения версии.

### `--with-python-config`
Установить путь кExecutable `python-config`, этот параметр имеет более высокий приоритет, чем `--with-python-dir` и `--with-python-version`

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
