Construire un module Python
=======================
Pour appeler des fonctions PHP depuis Python, il est nécessaire de construire d'abord le module Python `phpy`.




## Dépendances de compilation

- `cmake 3.16` ou une version supérieure

- `php 8.1 (embed)` ou une version supérieure, en compilant PHP, il faut ajouter l'option `--enable-embed`
- `Python 3.8` ou une version supérieure, il faut installer `python3-dev`


## Configuration de compilation


### `PHP_CONFIG`

Spécifiez le chemin de la directive `php-config`, par défaut est un chemin relatif, par exemple :

```shell
cmake . -D PHP_CONFIG=/usr/local/php/bin/php-config
```


### `PYTHON_CONFIG`

Spécifiez le chemin de la directive `python-config`, par défaut est un chemin relatif, par exemple :

```shell
cmake . -D PYTHON_CONFIG=/usr/local/bin/python3-config
```


## Construction
```shell
make -j 4
```

Après une compilation réussie, le fichier `phpy.so` sera généré dans le répertoire `lib`. Ce fichier peut être copié dans n'importe quel répertoire de `sys.path` de Python.


## Outils conda

Il est possible d'utiliser les outils `conda` pour gérer l'environnement Python.


### Créer un environnement Python

```shell
conda create -n py38 python=3.8
# Activer
conda activate py38
```


### Accélération de `pip`
```shell
# Source Aliyun
pip config set global.index-url https://mirrors.aliyun.com/pypi/simple
# Source Tsinghua
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
```

## Tests unitaires
```shell
pip install pytest
pytest -v tests/
```
