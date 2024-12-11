Bauen Sie ein Python-Modul
======================
Um Funktionen in PHP aus Python aufzurufen, muss zuerst das Python-Modul `phpy` gebaut werden.




## Abhängigkeiten für die Kompilierung

- `cmake 3.16` oder höher

- `PHP 8.1 (embed)` oder höher, beim Kompilieren von PHP muss der `--enable-embed` Parameter angegeben werden
- `Python 3.8` oder höher, ist `python3-dev` erforderlich


## Kompilierungsconfig


### `PHP_CONFIG`

Geben Sie den Pfad zur `php-config`-Befehlsanweisung an, standardmäßig ist dies ein relativer Pfad, zum Beispiel:

```shell
cmake . -D PHP_CONFIG=/usr/local/php/bin/php-config
```


### `PYTHON_CONFIG`

Geben Sie den Pfad zur `python-config`-Befehlsanweisung an, standardmäßig ist dies ein relativer Pfad, zum Beispiel:

```shell
cmake . -D PYTHON_CONFIG=/usr/local/bin/python3-config
```


## Erstellung
```shell
make -j 4
```

Nach erfolgreicher Kompilierung wird im `lib`-Verzeichnis `phpy.so` generiert, dieser Dateien kann in ein beliebiges Verzeichnis aus dem `sys.path` von Python kopiert werden.


## conda-Tools

Möchten Sie die Python-Umwelt mit `conda`-Tools verwalten?


### Erstellen einer Python-Umwelt

```shell
conda create -n py38 python=3.8
# Aktivieren
conda activate py38
```


### Beschleunigung von `pip`
```shell
# Alibaba Cloud
pip config set global.index-url https://mirrors.aliyun.com/pypi/simple
# Tsinghua Source
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
```

## Einheitstests
```shell
pip install pytest
pytest -v tests/
```
