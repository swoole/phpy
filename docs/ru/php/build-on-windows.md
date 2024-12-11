# компиляция под Windows

> Поддерживается только версия `PHP-8.1` и выше


## Среда разработки PHP

Ссылка: [https://wiki.php.net/internals/windows/stepbystepbuild_sdk_2](https://wiki.php.net/internals/windows/stepbystepbuild_sdk_2)



- Установите `Visual C++ 16.0`, адрес: [https://aka.ms/vs/16/release/vs_buildtools.exe](https://aka.ms/vs/16/release/vs_buildtools.exe)

- Установите `php-sdk-binary-tools`, адрес: [https://github.com/php/php-sdk-binary-tools](https://github.com/php/php-sdk-binary-tools)

- Скачать исходный код `PHP`

- Установить зависимые библиотеки, адрес: [https://windows.php.net/downloads/php-sdk/deps/](https://windows.php.net/downloads/php-sdk/deps/)

> Все файлы, связанные с `PHP`, установлены в каталоге `d:\workspace`  


## Среда разработки Python



- Установите `Python`, адрес: [https://www.python.org/downloads/windows/](https://www.python.org/downloads/windows/)

- Установите переменную окружения `Path`, добавьте `d:\python` в список, в `Windows Terminal` выполните `Python -V`

- Установите переменную окружения `PYTHONHOME`, указайте на `d:\python`

> `Python` установлен в каталоге `d:\python`

```shell
C:\WINDOWS\system32>python -V
Python 3.12.1

echo %Path%
echo %PYTHONHOME%
```



## Каталог построения

```shell
cd D:\workspace\php-sdk\php-sdk-binary-tools-2.2.0
phpsdk-vs16-x64.bat
```

После успеха перейдите в этот терминал в каталог `php-src`

```shell
cd D:\workspace\php-sdk\php-sdk-binary-tools-2.2.0\phpdev\vs16\x64\php-8.1.5
phpsdk_deps -u
```

Проекты расширений размещаются в каталоге `ext` в `php-src`, например: `D:\workspace\php-sdk\php-sdk-binary-tools-2.2.0\phpdev\vs16\x64\php-8.1.5\ext\phpy`, также можно использовать команду `mklink` для создания символической ссылки.



## Конфигурация построения

```shell
$ buildconf --force
Rebuilding configure.js
Now run 'configure --help'
configure --with-openssl --with-mysqlnd --with-mysqli --enable-mbstring --enable-pdo --with-pdo-mysql --with-curl --enable-cli --enable-opcache --disable-zts --enable-phpy=shared
```

`--enable-phpy=shared` означает включение расширения `phpy` и его сборку в `.dll` динамическую библиотеку

После успешного выполнения, вывод будет выглядеть следующим образом:

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



## Компиляция расширений
```shell
nmake clean
nmake
```

## Пакирование бинарных

```shell
nmake snap
```

После успешного выполнения в каталоге `D:\workspace\php-sdk\php-sdk-binary-tools-2.2.0\phpdev\vs16\x64\php-8.1.5\x64\Release` будет создан пакет `php-8.1.5-nts-Win32-vs16-x64.zip`.
