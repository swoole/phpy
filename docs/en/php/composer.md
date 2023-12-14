# IDE Auto Completion

`phpy` provides a tool for generating `IDE` auto completion files. Here is how to use it:

```shell
cd phpy/tools
php gen-lib.php [Python package name]
```

For example, `matplotlib.pyplot`:
- Import directly: `PyCore::import('matplotlib.pyplot')`
- Generate completion file: `php tools/gen-lib.php matplotlib.pyplot`

You can also configure `tools/gen-all-lib.php` to generate completion files for multiple packages at once.

## How to use

### Install dependency files

```shell
composer require swoole/phpy
```

### Use the auto completion

```php
require dirname(__DIR__, 2) . '/vendor/autoload.php';
$plt = python\matplotlib\pyplot::import();

$x = new PyList([1, 2, 3, 4]);
$y = new PyList([30, 20, 50, 60]);
$plt->plot($x, $y);
$plt->show();
```

![IDE Auto Completion](../../images/autocomplete.png)
