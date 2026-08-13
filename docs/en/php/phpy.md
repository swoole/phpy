# PHPy Management Tool

PHPy provides a `composer`-like package management tool that can install, update, and uninstall the `Python` environment, the `swoole/phpy` extension, and `Python-module`, and manages the dependencies of `Python`-related information and modules introduced by other `composer` packages.

## Usage

Install `swoole/phpy` via `composer`:

```shell
composer require swoole/phpy
```

## Documentation

### 1. Initialize the `phpy.json` configuration

#### Command:

```shell
./vendor/bin/phpy init-config
```

**Similar to `composer`, `PHPy` also has its own configuration management file `phpy.json`. Running the `init-config` command creates the `phpy.json` file in the current directory.**

#### File content:

```php
{
    // Global configuration
    "config": {
        // Cache directory
        "cache-dir": "~/.cache/phpy",
        // Scan paths
        "scan-dirs": [
        ],
        // pip index url
        "pip-index-url": ""
    },
    // python configuration
    "python": {
        // Source code path
        "source-url": "https://github.com/python/cpython.git",
        // Installation path
        "install-dir": "/usr",
        // Installation version; building with `latest` is not supported
        "install-version": "v3.13.2",
        // Build parameters (recommended not to modify)
        "install-configure": [
            "--enable-shared",
            "--with-system-expat",
            "--with-system-ffi",
            "--enable-ipv6",
            "--enable-loadable-sqlite-extensions",
            "--with-computed-gotos",
            "--with-ensurepip=install"
        ]
    },
    // phpy configuration
    "phpy": {
        // Source code path
        "source-url": "https://github.com/swoole/phpy.git",
        // Installation path; `latest` is supported to build from the master branch
        "install-version": "latest",
        // Build parameters
        "install-configure": [],
        // ini file path; an empty string means php.ini is not auto-loaded
        "ini-path": "/usr/local/etc/php/conf.d/xx-php-ext-phpy.ini"
    },
    // Module configuration
    "modules": {
        // Example
        "pandas": "^2.0"
    }
}
```

### 2. Install dependencies

#### Command:

```shell
./vendor/bin/phpy install
```

- The `install` command installs based on the `phpy.json` configuration information of the current project and all `composer` packages introduced in `vendor`. The installation includes:
  - Build dependencies. See [BuildToolsInstaller.php](../../../tools/src/Phpy/Installers/BuildToolsInstaller.php)
  - Build and install the `Python` environment. See [PythonInstaller.php](../../../tools/src/Phpy/Installers/PythonInstaller.php)
  - Build and install the `phpy` extension. See [PhpyInstaller.php](../../../tools/src/Phpy/Installers/PhpyInstaller.php)
  - Install `Python` modules. See [ModuleInstaller.php](../../../tools/src/Phpy/Installers/ModuleInstaller.php)
- The `install` command creates a `phpy.lock` file in the project path to record installation information. On the next install, if the `phpy.lock` file exists, it will not be installed repeatedly.
- The `install` command uses a `Python-venv` environment by default and creates a `py-vendor` directory in the project path to store the `Python` environment and modules.
- The `install` command creates the following files in the project path. **These files should be added to the project's `.gitignore`:**
  - `pip.command`: provides the `executePip` method to execute `pip` commands in a standardized way
  - `python.command`: provides the `executePython` method to execute `python` commands in a standardized way
  - `phpy.command`: provides the `executePhpy` method to execute `phpy` commands in a standardized way
  - `phpy.lock`: records installation information. On the next install, if the `phpy.lock` file exists, it will not be installed repeatedly
  - `requirements.txt`: records the installed `Python` module information, installed using the standardized `executePip`
- Run `--help` for more options

### 3. Update dependencies

#### Command:

```shell
./vendor/bin/phpy update
```

The `update` command updates based on the `phpy.json` configuration. Run `--help` for more options.

- If the `Python` environment has already been built, it is recommended to use `./vendor/bin/phpy update --skip-build-tools --skip-env --skip-ext` to skip environment building and avoid redundant execution.

### 4. Environment check

#### Command:

```shell
./vendor/bin/phpy show
```

The `show` command displays the current `Python` environment information and the imported `Python` module information. Run `--help` for more options.

```shell
/var/www/test-project # ./vendor/bin/phpy show
[>] Python-env:
 [>] Python 3.13.2
 [>] pip 25.0.1 from /var/www/phpy/py-vendor/lib/python3.13/site-packages/pip (python 3.13)
[>] Python-includes:
 [>] -I/var/www/phpy/py-vendor/include/python3.13 -I/var/www/phpy/py-vendor/include/python3.13
[>] Python-modules:
 [>] Package Version
 [>] ------- -------
 [>] pip     25.0.1
 [>] pyorc   0.10.0
```

### 5. Scan and import

#### Command:

```shell
./vendor/bin/phpy scan
```

The `scan` command scans all `php` files according to the `config.scan-dirs` in `phpy.json`, checks the dependent `Python-module`, and imports and installs them. Run `--help` for more options.

- The `scan` command maintains a mapping table between the `top_level` and `module_name` of `Python` modules. When a mapping relationship does not exist in the mapping table, manual confirmation is required.
- The `scan` command is responsible for saving the scan results to `phpy.json`, and `ModuleInstall->upgrade()` is responsible for building `requirements.txt` and installing.
- If the installation fails, please supplement the environment according to the error message. It is usually due to missing dependencies. After the dependencies are installed, re-run `scan` to install.

### 6. Clear cache

#### Command:

```shell
./vendor/bin/phpy clear-cache
```

The `clear-cache` command clears the relevant cache according to the `config.cache-dir` in `phpy.json`. Run `--help` for more options.

### 7. Switch pip mirror

```shell
./vendor/bin/phpy config:pip-mirror
```

`config:pip-mirror` provides some preset pip mirror sources to choose from, and also supports custom pip mirror sources. Run `--help` for more options.

## Community Maintenance

### Public Mapping Library

Package = module, package name = module name, but the name imported via `import` within a module is the module's `top_level`, and the basis for installation by `requirements.txt` is the `module_name`. However, in the `Python` world, `top_level` is not necessarily the same as `module_name`.

Therefore, `PHPy` uses a `supabase` public library to store and maintain a mapping table between `top_level` and `module_name`. This mapping table needs to be actively maintained by developers together:
  - `PHPy` provides a `metadata:push` command, through which developers can manually submit mapping relationships to the public library.
  - `PHPy` provides a `metadata:query` command, through which developers can view the public mapping library.
  - `PHPy`'s `scan` command will also prompt the developer to input manually when no mapping relationship is indexed. The input data will then be automatically synchronized to the public library.

**! We advocate that all users and developers please take good care of this mapping library and do not damage it!**

**! The public library currently stores data in a free tier and provides it to the open source community. Please do not occupy resources excessively!**
