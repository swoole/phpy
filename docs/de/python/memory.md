# Speicherabbau

Wenn `Python` eine `PHP`-Funktion/Methode aufruft, können bei Argumenten und Rückrufen mögliche Speicherabbauvorgänge auftreten. Bei der Entwicklung von performanceorientierten Programmen ist es notwendig, die Kosten für den Speicherabbau zu beachten.

## Argumente

- Integer, boolean, float, `None` werden immer als Wert übergeben

- Objekte, Ressourcen, Referenzen werden immer als Referenz übergeben, ohne dass der Speicher kopiert wird
- Strings, Arrays werden rekursiv tief kopiert und zu nativen Typen umgewandelt

```python
arg1 = 1234
arg2 = 1234.5678
arg3 = True

arg4 = phpy.Object('stdClass')
arg5 = phpy.Reference()
arg6 = phpy.call('fopen', "php://input", "r")

arg7 = {'hello' : 'world'}
arg8 = "hello world"
arg9 = [1, 2, 3, 4, 5]

phpy.call('test', arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9)
```

- `arg1`, `arg2`, `arg3` werden zu PHP-Integers, -Floats, -Booleans und werden direkt kopiert

- `arg4`, `arg5`, `arg6` werden direkt als Referenzen an PHP übergeben, ohne Speicherabbau
- `arg6`, `arg7`, `arg8` werden durchlaufen, tief kopiert und zu PHP-Arrays, -Strings umgewandelt

## Rückwerte

- Integer, boolean, float, `None` (und `null`) werden zu nativen Python-Typen

- Alles andere, was aus Python zurückgegeben wird, ist von Typ `PyObject`
- Es ist auch möglich, in PHP-Code einen `PyObject`-Objekt zu verwenden, um native Python-Typen transparent weiterzugeben

## Speicherabbau vermeiden
Verwenden Sie `phpy.String`, `phpy.Array` Objekte, um beim Aufrufen von PHP-Funktionen keinen Speicherabbau zu verursachen.
