Building a Python Module
====
When calling PHP functions from Python, you need to build the `phpy` module for Python.

## Compilation Dependencies

- `cmake 3.16` or higher

- `php 8.1 (embed)` or higher, you need to add the `--enable-embed` parameter when compiling PHP
- `Python 3.8` or higher, you need to install `python3-dev`

## Compilation Configuration

### `PHP_CONFIG` 

Specify the path to the `php-config` command, default is relative path, for example:

```shell
cmake . -D PHP_CONFIG=/usr/local/php/bin/php-config
```

### `PYTHON_CONFIG`

Specify the path to the `python-config` command, default is relative path, for example:

```shell
cmake . -D PYTHON_CONFIG=/usr/local/bin/python3-config
```

## Build
```shell
make -j 4
```

After successful compilation, `phpy.so` will be generated in the `lib` directory, and this file can be copied to any directory in Python's `sys.path`.

## conda Tool

You can use the `conda` tool to manage Python environments.

### Create Python Environment

```shell
conda create -n py38 python=3.8
# Activate
conda activate py38
```

### `pip` Acceleration
```shell
# Aliyun
pip config set global.index-url https://mirrors.aliyun.com/pypi/simple
# Tsinghua Source
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
```

## Unit Testing
```shell
pip install pytest
pytest -v tests/
```
