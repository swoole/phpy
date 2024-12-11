# パッケージの封装
 `phpy` は反射ツールを使用して自動的にすべての `PHP` 拡張関数とクラスを封装モジュールに生成し、パッケージ名は `php`で直接使用できます。

```python
from php import [拡張名]
```

で `PHP` 拡張で定義された定数、関数、クラスをインポートすることができます。

## 命名規則

- モジュール名はすべて小文字を使用し、例えば `PDO` の場合、対応するモジュールは `php.pdo`です。

-標準ライブラリの関数は `php.std` モジュールにあり、例えば `php.std.file_get_contents()`です。

- 言語コアの関数は `php.core` モジュールにあり、例えば `php.core.get_included_files()`です。

- 関数のプレフィックスが拡張名と一致する場合、拡張名前缀を省略できます。例えば、`php.curl.curl_init()`は `php.curl.init()`と短縮されます。

- クラス名はネームスペースを使用し、拡張名と一致する場合、CamelCaseのクラス名に変わります。例えば、`Swoole\Http\Server`は `php.swoole.HttpServer`になります。

- 関数名がネームスペースを使用する場合、Snake_caseの関名に変わります。例えば、`MongoDB\BSON\fromJSON`は `php.mongodb.bson_fromjson`になります。

- 関数またはメソッド名が `Python` キーワードの場合、自動的にアンダーバーを前に付けられます。例えば、`gmp_import`は `php.gmp._import`になります。

## オブジェクトインスタンス

```python
from php import redis

db = redis.Redis()
db.connect("127.0.0.1", 6379, -1)
db.set("key", "swoole")
print(db.get("key"))
```

## 関数インスタンス

```python
from php import std
import phpy

errno = phpy.Reference()
errstr = phpy.Reference()
rs = std.stream_socket_client('tcp://127.0.0.1:9999', errno, errstr, 30)
```
