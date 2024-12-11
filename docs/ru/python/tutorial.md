# Использование функций PHP в Python

В коде Python можно вызвать функции PHP. Модуль называется `phpy`, его нужно импортировать.

- [Список функций](function.md)

- [Операции с объектами](object.md)

- [Операции с классами](class.md)

- [Ссылочные типы](reference.md)
- [Обобщение модулей](module.md)

## Пример
```python
from php import curl

ch = curl.init("https://www.baidu.com/")
curl.setopt(ch, curl.CURLOPT_RETURNTRANSFER, True)
rs = curl.exec(ch)
print(rs)
```

В данном примере мы используем PHP cURL расширение для запроса главной страницы Baidu.

## Обобщение модулей
Помимо прямого использования модуля `phpy`, можно также использовать автоматически сгенерированные封装ные модули с помощью инструментов рефлексии.

### Генерация
```shell
php tools/gen-pymod.php
```

### Использование
```python
from php import curl

ch = curl.init("https://www.baidu.com/")
curl.setopt(ch, curl.CURLOPT_RETURNTRANSFER, True)
rs = curl.exec(ch)
print(rs)
```
