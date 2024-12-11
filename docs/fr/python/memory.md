# Copie de mémoire

Lorsque le code `Python` appelle une fonction/méthode `PHP`, il peut y avoir des copies de mémoire pour les arguments et les valeurs de retour, ce qui est important à prendre en compte pour les performances dans les programmes sensibles au temps.

## Arguments

- Les types intégres, booléens, flottants et `None` sont toujours transmis par valeur.
- Les objets, ressources et références sont toujours transmis par référence, sans copie de mémoire.
- Les chaînes et les tableaux subissent une copie profonde recursive pour être convertis en types natifs.

```python
arg1 = 1234
arg2 = 1234.5678
arg3 = True

arg4 = phpy.Object('stdClass')
arg5 = phpy.Reference()
arg6 = phpy.call('fopen', "php://input", "r")

arg7 = {'hello' : 'world'}
arg8 = "hello world"
arg9 = [1, 2, 3, 4, 5]

phpy.call('test', arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9)
```

- `arg1`, `arg2`, `arg3` seront convertis en types intégres, flottants et booléens en PHP, avec une simple copie de la valeur numérique.
- `arg4`, `arg5`, `arg6` seront transmis directement par référence en PHP, sans création de copies de mémoire.
- `arg6`, `arg7`, `arg8` seront parcourus et deep copied pour être convertis en `array` et `string` en PHP.

## Valeurs de retour

- Les types intégres, booléens, flottants et `None` (ainsi que `null`) seront convertis en types natifs Python.
- Tout le reste du contenu returned de Python est de type `PyObject`.
- Il est également possible d'utiliser le type d'objet `PyObject` en PHP pour retourner des types natifs Python, permettant une transmission transparente et indirecte.

## Éviter les copies de mémoire
En utilisant des objets `phpy.String` et `phpy.Array`, il n'y aura pas de copie de mémoire lors de l'appel de fonctions PHP.
