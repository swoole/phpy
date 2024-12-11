# Операции с массивами

`phpy.Array` - это гибридный тип, который может быть как `List`, так и `Map`.

## Создание
```python
# List
l = phpy.Array([1, 3, 5, 2023, 7, 9])
# Map
m = phpy.Array({"hello": "world", "php": "swoole"})
```

## Чтение
```python
print(l[3])
print(m["php"])
```

## Длина
```python
print(len(l))
print(len(m))
```

##写入
```python
# Установка ключа-значения
m["swoole"] = 'coroutine'
# Добавление элемента в конец
l.append(9999)
```

## Другие методы

- `get(key)` чтение

- `set(key, value)` запись

- `unset(key)` удаление

- `append(value)` добавление элемента в конец списка

- `count()` чтение элементов
- `collect()` преобразование в `Python` родной `dict` или `list`
- `is_list()` проверка, является ли массив `List`
