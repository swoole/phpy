Pythonモジュールの構築
=====================
PythonでPHPの関数を呼び出すためには、まずPythonの`phpy`モジュールを構築する必要があります。

## 編译依存

- cmake 3.16またはそれ以上

- PHP 8.1 (embed)またはそれ以上、PHPを編译する際には`--enable-embed`パラメータを追加する必要があります
- Python 3.8またはそれ以上、`python3-dev`をインストールする必要があります

## 編译設定

### `PHP_CONFIG`

`php-config`指令のpathを指定します。デフォルトは相対pathです。例えば：

```shell
cmake . -D PHP_CONFIG=/usr/local/php/bin/php-config
```

### `PYTHON_CONFIG`

`python-config`指令のpathを指定します。デフォルトは相対pathです。例えば：

```shell
cmake . -D PYTHON_CONFIG=/usr/local/bin/python3-config
```

## 構築
```shell
make -j 4
```

編译が成功すると`lib`ディレクトリに`phpy.so`が生成されます。このファイルを任意のPythonの`sys.path`ディレクトリにコピーすることができます。

## condaツール

Python環境を管理するためにcondaツールを使用できます。

### Python環境の作成

```shell
conda create -n py38 python=3.8
# 活性化
conda activate py38
```

### `pip`加速
```shell
# 阿里云
pip config set global.index-url https://mirrors.aliyun.com/pypi/simple
# 清华源
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
```

## 单元テスト
```shell
pip install pytest
pytest -v tests/
```
