# Liste des fonctions



## include charger un fichier
Le module `phpy` fournit des fonctions pour charger et exécuter du code PHP.
```python
phpy.include("vendor/autoload.php")
```


## globals obtenir une variable globale
```python
print(phpy.globals("_ENV"))
```
Veuillez noter que l'名称 de la variable ne doit pas contenir le symbole `$`


## constant obtenir la valeur d'une constante
```python
print(phpy.constant("PHP_OS"))
```


## eval exécuter un morceau de code PHP

```python
phpy.eval("var_dump(get_loaded_extensions());")
```


## call appeler une fonction PHP

Cela peut être une fonction d'extension ou une fonction définie par l'utilisateur. Le premier argument est le nom de la fonction, qui doit être une chaîne de caractères. Les autres arguments seront transmis comme paramètres à la fonction PHP appelée.


- Si un argument est de type référence, vous pouvez l'envelopper avec `phpy.Reference()` pour l'implémenter
- Il est possible d'appeler des méthodes statiques de classes, par exemple : `phpy.call("Test::main"))`

```python
print(phpy.call("file_get_contents", "/tmp/file.txt"))
```
