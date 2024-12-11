Построение Python модуля
================
При вызове функций PHP из Python необходимо сначала построить модуль Python `phpy`.




## Требования к сборке

- `cmake 3.16` или выше

- `php 8.1 (embed)` или выше, при сборке PHP необходимо добавить параметр `--enable-embed`
- `Python 3.8` или выше, необходимо установить `python3-dev`


## Конфигурация сборки


### `PHP_CONFIG`

Указывает путь к команде `php-config`, по умолчанию относительный путь, например:

```shell
cmake . -D PHP_CONFIG=/usr/local/php/bin/php-config
```


### `PYTHON_CONFIG`

Указывает путь к команде `python-config`, по умолчанию относительный путь, например:

```shell
cmake . -D PYTHON_CONFIG=/usr/local/bin/python3-config
```


## Сборка
```shell
make -j 4
```

После успешной сборки в каталоге `lib` будет создан файл `phpy.so`, который можно скопировать в любой каталог `sys.path` Python.


## Инструменты conda

Можно использовать инструменты conda для управления окружениями Python.


### Создание Python окружения

```shell
conda create -n py38 python=3.8
# Активация
conda activate py38
```


### Ускорение pip
```shell
# Aliyun
pip config set global.index-url https://mirrors.aliyun.com/pypi/simple
# Tsinghua Source
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
```

## Unit tests
```shell
pip install pytest
pytest -v tests/
```
