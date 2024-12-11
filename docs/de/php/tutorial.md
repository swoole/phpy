# Benutzerhandbuch

Das Ziel dieser Bibliothek ist es, die Lücken von PHP mit der Ökologie von Python auszugleichen. Wenn eine Funktion in PHP bereits vorhanden ist, kann man direkt die Sprache PHP verwenden. Gibt es keine entsprechenden Funktionen in PHP, kann man nach verfügbaren Bibliotheken in der Python-Ökologie suchen.

`phpy` importiert nur die Python-Bibliotheken in die PHP-Ökologie, aber der verwendete Syntax ist PHP, es gibt keine zusätzliche Lernzeit.

In Python ist alles ein Objekt, egal ob ein Modul, eine Klasse, eine Funktion, ein Integer, ein Float, None, ein Boolean, ein Objekt, ein Dictionary, eine Liste, eine Menge, ein Tuple – sie sind alle Instanzen von `PyObject`.

Was wir normalerweise beim Programmieren tun, sind ungefähr vier Dinge:

- `PyCore::import()` importiert ein Paket

- Aufrufen von Methoden eines Objekts: `$object->fn()`

- Lesen und Schreiben von Attributen eines Objekts: `$object->attr` und `$object->attr = $value`
- Ausführen von eingebauten Funktionen `PyCore::$fn()` um grundlegende Funktionen zu erreichen, zum Beispiel ist `import()` tatsächlich eine eingebildete Funktion.

## Beispiel

```php
// Importieren des Python os Pakets
$os = PyCore::import('os');
// Aufrufen einer Funktion
$uname = $os->uname();
// Lesen eines Attributs
echo $uname->sysname; 
// Ausgeben
echo strval(PyCore::str($uname));
```
