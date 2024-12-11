# Compilation sous Windows

> Seule la version `PHP-8.1` ou supérieure est prise en charge.

## Environnement de développement PHP

Référence : [https://wiki.php.net/internals/windows/stepbystepbuild_sdk_2](https://wiki.php.net/internals/windows/stepbystepbuild_sdk_2)

- Installez `Visual C++ 16.0`, adresse : [https://aka.ms/vs/16/release/vs_buildtools.exe](https://aka.ms/vs/16/release/vs_buildtools.exe)

- Installez `php-sdk-binary-tools`, adresse : [https://github.com/php/php-sdk-binary-tools](https://github.com/php/php-sdk-binary-tools)

- Téléchargez le code source `PHP`

- Installez les bibliothèques dépendantes, adresse : [https://windows.php.net/downloads/php-sdk/deps/](https://windows.php.net/downloads/php-sdk/deps/)

> Tous les fichiers liés à `PHP` sont installés dans le répertoire `d:\workspace`.

## Environnement de développement Python

- Installez `Python`, adresse : [https://www.python.org/downloads/windows/](https://www.python.org/downloads/windows/)

- Ajoutez `d:\python` à la liste des variables d'environnement `Path`, exécutez `Python -V` dans la `console Windows`.

- Ajoutez une variable d'environnement `PYTHONHOME` qui pointe vers `d:\python`.

> `Python` est installé dans le répertoire `d:\python`.

```shell
C:\WINDOWS\system32>python -V
Python 3.12.1

echo %Path%
echo %PYTHONHOME%
```

## Répertoire de construction

```shell
cd D:\workspace\php-sdk\php-sdk-binary-tools-2.2.0
phpsdk-vs16-x64.bat
```

Après succès, entrez dans le répertoire `php-src` dans ce terminal

```shell
cd D:\workspace\php-sdk\php-sdk-binary-tools-2.2.0\phpdev\vs16\x64\php-8.1.5
phpsdk_deps -u
```

Les projets d'extension sont placés dans le répertoire `ext` de `php-src`, par exemple : `D:\workspace\php-sdk\php-sdk-binary-tools-2.2.0\phpdev\vs16\x64\php-8.1.5\ext\phpy`, ou vous pouvez utiliser la commande `mklink` pour créer un lien symbolique.

## Configuration de la compilation

```shell
$ buildconf --force
Rebuilding configure.js
Maintenant, exécutez 'configure --help'
configure --with-openssl --with-mysqlnd --with-mysqli --enable-mbstring --enable-pdo --with-pdo-mysql --with-curl --enable-cli --enable-opcache --disable-zts --enable-phpy=shared
```

`--enable-phpy=shared` signifie activer l'extension `phpy` et la compiler en bibliothèque dynamique `.dll`.

Après l'exécution réussie, la sortie sera :

```shell
...

Génération de main/config.w32.h
Génération de phpize
Finie.


Extensions activées :
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


SAPI activé :
-------------
| Nom du Sapi |
-------------
| cli       |
-------------


---------------------------------------
|                   |                 |
---------------------------------------
| Type de build        | Release         |
| Sécurité des threads | Non              |
| Compilateur          | Visual C++ 2019 |
| Architecture          | x64             |
| Optimisation          | Désactivée PGO   |
| Intrinsèques natives | SSE2            |
| Analyseur statique    | Désactivé        |
---------------------------------------


Type 'nmake' pour construire PHP

D:\workspace\php-sdk\php-sdk-binary-tools-2.2.0\phpdev\vs16\x64\php-8.1.5
$
```

## Compilation des extensions
```shell
nmake clean
nmake
```

## Emballage binaire

```shell
nmake snap
```

Après succès, un fichier `php-8.1.5-nts-Win32-vs16-x64.zip` sera généré dans `D:\workspace\php-sdk\php-sdk-binary-tools-2.2.0\phpdev\vs16\x64\php-8.1.5\x64\Release`.
