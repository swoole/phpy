# Управление классами


## Загрузка класса

```python
cls = phpy.Class("class_name")
```


## Чтение статического свойства класса
```python
value = cls.get("name")
```


## Установка статического свойства класса
```python
cls.set("name", value)
```

## Создание экземпляра
```python
object = cls.new(arg1, arg2, arg3, ...)
```
