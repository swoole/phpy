# PyObject
`PyObject` является базовым классом всех других типов, кроме `PyCore`. Объекты не встроенных классов являются 实例ами `PyObject`. `PyObject` реализует `4` волшебных метода для сопоставления операций с объектами `Python`.

Все методы класса, параметры, возвращаемые значения ссылаются на файлы в каталоге `stubs`, документация больше не описывается.




## Встроенные классы

- `PyObject`: базовый класс всех других типов

- `PyDict`: тип словаря, эквивалент ассоциативному массиву в `PHP`

- `PyList`: тип списка, эквивалент индексированному массиву в `PHP`

- `PyTuple`: тигр, неизменимый список

- `PyStr`: строка
- `PyModule`: пакет `Python`, `PyModule` также является подклассом `PyObject`


##谱系ция наследования

```
PyObject -> PyModule
         -> PySequence -> PyList
                        -> PyTuple
         -> PySet
         -> PyStr
         -> PyDict
         -> PyType
```


## __get($name)
Чтение свойства объекта `Python`, следующие операции эквивалентны

```php
$pyobj->attr;
```

```py
pyobj.attr
```


## __set($name, $value)

Установка свойства объекта `Python`, следующие операции эквивалентны

```php
$pyobj->attr = 'hello';
```

```py
pyobj.attr = 'hello'
```


## __call($name, $args)

Зов метода объекта `Python`, следующие операции эквивалентны

```php
$pyobj->fn($a, $b, $c);
```

```py
pyobj.fn(a, b, c)
```


## __invoke(...$args)

Выполнение объекто-функции, обычно используется для выполнения функций, создания объектов. Следующие операции эквивалентны

```php
// $user является PyModule
$user = PyCore::import('app.user');
// Info является классом в app.user
$Info = $user->Info;
// Создание объекта Info
$info = $Info('Rango', 2023);
```

```py
from app.user import Info

# Создание объекта Info
info = Info('Rango', 2023);
```


## Номинальные параметры
Поддерживается写法 с именными параметрами. Пример:


### Передача именованных параметров
```php
kwargs($a, $b, $c, name: 'hello', world: 'rango');
```


- Порядок параметров должен быть первым, а именованные параметры - последним


### Получение именованных параметров
```php
function kwargs($a, $b, $c, $name, $world) {

}
```


### Переменные именованные параметры
```php
function kwargs(...$kwargs) {
    var_dump($kwargs);
}

```
- `$kwargs` будет содержать как порядок параметров, так и именованные параметры, например, в предыдущем примере будет получено
```php
array(
 0 => $a,
 1 => $b,
 2 => $c,
 'name' => 'hello',
 'world' => 'rango',
)
```

### Передача именованных параметров
```php
function kwargs(...$kwargs) {
    kwargs_fn2(...$kwargs);
}
```

Можно передать именованные параметры другой функции.