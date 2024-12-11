# Opérations de chaînes
Le type de chaîne `phpy.String` est similaire à un tableau d'octets en `Python`. Le contenu ne contient pas d'informations sur l'encodage et peut contenir du contenu binaire.
Il n'est pas équivalent au type `str` en `Python`. La couche sous-jacente de `phpy` fournit une API de style `str` pour manipuler les chaînes.

## Création
```python
s1 = phpy.String("hello world")
s2 = phpy.call("random_bytes", 128)
```

## Longueur
```python
print(len(s1))
print(len(s2))
```

## Addition
```python
# Ajouter une chaîne
s1 += "hello"
# Ajouter des bytes
s1 += b"world"
# Ajouter une autre phpy.String
s1 += phpy.String(", php est la meilleure langue de programmation")
```

## Contenu
```python
# Retourne True
print(s1.__contains__("php")) 
# Retourne False
print(s1.__contains__("java"))
```

## Comparaison
```python
s3 = phpy.String("hello")
if s3 == "hello":
    print("==")
```

## Récupération de bytes
```python
print(s1[2])
```

Veuillez noter que la forme de retour de `phpy.String` est cohérente avec celle des `bytes`, c'est un `uchar`.
Contrairement à `str`, qui traite l'encodage `UTF-8` et retourne un caractère large `UTF-8`, par exemple `str('中国')[0]` retourne `中`.

## Conversion en type `bytes` de `Python`

```python
print(bytes(s1))
```

> Veuillez noter qu'une copie de mémoire se produira ici
