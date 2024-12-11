# Compilation pour Linux/macOS/Unix

> Actuellement, seule la version `Python 3.10` ou supérieure est prise en charge.

- Modifiez `config.m4` pour configurer le chemin de `Python`, par défaut : `/opt/anaconda3`

```shell
phpize
./configure
make install
```

Modifiez `php.ini` pour ajouter `extension=phpy.so`

Utilisez `php -m` pour vérifier si elle apparaît dans la liste, utilisez `php --ri phpy` pour voir les informations, utilisez `php --re phpy` pour voir les classes et méthodes définies dans l'extension.

```shell
php -m
----
```
php -m
[Modules PHP]
bcmath
bz2
Core
...
phpy
...

[Modules Zend]
Zend OPcache
```

Paramètres de compilation
----

### `--with-python-dir`

Spécifiez le chemin d'installation de `Python`, par exemple `/usr/bin/python` devrait être configuré en `--with-python-dir=/usr`.
Si vous utilisez `conda` pour installer `Python`, il devrait être configuré en `/opt/anaconda3`.

### `--with-python-version`

Spécifiez la version de `Python`, par exemple `3.10`, `3.11`, `3.12`, la version par défaut sera obtenue en utilisant `$python-dir/bin/python -V`.

### `--with-python-config`

Configurez le chemin de l'exécutable `python-config`, cette option a un niveau de priorité supérieur à `--with-python-dir` et `--with-python-version`.

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
