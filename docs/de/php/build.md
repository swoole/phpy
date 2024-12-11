# Linux/macOS/Unix-Kompilierung

> Derzeit werden nur Python 3.10 oder höher unterstützt.

- Ändern Sie in `config.m4` den Pfad für `Python`, der Default ist: `/opt/anaconda3`

```shell
phpize
./configure
make install
```

Fügen Sie in `php.ini` `extension=phpy.so` hinzu.
Verwenden Sie `php -m`, um zu sehen, ob es in der Liste erscheint. Sie können auch `php --ri phpy` verwenden, um Informationen anzuzeigen, und `php --re phpy`, um die von der Erweiterung definierte Klassen und Methoden zu sehen.

```shell
php -m
----
```
```shell
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

Kompilierungsoptionen
----

### `--with-python-dir`

Geben Sie den Installationspfad für `Python` an, zum Beispiel sollte `/usr/bin/python` mit `--with-python-dir=/usr` festgelegt werden.
Wenn Sie `Python` mit `conda` installiert haben, sollte es mit `/opt/anaconda3` festgelegt werden.

### `--with-python-version`
Geben Sie die Version von `Python` an, zum Beispiel `3.10`, `3.11`, `3.12`. Der Default verwendet `$python-dir/bin/python -V`, um die Version zu ermitteln.

### `--with-python-config`
Setzen Sie den Pfad für das `python-config` Executable fest. Diese Option hat Vorrang vor `--with-python-dir` und `--with-python-version`.

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
