# Rückruffunktion

Man kann ein callable Objekt in PHP als Rückruffunktion in Python verwenden. Dies wird durch Umhüllung mit `PyCore::fn(callable $fn)` erreicht.

```php
$m = PyCore::import('app.user');
$uuid = uniqid();
$rs = $m->test_callback(PyCore::fn(function ($namespace) use ($uuid) {
    var_dump($namespace);
    return $uuid;
}));
```

- `import app.user` importiert ein benutzerdefiniertes Python-Paket

- Es wird eine Funktion `test_callback` im Paket aufgerufen, die einen Parameter für ein Python Callable-Objekt erwartet

- Mit `PyCore::fn()` wird ein Closure-Objekt als Rückruf umhüllt, was auch die Verwendung von Funktionsnamen als Strings oder Methoden von Objekten unterstützt

- Die Rückruffunktion gibt einen String zurück, der in der `test_callback` Funktion als `str` zurückgegeben wird

## Closure-Funktionsobjekt
In der neuesten Version müssen für Rückruffunktionen vom Typ `Closure` keine `PyCore::fn()` Umhüllungen mehr verwendet werden, da sie direkt zu einem Rückrufobjekt umgewandelt werden.
Allerdings müssen für Rückruffunktionen, die als `array` oder `string` des Funktionsnamens oder Methoden von Objekten verwendet werden, immer noch `PyCore::fn()` verwendet werden.

```php
# Closure-Funktionsobjekt kann direkt übergeben werden
$m->test_callback(function ($namespace) use ($uuid) {
    return $uuid;
});

# Wenn ein String als Funktionsname für die Rückruffunktion verwendet wird, muss dies mit `PyCore::fn()` verpackt werden
function test_fn() {
    return $uuid;
}
$m->test_callback(PyCore::fn('test_fn'));
```

## Beispiel
Hier wird ein Beispiel mit `Python tkinter` verwendet:

```php
<?php
$tkinter = PyCore::import('tkinter');
$root = $tkinter->Tk();
$root->title('Mein Fenster');
$root->geometry("500x500");
$root->resizable(False, False);

$button = $tkinter->Button($root, text: "Klicken Sie mich!!", command: function () {
    var_dump(func_get_args());
    echo 'Klicken Sie mich!!' . PHP_EOL;
});
$button->pack();

$tkinter->mainloop();
```

PHP dient hier als Rückruffunktion für ein Tk Button.
