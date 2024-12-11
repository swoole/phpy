# IDE 自動提示

`phpy`は、IDEの自動提示機能を提供する自動生成ツールを提供しています。使用方法は以下の通りです：

```shell
cd phpy/tools
php gen-lib.php [Python パッケージ名]
```

例えば`matplotlib.pyplot`については：

- 直接導入：`PyCore::import('matplotlib.pyplot')`
- 推測ファイル生成：`php tools/gen-lib.php matplotlib.pyplot`

また、`tools/gen-all-lib.php`を配置することで、複数のパッケージの推測ファイルを一度に生成することもできます。

## 使用方法

### 依存ファイルのインストール

```shell
composer require swoole/phpy
```

### 自動提示器の使用

```php
require dirname(__DIR__, 2) . '/vendor/autoload.php';
$plt = python\matplotlib\pyplot::import();

$x = new PyList([1, 2, 3, 4]);
$y = new PyList([30, 20, 50, 60]);
$plt->plot($x, $y);
$plt->show();
```

![IDE 自動完成](../../images/autocomplete.png)
