# Objet Python
`PyObject` est la classe de base de tous les autres types, à l'exception de `PyCore`. Les objets des classes non intégrées sont des instances de `PyObject`. `PyObject` implémente quatre méthodes magiques pour mapper les opérations aux objets Python.

Tous les méthodes de classe, paramètres et retours font référence aux fichiers dans le répertoire `stubs`, la documentation n'est plus présentée ici.

## Classes intégrées

- `PyObject` : classe de base de tous les autres types

- `PyDict` : type de dictionnaire, équivalent à l'associatif PHP

- `PyList` : type de liste, équivalent à l'array indexé PHP

- `PyTuple` : tuple, liste immuable

- `PyStr` : chaîne de caractères
- `PyModule` : paquet Python, `PyModule` est également une sous-classe de `PyObject`

## héritage

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
Lit les attributs d'un objet Python, les opérations suivantes sont équivalentes

```php
$pyobj->attr;
```

```py
pyobj.attr
```

## __set($name, $value)

Établit les attributs d'un objet Python, les opérations suivantes sont équivalentes

```php
$pyobj->attr = 'hello';
```

```py
pyobj.attr = 'hello'
```

## __call($name, $args)

Appelle une méthode d'un objet Python, les opérations suivantes sont équivalentes

```php
$pyobj->fn($a, $b, $c);
```

```py
pyobj.fn(a, b, c)
```

## __invoke(...$args)

Exécute un objet callable, généralement utilisé pour exécuter des fonctions, construire des objets. Les opérations suivantes sont équivalentes

```php
// $user est un PyModule
$user = PyCore::import('app.user');
// Info est une classe dans app.user
$Info = $user->Info;
// Crée un objet Info
$info = $Info('Rango', 2023);
```

```py
from app.user import Info

# Crée un objet Info
info = Info('Rango', 2023);
```

## Paramètres nommés
Soutient l'écriture avec des paramètres nommés. Exemple :

### Passer des paramètres nommés
```php
kwargs($a, $b, $c, name: 'hello', world: 'rango');
```

- Les paramètres ordonnés doivent être en premier, les paramètres nommés doivent être en dernier

### Recevoir des paramètres nommés
```php
function kwargs($a, $b, $c, $name, $world) {

}
```

### Paramètres nommés variables
```php
function kwargs(...$kwargs) {
    var_dump($kwargs);
}

```
- `$kwargs` contiendra à la fois les paramètres ordonnés et les paramètres nommés, par exemple, dans l'exemple ci-dessus, on obtiendra
```php
array(
 0 => $a,
 1 => $b,
 2 => $c,
 'name' => 'hello',
 'world' => 'rango',
)
```

### Passer des paramètres nommés à une autre fonction
```php
function kwargs(...$kwargs) {
    kwargs_fn2(...$kwargs);
}
```

Il est possible de transmettre des paramètres nommés à une autre fonction.
