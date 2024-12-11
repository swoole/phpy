# Objektoperationen


## Erstellung eines Objekts einer Klasse

```python
object = phpy.Object("mysqli", arg1, arg2, arg3, ...)
```


## Lesen einer Eigenschaft
```python
value = object.get("name")
```


## Festlegen einer Eigenschaft
```python
object.set("name", value)
```

## Aufrufen einer Methode
```python
return_value = object.call("name", arg1, arg2, arg3, ...)
```

> Muss eine Methode des Objekts sein, für statische Methoden der Klasse bitte die `phpy.call()` Funktion verwenden
