# Windows Compilation

> Only supports `PHP-8.1` or higher


## PHP Development Environment

Refer to: [https://wiki.php.net/internals/windows/stepbystepbuild_sdk_2](https://wiki.php.net/internals/windows/stepbystepbuild_sdk_2)



- Install `Visual C++ 16.0`, address: [https://aka.ms/vs/16/release/vs_buildtools.exe](https://aka.ms/vs/16/release/vs_buildtools.exe)

- Install `php-sdk-binary-tools`, address: [https://github.com/php/php-sdk-binary-tools](https://github.com/php/php-sdk-binary-tools)

- Download `php` source code
- Install dependency libraries, address: [https://windows.php.net/downloads/php-sdk/deps/](https://windows.php.net/downloads/php-sdk/deps/)

> All files related to `PHP` are installed in the `d:\workspace` directory  


## Python Development Environment



- Install `Python`, address: [https://www.python.org/downloads/windows/](https://www.python.org/downloads/windows/)

- Set `Path` environment variable, add `d:\python` to the list, execute `Python -V` in `Windows Terminal`
- Set `PYTHONHOME` environment variable, pointing to `d:\python`

> `Python` is installed in the `d:\python` directory

```shell
C:\WINDOWS\system32>python -V
Python 3.12.1

echo %Path%
echo %PYTHONHOME%
```



## Build Directory

```shell
cd D:\workspace\php-sdk\php-sdk-binary-tools-2.2.0
phpsdk-vs16-x64.bat
```

After successful execution, enter the `php-src` directory in this terminal

```shell
cd D:\workspace\php-sdk\php-sdk-binary-tools-2.2.0\phpdev\vs16\x64\php-8.1.5
phpsdk_deps -u
```

Place extension projects in the `ext` directory of `php-src`, for example: `D:\workspace\php-sdk\php-sdk-binary-tools-2.2.0\phpdev\vs16\x64\php-8.1.5\ext\phpy`. You can also use the `mklink` command to create a symbolic link.



## Compilation Configuration

```shell
$ buildconf --force
Rebuilding configure.js
Now run 'configure --help'
configure --with-openssl --with-mysqlnd --with-mysqli --enable-mbstring --enable-pdo --with-pdo-mysql --with-curl --enable-cli --enable-opcache --disable-zts --enable-phpy=shared
```

`--enable-phpy=shared` indicates enabling the `phpy` extension and compiling it into a `.dll` dynamic link library.

After successful execution, the output:

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



## Compile Extensions
```shell
nmake clean
nmake
```

## Binary Packaging

```shell
nmake snap
```

After successful execution, `php-8.1.5-nts-Win32-vs16-x64.zip` will be generated in `D:\workspace\php-sdk\php-sdk-binary-tools-2.2.0\phpdev\vs16\x64\php-8.1.5\x64\Release`.
