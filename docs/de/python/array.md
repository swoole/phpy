# Array-Operationen

`phpy.Array` ist ein gemischtes Typ, das entweder ein `List` oder ein `Map` sein kann.

## Erstellung
```python
# List
l = phpy.Array([1, 3, 5, 2023, 7, 9])
# Map
m = phpy.Array({"hello": "world", "php": "swoole"})
```

## Lesen
```python
print(l[3])
print(m["php"])
```

## Länge
```python
print(len(l))
print(len(m))
```

## Schreiben
```python
# Setzen von Key Value
m["swoole"] = 'coroutine'
# Hinzufügen von Element an das Ende
l.append(9999)
```

## Weitere Methoden

- `get(key)` lesen

- `set(key, value)` schreiben

- `unset(key)` löschen

- `append(value)` Element am Ende des Listen hinzufügen

- `count()` Elemente lesen
- `collect()` in ein natives `Python` `dict` oder `list` umwandeln
- `is_list()` überprüfen, ob das Array ein `List` ist
