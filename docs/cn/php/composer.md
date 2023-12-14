# IDE 自动提示

`phpy` 提供了一个自动生成工具，可以生成 `IDE` 自动提示文件。使用方法：

```shell
cd phpy/tools
php gen-lib.php [Python 包名称]
```

例如 `matplotlib.pyplot` ：
- 直接导入：`PyCore::import('matplotlib.pyplot')`
- 生成提示文件：`php tools/gen-lib.php matplotlib.pyplot`

也配置 `tools/gen-all-lib.php` 批量生成多个包的提示文件。


## 如何使用

### 安装依赖文件

```shell
composer require swoole/phpy
```

### 使用自动提示器

```php
require dirname(__DIR__, 2) . '/vendor/autoload.php';
$plt = python\matplotlib\pyplot::import();

$x = new PyList([1, 2, 3, 4]);
$y = new PyList([30, 20, 50, 60]);
$plt->plot($x, $y);
$plt->show();
```

![IDE 自动完成](../../images/autocomplete.png)
