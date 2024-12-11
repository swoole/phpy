# PythonでPHPの機能を使う

Pythonコード内でPHPの関数を呼び出すことができます。モジュール名は`phpy`です。

- [関数リスト](function.md)

- [オブジェクト操作](object.md)

- [クラス操作](class.md)

- [参照タイプ](reference.md)
- [モジュール封装](module.md)

## 例
```python
from php import curl

ch = curl.init("https://www.baidu.com/")
curl.setopt(ch, curl.CURLOPT_RETURNTRANSFER, True)
rs = curl.exec(ch)
print(rs)
```
上記のコードでは、PHPの`curl`拡張を使用して百度のホームページをリクエストしました。

## モジュール封装
`phpy`モジュールを直接使用するだけでなく、反射ツールで自動生成された封装モジュールを使用することもできます。

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
