# Opérations sur les classes


## Charge une classe

```python
cls = phpy.Class("class_name")
```


## Récupère une propriété statique d'une classe
```python
value = cls.get("name")
```


## Établit une propriété statique d'une classe
```python
cls.set("name", value)
```

## Crée une instance
```python
object = cls.new(arg1, arg2, arg3, ...)
```
