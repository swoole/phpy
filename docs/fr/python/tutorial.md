# Utiliser les fonctionnalités de PHP dans Python

Appeler des fonctions PHP dans du code Python. Le module est nommé `phpy`, il suffit d'y faire importation.

- [Liste des fonctions](function.md)

- [Opérations sur les objets](object.md)

- [Opérations sur les classes](class.md)

- [Types de référence](reference.md)
- [Gestion des modules](module.md)

## Exemple
```python
from php import curl

ch = curl.init("https://www.baidu.com/")
curl.setopt(ch, curl.CURLOPT_RETURNTRANSFER, True)
rs = curl.exec(ch)
print(rs)
```

Dans le code ci-dessus, nous avons utilisé l'extension `curl` de PHP pour demander le contenu du site Baidu.

## Gestion des modules
En plus d'utiliser directement le module `phpy`, on peut également utiliser des modules encapsulés générés automatiquement par des outils de réflexion.

### Génération
```shell
php tools/gen-pymod.php
```

### Utilisation
```python
from php import curl

ch = curl.init("https://www.baidu.com/")
curl.setopt(ch, curl.CURLOPT_RETURNTRANSFER, True)
rs = curl.exec(ch)
print(rs)
```
