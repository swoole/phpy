# Объектные операции


## Создание объекта класса

```python
object = phpy.Object("mysqli", arg1, arg2, arg3, ...)
```


## Чтение свойства
```python
value = object.get("name")
```


## Установка свойства
```python
object.set("name", value)
```

## Вызывание метода
```python
return_value = object.call("name", arg1, arg2, arg3, ...)
```

> Обязательно должен быть методом объекта, для классовых статических методов используйте функцию `phpy.call()` для вызова

