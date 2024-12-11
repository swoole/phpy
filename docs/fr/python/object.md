# Opérations sur les objets


## Créer un objet d'une classe

```python
object = phpy.Object("mysqli", arg1, arg2, arg3, ...)
```


## Lire une propriété
```python
value = object.get("name")
```


## Établir une propriété
```python
object.set("name", value)
```

## Appeler une méthode
```python
return_value = object.call("name", arg1, arg2, arg3, ...)
```

> Doit être une méthode de l'objet, pour appeler une méthode statique de la classe utilisez la fonction `phpy.call()`
