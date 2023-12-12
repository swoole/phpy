# 在 Python 使用 PHP 的功能

在 `Python` 代码中调用 `PHP` 的函数。模块名称为 `phpy`，导入即可。

- [函数列表](function.md)
- [对象操作](object.md)
- [类操作](class.md)
- [引用类型](reference.md)
- [封装模块](module.md)


## 例子
```python
from php import curl

ch = curl.init("https://www.baidu.com/")
curl.setopt(ch, curl.CURLOPT_RETURNTRANSFER, True)
rs = curl.exec(ch)
print(rs)
```

在上面的代码中我们使用了 `PHP` 的 `curl` 扩展，请求了百度首页。

## 封装模块
除了直接使用 `phpy` 模块外，也可以使用反射工具自动生成的封装模块。

### 生成
```shell
php tools/gen-pymod.php
```

### 使用
```python
from php import curl

ch = curl.init("https://www.baidu.com/")
curl.setopt(ch, curl.CURLOPT_RETURNTRANSFER, True)
rs = curl.exec(ch)
print(rs)
```
