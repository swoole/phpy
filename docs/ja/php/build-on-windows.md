# Windows での構築

> PHP-8.1 以降りのバージョンのみサポートされています。

## PHP開発環境

参考：[https://wiki.php.net/internals/windows/stepbystepbuild_sdk_2](https://wiki.php.net/internals/windows/stepbystepbuild_sdk_2)

- Visual C++ 16.0 をインストールしてください。[https://aka.ms/vs/16/release/vs_buildtools.exe](https://aka.ms/vs/16/release/vs_buildtools.exe)

- php-sdk-binary-toolsをインストールしてください。[https://github.com/php/php-sdk-binary-tools](https://github.com/php/php-sdk-binary-tools)

- PHPソースコードをダウンロードしてください。

- 依存ライブラリをインストールしてください。[https://windows.php.net/downloads/php-sdk/deps/](https://windows.php.net/downloads/php-sdk/deps/)

> PHP関連のすべてのファイルは `d:\workspace` ディレクトリにインストールされます。

## Python開発環境

- Pythonをインストールしてください。[https://www.python.org/downloads/windows/](https://www.python.org/downloads/windows/)

- `Path`環境変数を設定し、`d:\python`を追加してください。Windowsターミナルで`Python -V`を実行して確認します。

- `PYTHONHOME`環境変数を`d:\python`に設定してください。

> Pythonは`d:\python`ディレクトリにインストールされます。

```shell
C:\WINDOWS\system32>python -V
Python 3.12.1

echo %Path%
echo %PYTHONHOME%
```

## 構築ディレクトリ

```shell
cd D:\workspace\php-sdk\php-sdk-binary-tools-2.2.0
phpsdk-vs16-x64.bat
```

成功した後は、このターミナルで`php-src`ディレクトリに入ります。

```shell
cd D:\workspace\php-sdk\php-sdk-binary-tools-2.2.0\phpdev\vs16\x64\php-8.1.5
phpsdk_deps -u
```

拡張プロジェクトは`php-src`の`ext`ディレクトリに置かれます。例えば：`D:\workspace\php-sdk\php-sdk-binary-tools-2.2.0\phpdev\vs16\x64\php-8.1.5\ext\phpy`。また、`mklink`コマンドを使用してシンボリックリンクを作成することもできます。

## 構築設定

```shell
$ buildconf --force
Rebuilding configure.js
Now run 'configure --help'
configure --with-openssl --with-mysqlnd --with-mysqli --enable-mbstring --enable-pdo --with-pdo-mysql --with-curl --enable-cli --enable-opcache --disable-zts --enable-phpy=shared
```

`--enable-phpy=shared`は`phpy`拡張を有効にし、`.dll`動的リンクライブラリとしてコンパイルすることを意味します。

成功した後は、以下のような出力が得られます。

```shell
...

Generating main/config.w32.h
Generating phpize
Done.


Enabled extensions:
-----------------------
| Extension  | Mode   |
-----------------------
| date       | static |
| hash       | static |
| json       | static |
| pcre       | static |
| phpy       | shared |
| reflection | static |
| spl        | static |
| standard   | static |
-----------------------


Enabled SAPI:
-------------
| Sapi Name |
-------------
| cli       |
-------------


---------------------------------------
|                   |                 |
---------------------------------------
| Build type        | Release         |
| Thread Safety     | No              |
| Compiler          | Visual C++ 2019 |
| Architecture      | x64             |
| Optimization      | PGO disabled    |
| Native intrinsics | SSE2            |
| Static analyzer   | disabled        |
---------------------------------------


Type 'nmake' to build PHP

D:\workspace\php-sdk\php-sdk-binary-tools-2.2.0\phpdev\vs16\x64\php-8.1.5
$
```

## 拡張の構築
```shell
nmake clean
nmake
```

## 二進体のパッケージ化

```shell
nmake snap
```

成功した後は、`D:\workspace\php-sdk\php-sdk-binary-tools-2.2.0\phpdev\vs16\x64\php-8.1.5\x64\Release`に`php-8.1.5-nts-Win32-vs16-x64.zip`が生成されます。
