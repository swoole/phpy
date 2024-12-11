# Copie de mémoire

Lorsque le code PHP appelle une fonction/méthode Python, il peut y avoir des copies de mémoire pour les arguments et les valeurs de retour, ce qui est important à prendre en compte pour les performances dans les programmes sensibles à la mémoire.

## Arguments

- Les types intégres, booléens, flottants et nulls sont toujours transmis par valeur.
- Les objets, les ressources et les références sont toujours transmis par référence, sans duplication de mémoire.
- Les chaînes et les tableaux subissent une copie profonde et sont convertis en types natifs.

```php
$user = PyCore::import("user");
$arg1 = 1234;
$arg2 = 1234.5678;
$arg3 = true;

$arg4 = new PyDict();
$arg5 = new stdClass();
$arg6 = fopen("php://input", "r");

$arg7 = ['hello' => 'world'];
$arg8 = "hello world";
$arg9 = [1, 2, 3, 4, 5];

$user->test($arg1, $arg2, $arg3, $arg4, $arg5, $arg6, $arg7, $arg8, $arg9);
```

- `$arg1`, `$arg2`, `$arg3` seront convertis en types intégres, flottants et booléens en Python, et les valeurs numériques seront directement copiées.
- `$arg4`, `$arg5`, `$arg6` seront transmis par référence en Python, sans création de copies de mémoire.
- `$arg6`, `$arg7`, `$arg8` seront parcourus et deep copied, puis convertis en `list`, `dict` et `str` en Python.

## Valeurs de retour

- Les types intégres, booléens, flottants et nulls (ainsi que `None` et `null`) seront convertis en types natifs PHP.
- Tout le reste du contenu renvoyé depuis Python est de type `PyObject`.
- Il est également possible d'utiliser directement des types natifs PHP tels que `phpy.String` ou `phpy.Array` dans le code Python pour une transmission transparente.

## Éviter les copies de mémoire
Utilisez la méthode `PyObject::object($value)` pour transformer des chaînes et des tableaux en `PyObject`. Dans le code Python, vous obtiendrez des types `phpy.String` et `phpy.Array`.

Cette méthode nécessite une adaptation du système de types `phpy` dans le code Python.
