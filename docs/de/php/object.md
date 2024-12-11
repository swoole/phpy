# PyObject
`PyObject` ist die Basisklasse für alle anderen Typen außer `PyCore`. Objekte von nicht eingebauten Klassen sind Instanzen von `PyObject`. `PyObject` implementiert vier Magiemethoden, um Operationen auf `Python`-Objekte zu mappen.

Alle Klassenmethoden, Parameter und Rückkehrwerte sind in den Dateien der `stubs`-Verzeichnis referenziert, weitere Dokumentation wird nicht bereitgestellt.

## eingebauten Typen

- `PyObject`: Basisklasse für alle anderen Typen

- `PyDict`: Der Dictionary-Typ, äquivalent zu assoziierten Arrays in `PHP`

- `PyList`: Der List-Typ, äquivalent zu Index-Arrays in `PHP`

- `PyTuple`: Ein Tuple, eine unveränderliche Liste

- `PyStr`: Eine String-Klasse

- `PyModule`: Ein `Python`-Paket, `PyModule` ist auch eine Unterklasse von `PyObject`

## Vererbungshierarchie

```
PyObject -> PyModule
         -> PySequence -> PyList
                        -> PyTuple
         -> PySet
         -> PyStr
         -> PyDict
         -> PyType
```

## __get($name)
Lesen Sie die Eigenschaften eines `Python`-Objekts, die folgenden Operationen sind äquivalent:

```php
$pyobj->attr;
```

```py
pyobj.attr
```

## __set($name, $value)

Stellen Sie die Eigenschaften eines `Python`-Objekts fest, die folgenden Operationen sind äquivalent:

```php
$pyobj->attr = 'hello';
```

```py
pyobj.attr = 'hello'
```

## __call($name, $args)

Rufen Sie eine Methode eines `Python`-Objekts auf, die folgenden Operationen sind äquivalent:

```php
$pyobj->fn($a, $b, $c);
```

```py
pyobj.fn(a, b, c)
```

## __invoke(...$args)

Führen Sie ein `callable`-Objekt aus, oft zum Ausführen von Funktionen oder zum Instanziieren von Objekten. Die folgenden Operationen sind äquivalent:

```php
// $user ist ein PyModule
$user = PyCore::import('app.user');
// Info ist eine Klasse in app.user
$Info = $user->Info;
// Erstellen eines Info-Objekts
$info = $Info('Rango', 2023);
```

```py
from app.user import Info

# Erstellen eines Info-Objekts
info = Info('Rango', 2023);
```

## Named Parameters
Named Parameters werden unterstützt. Beispiel:

### Named Parameters übergeben
```php
kwargs($a, $b, $c, name: 'hello', world: 'rango');
```

- Reihenfolge der Parameter muss voranstehen, Named Parameters müssen am Ende stehen

### Named Parameters empfangen
```php
function kwargs($a, $b, $c, $name, $world) {

}
```

### Varibles Named Parameters
```php
function kwargs(...$kwargs) {
    var_dump($kwargs);
}

```
- `$kwargs` wird sowohl die Reihenfolgeparameter als auch die Named Parameters enthalten, wie im obigen Beispiel
```php
array(
 0 => $a,
 1 => $b,
 2 => $c,
 'name' => 'hello',
 'world' => 'rango',
)
```

### Named Parameters weiterleiten
```php
function kwargs(...$kwargs) {
    kwargs_fn2(...$kwargs);
}
```

Named Parameters können an andere Funktionen weitergegeben werden.
