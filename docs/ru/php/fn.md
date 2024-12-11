# Кеш-функции

В `Python` можно использовать объект, который может быть вызван в `PHP`, в качестве回调-функции. Для этого достаточно обернуть его в `PyCore::fn(callable $fn)`.

```php
$m = PyCore::import('app.user');
$uuid = uniqid();
$rs = $m->test_callback(PyCore::fn(function ($namespace) use ($uuid) {
    var_dump($namespace);
    return $uuid;
}));
```

- `import app.user` импортирует пользовательский пакет `Python`.

- Функция `test_callback` в пакете принимает один параметр - объект, который является callable в `Python`.

- Для callback используется `PyCore::fn()`, который оберает Closure-объект. Также поддерживаются имя функции как строки и вызов метода объекта.

- Callback-функция возвращает строку, которая будет получена в `test_callback` в виде `str`.

## Функции Closure
В последних версиях, когда тип callback является Closure, обернуть его в `PyCore::fn()` больше не требуется, так как он будет автоматически превращен в callback-объект.
Однако, когда callback является функцией, представленной в виде массива или строки, или методом класса, все еще необходимо использовать `PyCore::fn()` для упаковки.

```php
#Closure можно передавать напрямую
$m->test_callback(function ($namespace) use ($uuid) {
    return $uuid;
});

#Когда callback является именем функции в виде строки, его все равно нужно упаковать с помощью PyCore::fn()
function test_fn() {
    return $uuid;
}
$m->test_callback(PyCore::fn('test_fn'));
```

## Пример
В этом примере используется `Python tkinter`:

```php
<?php
$tkinter = PyCore::import('tkinter');
$root = $tkinter->Tk();
$root->title('Мой окно');
$root->geometry("500x500");
$root->resizable(False, False);

$button = $tkinter->Button($root, text: "Нажмите меня!!", command: function () {
    var_dump(func_get_args());
    echo 'Нажмите меня!!' . PHP_EOL;
});
$button->pack();

$tkinter->mainloop();
```

`PHP` служит callback-функцией для `Tk Button`.
