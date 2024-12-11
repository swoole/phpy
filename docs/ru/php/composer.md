# Автоматическое Suggestion в IDE

`phpy` предоставляет инструмент для автоматического генерации файлов со suggestionами для `IDE`. Как использовать:

```shell
cd phpy/tools
php gen-lib.php [Название Python пакета]
```

Например, `matplotlib.pyplot`:

- Прямое импортирование: `PyCore::import('matplotlib.pyplot')`
- Генерация файла suggestionов: `php tools/gen-lib.php matplotlib.pyplot`

Также можно настроить `tools/gen-all-lib.php` для массового генерации suggestionов для нескольких пакетов.

## Как использовать

### Установка зависимых файлов

```shell
composer require swoole/phpy
```

### Использование автоматического suggestionатора

```php
require dirname(__DIR__, 2) . '/vendor/autoload.php';
$plt = python\matplotlib\pyplot::import();

$x = new PyList([1, 2, 3, 4]);
$y = new PyList([30, 20, 50, 60]);
$plt->plot($x, $y);
$plt->show();
```

![IDE Автоматическое завершение](../../images/autocomplete.png)
