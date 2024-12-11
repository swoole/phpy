# Opérations sur les tableaux

`phpy.Array` est un type hétérogène qui peut être soit un `List` soit un `Map`.

## Création
```python
# List
l = phpy.Array([1, 3, 5, 2023, 7, 9])
# Map
m = phpy.Array({"hello": "world", "php": "swoole"})
```

## Lecture
```python
print(l[3])
print(m["php"])
```

## Longueur
```python
print(len(l))
print(len(m))
```

## Écriture
```python
# Établir une valeur par clé
m["swoole"] = 'coroutine'
# Ajouter un élément à la fin
l.append(9999)
```

## Autres méthodes

- `get(key)` pour la lecture

- `set(key, value)` pour l'écriture

- `unset(key)` pour la suppression

- `append(value)` pour ajouter un élément à la fin de la liste

- `count()` pour la lecture du nombre d'éléments
- `collect()` pour se transformer en un `dict` ou `list`原生 de `Python`
- `is_list()` pour vérifier si l'array est un `List`
