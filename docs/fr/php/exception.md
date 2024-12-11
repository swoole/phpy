# Traitement des exceptions

`phpy` encapsule les exceptions de `Python`, offrant le type `PyError`, permettant aux codes `PHP` de capturer les exceptions `Python`.

## Hierarchie de l'héritage
`PyError` est une sous-classe de la classe `Exception`.

## Liste des attributs

- `error` : objet d'erreur
- `type` : type d'erreur
- `value` : valeur de l'erreur
- `traceback` : pile d'appel de l'erreur

Ces attributs sont des objets `PyObject` ou `null`.

## Capturer une exception

```php
try {
    PyCore::import('not_exists');
} catch (PyError $e) {
    PyCore::print($e->error);
    PyCore::print($e->type);
    PyCore::print($e->value);
    PyCore::print($e->traceback);
}
```

- Le底层 associe automatiquement la valeur de chaîne de `$e->value` à l'message de l'exception, accessible via `$e->getMessage()`.
- `PyError` n'est pas équipé de `$e->code` pour l'erreur, veuillez ne pas l'utiliser.
