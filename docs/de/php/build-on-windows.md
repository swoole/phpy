# Windows-Kompilierung

> Unterstützt nur PHP-Versionen ab 8.1


## PHP-Entwicklungsumgebung

Referenz: [https://wiki.php.net/internals/windows/stepbystepbuild_sdk_2](https://wiki.php.net/internals/windows/stepbystepbuild_sdk_2)



- Installieren Sie `Visual C++ 16.0`, Adresse: [https://aka.ms/vs/16/release/vs_buildtools.exe](https://aka.ms/vs/16/release/vs_buildtools.exe)

- Installieren Sie `php-sdk-binary-tools`, Adresse: [https://github.com/php/php-sdk-binary-tools](https://github.com/php/php-sdk-binary-tools)

- Herunterladen Sie die `php`-Quellcode

- Installieren Sie die Abhängigkeiten, Adresse: [https://windows.php.net/downloads/php-sdk/deps/](https://windows.php.net/downloads/php-sdk/deps/)

> Alle `PHP`-相关的 Dateien werden in dem Verzeichnis `d:\workspace` installiert  


## Python-Entwicklungsumgebung



- Installieren Sie `Python`, Adresse: [https://www.python.org/downloads/windows/](https://www.python.org/downloads/windows/)

- Legen Sie die `Path`-Umweltvariablen fest, fügen Sie `d:\python` hinzu, und führen Sie in der `Windows-Terminal` `Python -V` durch

- Legen Sie die `PYTHONHOME`-Umweltvariablen fest, zeigen Sie auf `d:\python`

> `Python` wird im Verzeichnis `d:\python` installiert

```shell
C:\WINDOWS\system32>python -V
Python 3.12.1

echo %Path%
echo %PYTHONHOME%
```



## Build-Verzeichnis

```shell
cd D:\workspace\php-sdk\php-sdk-binary-tools-2.2.0
phpsdk-vs16-x64.bat
```

Nach dem Erfolg betreten Sie diesen Terminal und wechseln Sie in das Verzeichnis `php-src`

```shell
cd D:\workspace\php-sdk\php-sdk-binary-tools-2.2.0\phpdev\vs16\x64\php-8.1.5
phpsdk_deps -u
```

Erweiterungsprojekte werden im `ext` Verzeichnis von `php-src` platziert, zum Beispiel: `D:\workspace\php-sdk\php-sdk-binary-tools-2.2.0\phpdev\vs16\x64\php-8.1.5\ext\phpy`, oder Sie können `mklink` verwenden, um einen softlink zu erstellen.



## Kompilierungsconfig

```shell
$ buildconf --force
Rebuilding configure.js
Jetzt führen Sie 'configure --help' durch
configure --with-openssl --with-mysqlnd --with-mysqli --enable-mbstring --enable-pdo --with-pdo-mysql --with-curl --enable-cli --enable-opcache --disable-zts --enable-phpy=shared
```

`--enable-phpy=shared` bedeutet, dass die `phpy`-Erweiterung aktiviert wird und als `.dll` dynamische Link-Bibliothek kompiliert wird

Nach erfolgreicher Ausführung wird das folgende Output generiert:

```shell
...

Generierung von main/config.w32.h
Generierung von phpize
Fertig.


Aktivierte Erweiterungen:
-----------------------
| Erweiterung  | Modus   |
-----------------------
| date       | statisch |
| hash       | statisch |
| json       | statisch |
| pcre       | statisch |
| phpy       | geteilt  |
| reflection | statisch |
| spl        | statisch |
| standard   | statisch |
-----------------------


Aktivierte SAPIs:
-------------
| Sapi-Name |
-------------
| cli       |
-------------


---------------------------------------
|                   |                 |
---------------------------------------
| Build-Typ        | Release         |
| Thread-Sicherheit     | Nein              |
| Compiler          | Visual C++ 2019 |
| Architektur      | x64             |
| Optimierung      | PGO ausgeschaltet    |
| Native Intrinsics | SSE2            |
| Statische Analyzer   | ausgeschaltet        |
---------------------------------------


Typ 'nmake' um PHP zu bauen

D:\workspace\php-sdk\php-sdk-binary-tools-2.2.0\phpdev\vs16\x64\php-8.1.5
$
```



## Erweiterung kompilieren
```shell
nmake clean
nmake
```

## Binär-Paketieren

```shell
nmake snap
```

Nach erfolgreicher Ausführung wird im Verzeichnis `D:\workspace\php-sdk\php-sdk-binary-tools-2.2.0\phpdev\vs16\x64\php-8.1.5\x64\Release` das Paket `php-8.1.5-nts-Win32-vs16-x64.zip` generiert.
