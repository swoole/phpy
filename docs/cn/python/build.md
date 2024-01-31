构建 Python 模块
====
在 `Python` 中调用 `PHP` 的函数时需要先构建 `Python` 的 `phpy` 模块。

## 编译依赖
- `cmake 3.16` 或更高版本
- `php 8.1 (embed)` 或更高版本，编译 `PHP` 时需要增加 `--enable-embed` 参数
- `Python 3.8` 或更高版本,需要安装 `python3-dev`

## 编译配置

### `PHP_CONFIG` 

指定 `php-config` 指令的路径，默认为相对路径，例如：

```shell
cmake . -D PHP_CONFIG=/usr/local/php/bin/php-config
```

### `PYTHON_CONFIG`

指定 `python-config` 指令的路径，默认为相对路径，例如：

```shell
cmake . -D PYTHON_CONFIG=/usr/local/bin/python3-config
```

## 构建
```shell
make -j 4
```

编译成功后在 `lib` 目录下会生成 `phpy.so`，可以将此文件复制到任意 `Python` 的 `sys.path` 目录中。

## conda 工具

可使用 `conda` 工具来管理 `Python` 环境。

### 创建 `Python` 环境

```shell
conda create -n py38 python=3.8
# 激活
conda activate py38
```

### `pip` 加速
```shell
# 阿里云
pip config set global.index-url https://mirrors.aliyun.com/pypi/simple
# 清华源
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
```

## 单元测试
```shell
pip install pytest
pytest -v tests/
```
