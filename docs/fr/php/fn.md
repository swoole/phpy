# Fonction de rappel

Il est possible d'utiliser des objets callable en PHP comme fonction de rappel en Python. Il suffit de les envelopper avec `PyCore::fn(callable $fn)`.

```php
$m = PyCore::import('app.user');
$uuid = uniqid();
$rs = $m->test_callback(PyCore::fn(function ($namespace) use ($uuid) {
    var_dump($namespace);
    return $uuid;
}));
```

- `import app.user` importe un paquet Python personnalisé

- La fonction `test_callback` du paquet est appelée avec un argument qui est un objet Callable Python

- `PyCore::fn()` enveloppe un objet Closure pour servir de rappel. Cela prend en charge également les appels aux fonctions par nom et aux méthodes d'objets

- La fonction de rappel retourne une chaîne de caractères, qui sera de type str dans la fonction `test_callback`

## Fonction Closure
Dans les dernières versions, lorsque la fonction de rappel est de type Closure, il n'est plus nécessaire d'envelopper avec `PyCore::fn()`, car elle sera directement convertie en objet de rappel. Cependant, lorsque vous utilisez des noms de fonctions ou des méthodes d'objets en tant que rappel, vous devez toujours les envelopper avec `PyCore::fn()`.

```php
# La fonction Closure peut être passée directement
$m->test_callback(function ($namespace) use ($uuid) {
    return $uuid;
});

# Lorsqu'un nom de fonction en chaîne est utilisé comme rappel, il doit être enveloppé avec PyCore::fn()
function test_fn() {
    return $uuid;
}
$m->test_callback(PyCore::fn('test_fn'));
```

## Exemple
Nous utilisons ici `Python tkinter` comme exemple :

```php
<?php
$tkinter = PyCore::import('tkinter');
$root = $tkinter->Tk();
$root->title('Ma fenêtre');
$root->geometry("500x500");
$root->resizable(False, False);

$button = $tkinter->Button($root, text: "Cliquez sur moi!!", command: function () {
    var_dump(func_get_args());
    echo 'cliquez sur moi!!' . PHP_EOL;
});
$button->pack();

$tkinter->mainloop();
```

PHP sert de fonction de rappel pour le bouton Tk de Tkinter.
