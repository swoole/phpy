Ganzzahlige Datentypen
======================
Die `Python` Sprache unterstützt nativ die Berechnung von Ganzzahlen mit unendlicher Präzision und kann die Integer-Berechnungsfähigkeit von `Python` nutzen, um `ext-bcmath` zu ersetzen.

Konstruktion
------------
Verwenden Sie die `PyCore::int()` Funktion, um eine Zahl zu konstruieren, und übergeben Sie dabei eine ganze Zahl, eine Flüssigkeitszahl oder einen String zur Initialisierung.

```php
$i1 = PyCore::int(12345678);
$i2 = PyCore::int('1234567890123456789012345678901234567890');
$i3 = PyCore::int(12345678.03);
```

Operationen
----------
Ganzzahlen sind ebenfalls Instanzen von `PyObject` und können mit eingebauten Methodenklasse durchgeführt werden.

```php
$i = PyCore::int(12345435);
var_dump(strval($i->__pow__(3)));
var_dump(strval($i->__add__(4)));
```

Wird dies ausgegeben, ist `1881564851360655187875`, da das Ergebnis die maximale Präzision von `64 Bit` überschreitet, wird das Ausgabeergebnis automatisch in einen String-Typ umgewandelt.
