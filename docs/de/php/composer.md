# IDE-Automatische Vervollständigung

`phpy` bietet ein automatisches Generatortool, das IDE-Automatischer Vervollständigungsdateien erstellen kann.使用方法：

```shell
cd phpy/tools
php gen-lib.php [Python-Paketname]
```

Zum Beispiel `matplotlib.pyplot`:

- Direkt importieren: `PyCore::import('matplotlib.pyplot')`
- Vervollständigungsdatei generieren: `php tools/gen-lib.php matplotlib.pyplot`

Auch die Konfiguration von `tools/gen-all-lib.php` ermöglicht es, mehrere Pakete gleichzeitig zu generieren.

## Wie es funktioniert

### Abhängigkeitsdateien installieren

```shell
composer require swoole/phpy
```

### Automatischer Vervollständiger verwenden

```php
require dirname(__DIR__, 2) . '/vendor/autoload.php';
$plt = python\matplotlib\pyplot::import();

$x = new PyList([1, 2, 3, 4]);
$y = new PyList([30, 20, 50, 60]);
$plt->plot($x, $y);
$plt->show();
```

![IDE Automatische Vervollständigung](../../images/autocomplete.png)
