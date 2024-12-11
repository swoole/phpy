# noyau

Tous les fonctions intégrées de `Python` sont disponibles en tant que méthodes statiques de la classe `PyCore`. Pour référence sur l'utilisation des méthodes intégrées, veuillez consulter la documentation de `Python`.

## Importation de packages
```php
$os = PyCore::import('os');
```

Après un succès, cela retourne un objet `PyModule`. Il est possible d'importer des packages intégrés de `Python`, ainsi que des packages tiers ou des packages personnalisés par l'utilisateur.

Il est possible de charger des modules uniquement, il n'est pas supporté la syntaxe `from module import class` en `Python`. Il est possible d'utiliser la syntaxe suivante à la place.

```php
$module = PyCore::import($moduleName);
$class = $module->$className;
```

Le niveau sous-jacent de `Python` cache les modules déjà chargés. Lors de la charge suivante, le module est automatiquement retourné à partir du cache, sans être chargé à nouveau. Par conséquent, cela peut également être utilisé dans des environnements à courte durée de vie comme `PHP-FPM/Apache`, sans aucun problème de performance.

## Chemin de chargement
Il est possible d'ajouter certains répertoires au chemin de chargement en utilisant `PyCore::import('sys')->path->append()`. Par exemple, pour charger un package personnalisé comme `/workspace/app/user.py`, vous pouvez suivre les étapes suivantes :

1. `PyCore::import('sys')->path->append('/workspace')` ajouter `/workspace` au chemin `sys.path`
2. `PyCore::import('app.user')` rechercher automatiquement dans le chemin `sys.path` et charger le package correspondant à `app/user.py`

## Méthodes intégrées

- `PyCore::import($module)` charger un module

- `PyCore::str()` transformer un objet en chaîne de caractères

- `PyCore::repr()` 

- `PyCore::type()` obtenir le type de l'objet

- `PyCore::locals()` obtenir toutes les variables locales du contexte actuel

- `PyCore::globals()` obtenir toutes les variables globales

- `PyCore::hash()` obtenir la valeur de hachage

- `PyCore::hasattr()` vérifier si l'objet possède une propriété spécifique

- `PyCore::id()` obtenir le numéro d'intérieur de l'objet

- `PyCore::len()` obtenir la longueur

- `PyCore::dir()` obtenir toutes les propriétés et méthodes de l'objet

- `PyCore::int()` construire un entier

- `PyCore::float()` construire un nombre à virgule flottante

- `PyCore::fn()` construire une fonction callable

- `PyCore::eval()` exécuter du code `Python`

- `PyCore::dict()` construire un objet dictionnaire

- `PyCore::set()` construire un objet ensemble

- `PyCore::range()` construire une séquence de plage

- `PyCore::scalar($pyobj)` transformer un objet `PyObject` en un type scalaire PHP, par exemple `PyStr` sera transformé en chaîne de caractères PHP, `Dict/Tuple/Set/List` seront transformés en `Array`
- `PyCore::fileno($fp)` obtenir le numéro de fichier du ressources `PHP Stream`, veuillez noter que cela ne prend en charge que les ressources de type `tcp/udp/unix`

> La classe `PyCore` a réalisé la méthode magique `__callStatic()`, ce qui permet d'appeler automatiquement la méthode correspondante du module `builtins` en `Python` lors de l'appel d'une méthode statique de `PyCore`. Pour plus d'informations sur l'utilisation des méthodes intégrées, veuillez consulter [Built-in Functions](https://docs.python.org/3/library/functions.html).

## Probleme de bibliothèque dynamique
L'importation de bibliothèques peut provoquer des erreurs de bibliothèque dynamique, en raison d'une mauvaise configuration du chemin `LD`. Il est possible de setting l'environnement pour indiquer le chemin des bibliothèques dynamiques des modules `C` de `Python`.

> Il est possible d'utiliser `:` pour séparer plusieurs chemins lors de l'établissement.

```shell
# Utiliser uniquement l'environnement base de anaconda3
export LD_LIBRARY_PATH=/opt/anaconda3/lib
# Utilisation d'un environnement particulier, nommé cef
export LD_LIBRARY_PATH=/opt/anaconda3/envs/cef/lib:/opt/anaconda3/lib
php plot.php
```

Cette méthode est uniquement valide pour la session actuelle de `bash` et n'affecte pas le système global. Il n'est pas approprié de modifier directement `/etc/ld.so.conf.d/*.conf` pour ajouter `/opt/anaconda3/lib`, car cela pourrait entraîner des conflits avec la bibliothèque `libc` et affecter le fonctionnement normal d'autres programmes de l'opération systeme.

## Sensibilité à la casse
Tous les noms de fonctions, méthodes, variables et propriétés en `Python` sont entièrement sensibles à la casse. Lors de l'appel, il est nécessaire d'utiliser le nom exactement comme en `Python`.

Par exemple :

```python
def TestUser():
    pass
```

Dans le code `PHP`, il est nécessaire d'utiliser `$module->TestUser()`, mentre d'autres formes telles que `$module->testUser()` ou `$module->testuser()` sont des écritures erronées.

## Variables d'environnement
Dans `phpy`, l'environnement `os.environ` de `Python` n'est pas initialisé automatiquement, donc `environ` est un dictionnaire vide. Il est nécessaire de parcourir `$_ENV` pour injecter les variables d'environnement dans l'environnement `Python`.

```php
$os = PyCore::import('os');
foreach($_ENV as $k => $v) {
    $os->environ->__setitem__($k, $v);
}
```

## undefined symbol:ffi_type_uint32, version LIBFFI_BASE_7.0
Problème de conflit de chemin de bibliothèque dynamique, essayez la méthode suivante pour résoudre. Si le problème persiste, il est conseillé d'utiliser l'environnement `Python` fourni par le système plutôt que celui créé par `conda`.

```shell
export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libffi.so.7
```

## Échec de l'importation
Dans la plupart des cas, `from a import b` est équivalent à `PyCore::import('a')->b`, mais certaines bibliothèques spéciales ne peuvent pas être chargées correctement par la méthode ci-dessus. Il est possible de les remplacer par la méthode suivante :

```php
# Incapable de charger
$b = PyCore::import('a')->b;
# Remplacer par le code suivant
$b = PyCore::import('a.b');
```
