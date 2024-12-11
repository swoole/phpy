# Guide utilisateur

Le but de cette bibliothèque est d'utiliser l'écosystème Python pour combler les lacunes du PHP. Si une fonction ou caractéristique existe déjà en PHP, il suffit d'utiliser directement le langage PHP. Sinon, on peut chercher dans l'écosystème Python les bibliothèques disponibles.

`phpy` n'est que l'importation des bibliothèques Python dans l'écosystème PHP, mais la syntaxe utilisée est entièrement PHP, sans coût d'apprentissage supplémentaire.

En Python, tout est objet, que ce soit les modules, les classes, les fonctions, les entiers, les浮点数, `None`, les valeurs booléennes, les objets, les dictionnaires, les listes, les ensembles, les tuples, tout est une instance de `PyObject`.

Généralement, ce que nous faisons en programmation se résume à quatre choses :

- `PyCore::import()` pour importer un paquet
- Appeler une méthode d'un objet : `$object->fn()`
- Lire ou écrire une propriété d'un objet : `$object->attr` et `$object->attr = $value`
- Appeler une fonction intégrée `PyCore::$fn()` pour réaliser certaines fonctions de base, par exemple `import()` est en fait une fonction intégrée.

## Exemple

```php
// Importer le paquet Python os
$os = PyCore::import('os');
// Appeler une fonction
$uname = $os->uname();
// Lire une propriété
echo $uname->sysname; 
// Imprimer
echo strval(PyCore::str($uname));
```
