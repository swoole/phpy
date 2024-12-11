# Руководство для пользователей

Цель этой библиотеки заключается в использовании экосистемы `Python` для компенсации недостатков `PHP`. Если функция уже существует в `PHP`, то можно использовать ее напрямую на языке `PHP`. В противном случае можно искать подходящие библиотеки в экосистеме `Python`.

`phpy` просто импортирует библиотеки `Python` в экосистему `PHP`, но используется语法 `PHP`, так что нет дополнительных затрат на обучение.

В `Python` все является объектом, будь то модули, классы, функции, целые числа, плавающие точки, `None`, логические значения, объекты, словари, списки, множества, тости - все это примеры `PyObject`.

Обычно мы делаем всего четыре вещи при программировании:

- `PyCore::import()` импортирует пакет

- Зовем метод объекта: `$object->fn()`

- Читая и пишем свойства объекта: `$object->attr` и `$object->attr = $value`
- Зовем встроенную функцию `PyCore::$fn()` для реализации некоторых основных функций, например, `import()` на самом деле является встроенной функцией

## Пример

```php
// Импортировать Python os пакет
$os = PyCore::import('os');
// Звать функцию
$uname = $os->uname();
// Читать свойство
echo $uname->sysname; 
// Отпечатать
echo strval(PyCore::str($uname));
```