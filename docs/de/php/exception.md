# Ausnahmebehandlung

`phpy` hat die Ausnahmen in `Python` verpackt und den `PyError` Typ bereitgestellt, der es in `PHP`-Code ermöglicht, `Python`-Ausnahmen zu fangen.


## Vererbungshierarchie
`PyError` ist eine Unterklasse der `Exception`-Klasse.




## Attributliste

- `error`: Das Fehlerm对象

- `type`: Die Fehlertyp

- `value`: Der Fehlervalue
- `traceback`: Der Rückrufstack des Fehlers

Diese Attribute sind entweder `PyObject`-Objekte oder `null`


## Ausnahmen fangen

```php
try {
    PyCore::import('not_exists');
} catch (PyError $e) {
    PyCore::print($e->error);
    PyCore::print($e->type);
    PyCore::print($e->value);
    PyCore::print($e->traceback);
}
```


- Im Hintergrund wird der stringwerte von `$e->value` automatisch als Ausnahmemeldung festgelegt, die mit `$e->getMessage()` abgerufen werden kann
- `PyError` setzt keinen `$e->code` Fehlercode, bitte nicht verwenden
