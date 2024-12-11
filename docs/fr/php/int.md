Type d'entier
============
Le langage `Python` prend en charge naturellement le calcul de nombres entiers à précision infinie et peut utiliser la capacité de calcul des entiers de `Python` pour remplacer `ext-bcmath`.

Constructeur
-----------
Utilisez la fonction `PyCore::int()` pour construire un nombre, en passant un entier, un nombre à virgule flottante ou une chaîne pour l'initialiser.

```php
$i1 = PyCore::int(12345678);
$i2 = PyCore::int('1234567890123456789012345678901234567890');
$i3 = PyCore::int(12345678.03);
```

Opérations
---------
Les entiers sont également des instances de `PyObject`, et peuvent utiliser les méthodes intégrées pour effectuer des opérations.

```php
$i = PyCore::int(12345435);
var_dump(strval($i->__pow__(3)));
var_dump(strval($i->__add__(4)));
```

La sortie sera `1881564851360655187875`, car elle dépasse la précision maximale de `64 bits`, le résultat sera donc automatiquement converti en type chaîne.
