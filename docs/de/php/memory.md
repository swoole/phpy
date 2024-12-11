# Speicherkopie

Wenn PHP eine Python-Funktion/Methode aufruft, können bei den Parametern und Rückgaben mögliche Speicherkopien auftreten, was bei der Entwicklung von Performance-kritischen Programmen auf die Kosten der Speicherkopie achten muss.

## Parameter

- Integer, boolean, float, null (null) werden immer als Wert übergeben

- Objekte, Ressourcen, Referenzen werden immer als Referenz übergeben, ohne dass der Speicher kopiert wird
- Strings, Arrays werden rekursiv tief kopiert und zu nativen Typen umgewandelt

```php
$user = PyCore::import("user");
$arg1 = 1234;
$arg2 = 1234.5678;
$arg3 = true;

$arg4 = new PyDict();
$arg5 = new stdClass();
$arg6 = fopen("php://input", "r");

$arg7 = ['hello' => 'world'];
$arg8 = "hello world";
$arg9 = [1, 2, 3, 4, 5];

$user->test($arg1, $arg2, $arg3, $arg4, $arg5, $arg6, $arg7, $arg8, $arg9);
```

- `$arg1`, `$arg2`, `$arg3` werden zu Python-Integers, -Floats, -Booleans und werden direkt kopiert

- `$arg4`, `$arg5`, `$arg6` werden direkt mit Referenzen an Python übergeben, ohne dass eine Speicherkopie entsteht
- `$arg6`, `$arg7`, `$arg8` werden durchlaufen, tief kopiert und zu Python-Listen, -Dictionaries, -Strings umgewandelt

## Rückgaben

- Integer, boolean, float, null (None und null) werden zu nativen PHP-Typen

- Alles andere, was aus Python zurückgegeben wird, ist von Typ PyObject
- Man kann auch direkt in der Python-Code Python-natives Typen wie phpy.String oder phpy.Array verwenden, um eine transparente Weitergabe zu erreichen

## Speicherkopien vermeiden
Verwenden Sie die Methode `PyObject::object($value)` zum Konvertieren von Strings und Arrays in PyObject. Die in der Python-Code erhaltenen Typen sind dann phpy.String und phpy.Array.

Diese Methode erfordert, dass der Python-Code an das Typensystem von phpy angepasst wird.
