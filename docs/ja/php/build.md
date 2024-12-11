# Linux/macOS/Unixでのコンパイル

> 現在は `Python 3.10` 以降のバージョンのみサポートされています


- `config.m4` を編集して `Python` のパスを設定します。デフォルトは `/opt/anaconda3`です。


```shell
phpize
./configure
make install
```

`php.ini` を編集して `extension=phpy.so`を追加します。

`php -m` を実行してリストに表示されているかどうかを確認します。`php --ri phpy` を実行して情報查看し、`php --re phpy` を実行して拡張機能で定義されているクラスや方法を查看します。


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


コンパイルパラメータ
----

### `--with-python-dir`

`Python` のインストールパスを指定します。例えば `/usr/bin/python` の場合は `--with-python-dir=/usr`と設定します。
`conda`で `Python` をインストールした場合は `/opt/anaconda3`と設定します。


### `--with-python-version`

指定する `Python`のバージョンです。例えば `3.10`、`3.11`、`3.12`などです。デフォルトでは `$python-dir/bin/python -V`を使用してバージョンを取得します。

### `--with-python-config`

`python-config`実行文件的路径を設定します。このオプションの優先度は `--with-python-dir`や `--with-python-version`よりも高いです。

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
