# PHPy 管理工具

PHPy提供类似`composer`的包管理工具，可以安装、更新、卸载 `Python`环境、`swoole/phpy`拓展及`Python-module`，
对其他`composer`引入的`Python`相关信息和模块进行依赖管理。

## 使用

通过`composer`安装`swoole/phpy`
```shell
composer require swoole/phpy
```

## 文档

### 1. 初始化`phpy.json`配置

#### 命令：
```shell
./vendor/bin/phpy init-config
```

**与`composer`类似，`PHPy`也有自己的配置管理文件`phpy.json`；使用`init-config`命令可以在当前目录下创建`phpy.json`文件。**

#### 文件内容：
```php
{
    // 全局配置
    "config": {
        // 缓存目录
        "cache-dir": "~/.cache/phpy",
        // 扫描路径
        "scan-dirs": [
        ],
        // pip源
        "pip-index-url": ""
    },
    // python 配置
    "python": {
        // 源码路径
        "source-url": "https://github.com/python/cpython.git",
        // 安装路径
        "install-dir": "/usr",
        // 安装版本，不支持latest构建
        "install-version": "v3.13.2",
        // 编译参数（建议不要改动）
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
    // phpy 配置
    "phpy": {
        // 源码路径
        "source-url": "https://github.com/swoole/phpy.git",
        // 安装路径，支持latest使用master分支进行构建
        "install-version": "latest",
        // 编译参数
        "install-configure": [],
        // ini文件路径，空字符串为不自动引入php.ini
        "ini-path": "/usr/local/etc/php/conf.d/xx-php-ext-phpy.ini"
    },
    // 模块配置
    "modules": {
        // 例子
        "pandas": "^2.0"
    }
}
```

### 2. 依赖安装

#### 命令：
```shell
./vendor/bin/phpy install
```
- `install`命令会根据当前项目及`vendor`中引入的所有`composer`包的`phpy.json`配置信息进行安装，安装内容如下：
  - 编译构建依赖，详见[BuildToolsInstaller.php](../../../tools/src/Phpy/Installer/BuildToolsInstaller.php)
  - 编译安装`Python`环境，详见[PythonInstaller.php](../../../tools/src/Phpy/Installer/PythonInstaller.php)
  - 编译安装`phpy`拓展，详见[PhpyInstaller.php](../../../tools/src/Phpy/Installer/PhpyInstaller.php)
  - 安装`Python`模块，详见[ModuleInstaller.php](../../../tools/src/Phpy/Installer/ModuleInstaller.php)
- `install`命令会在项目路径下创建`phpy.lock`文件，用于记录安装信息，下次安装时，如果`phpy.lock`文件存在，则不会重复安装。
- `install`命令默认使用`Python-venv`环境，会在项目路径下创建`py-vendor`目录，用于存储`Python`环境及模块。
- `install`命令会在项目路径下创建如下文件，**以下文件建议加入项目`.gitignore`文件**：
  - `pip.command`：用于提供`executePip`方法标准化执行`pip`命令
  - `python.command`：用于提供`executePython`方法标准化执行`python`命令
  - `phpy.command`：用于提供`executePhpy`方法标准化执行`phpy`命令
  - `phpy.lock`：用于记录安装信息，下次安装时，如果`phpy.lock`文件存在，则不会重复安装
  - `requirements.txt`：用于记录安装的`Python`模块信息，使用标准化`executePip`安装
- 更多查看`--help`

### 3. 依赖更新

#### 命令：
```shell
./vendor/bin/phpy update
```

`update`命令会根据`phpy.json`配置信息进行更新，更多查看`--help`

- 如果已经构建好Python环境，建议使用`./vendor/bin/phpy update --skip-build-tools --skip-env --skip-ext`跳过环境构建，避免重复执行

### 4. 环境检查

#### 命令：
```shell
./vendor/bin/phpy show
```

`show`命令会展示当前`Python`环境信息及引入的`Python`模块信息，更多查看`--help`

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

### 5. 扫描引入

#### 命令：
```shell
./vendor/bin/phpy scan
```

`scan`命令会根据`phpy.json`的`config.scan-dirs`扫描所有php文件并检查依赖的`Python-module`，
引入并安装，更多查看`--help`

- `scan`命令维护了一个`Python module`的`top_level`与`module_name`的映射表，在映射表中不存在映射关系的时候需要手动确认
- `scan`命令负责将扫描结果保存至`phpy.json`，由`ModuleInstall->upgrade()`负责构建`requirements.txt`及安装
- 如安装过程失败，请根据错误信息进行环境补足，一般情况是缺少依赖，待依赖安装完成后重复执行`scan`即可安装

### 6. 缓存清除

#### 命令：
```shell
./vendor/bin/phpy clear-cache
```

`clear-cache`命令会根据`phpy.json`的`config.cache-dir`清除相关缓存，更多查看`--help`

## 共建维护

### 公共映射库

包 = 模块，包名 = 模块名，但在模块之中以import引入的名称是模块的`top_level`，`requirements.txt`
安装的依据是`module_name`，但在`Python`世界中，`top_level`并不一定与`module_name`相同；

因此`PHPy`通过`supabase`公共库储存维护了一张`top_level`与`module_name`的映射表，这张映射表需要
开发者们一起积极维护；
  - `PHPy`提供了一个`metadata:push_metadata`的命令，开发者可以手动提交映射关系至公共库；
  - `PHPy`提供了一个`metadata:query_metadata`的命令，开发者可以查看映射关系公共库；
  - `PHPy`的`scan`的命令也会在未索引到映射关系时提示开发者手动输入，输入数据在随后会自动同步到公共库；

**！这里我们倡导所有使用者及开发者，请爱护好该映射库，请勿破坏！**

**！公共库目前以免费版储存数据提供至开源社区，请勿过量占用资源！**

