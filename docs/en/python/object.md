# Object Operation

## Creating an object of a class

```python
object = phpy.Object("mysqli", arg1, arg2, arg3, ...)
```

## Reading attributes
```python
value = object.get("name")
```

## Setting attributes
```python
object.set("name", value)
```

## Calling methods
```python
return_value = object.call("name", arg1, arg2, arg3, ...)
```

> Only object methods can be called using this syntax. For class static methods, please use the `phpy.call()` function.