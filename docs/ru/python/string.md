# операций со строками
`phpy.String` тип строки эквивалентен массиву字节 в `Python`. В содержании не содержится информация о кодировке и может существовать бинарное содержание.
Не эквивалентен типу `str` в `Python`. В основе `phpy` предоставлена API-стиль `str` для работы со строками.

## Создание
```python
s1 = phpy.String("hello world")
s2 = phpy.call("random_bytes", 128)
```

## Длина
```python
print(len(s1))
print(len(s2))
```

## Добавление
```python
# Добавление str
s1 += "hello"
# Добавление bytes
s1 += b"world"
# Добавление другой phpy.String
s1 += phpy.String(", php is the best program language")
```

## Содержание
```python
# Возвращает True
print(s1.__contains__("php")) 
# Возвращает False
print(s1.__contains__("java"))
```

## Сравнение
```python
s3 = phpy.String("hello")
if s3 == "hello":
    print("==")
```

## Получение字节
```python
print(s1[2])
```

Обратите внимание, что `phpy.String` возвращает формат, согласующийся с `bytes`, это `uchar`.
Однако в отличие от `str`, `str` обрабатывает `UTF-8` кодировку и возвращает широком字符 `UTF-8`, например, `str('中国')[0]` возвращает `中`.

## Конвертация в тип `bytes` `Python`

```python
print(bytes(s1))
```

> Обратите внимание, что здесь произойдет копирование памяти

