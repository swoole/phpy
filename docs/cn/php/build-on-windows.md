# Windows 编译

> 仅支持 `PHP-8.1` 或更高版本

## 开发环境

参考：[https://wiki.php.net/internals/windows/stepbystepbuild_sdk_2](https://wiki.php.net/internals/windows/stepbystepbuild_sdk_2)

- 安装 `Visual C++ 16.0`
- 安装 `php-sdk-binary-tools`，地址：[https://github.com/php/php-sdk-binary-tools](https://github.com/php/php-sdk-binary-tools)
- 下载 `php` 源代码
- 安装依赖库，地址：[https://windows.php.net/downloads/php-sdk/deps/](https://windows.php.net/downloads/php-sdk/deps/)


> 所有文件均安装在 `d:\workspace` 目录下


## 构建目录

```shell
cd D:\workspace\php-sdk\php-sdk-binary-tools-2.2.0
phpsdk-vs16-x64.bat
```

成功后，在此终端进入 `php-src` 目录

```shell
cd D:\workspace\php-sdk\php-sdk-binary-tools-2.2.0\phpdev\vs16\x64\php-8.1.5
```

扩展项目放置于 `php-src` 的 `ext` 目录下，例如：`D:\workspace\php-sdk\php-sdk-binary-tools-2.2.0\phpdev\vs16\x64\php-8.1.5\ext\phpy`，也可以使用 `mklink` 命令创建软连接。


## 编译配置

```shell
$ buildconf --force
Rebuilding configure.js
Now run 'configure --help'
configure --disable-all --enable-cli --disable-zts --enable-phpy=shared
```

`--enable-phpy=shared` 表示启用 `phpy` 扩展，并且编译为 `.dll` 动态链接库

执行成功后，输出：

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


## 编译扩展
```shell
nmake clean
nmake
```

## 二进制打包

```shell
nmake snap
```

执行成功后，将在 `D:\workspace\php-sdk\php-sdk-binary-tools-2.2.0\phpdev\vs16\x64\php-8.1.5\x64\Release` 生成 `php-8.1.5-nts-Win32-vs16-x64.zip`。