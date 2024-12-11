# Verpackungsmodule
Das `phpy`-Modul verwendet Reflektionswerkzeuge, um automatisch alle PHP-Erweiterungsfunktionen und -klassen in Verpackungsmodule zu generieren. Der Paketname ist `php`, und es kann direkt verwendet werden, um Konstanten, Funktionen und Klassen zu importieren, die in PHP-Erweiterungen definiert sind.

```python
from php import [ext-name]
```

## Namensregeln

- Modulnamen verwenden ausschließlich kleine Buchstaben, zum Beispiel `PDO`, das entsprechende Modul ist `php.pdo`.

- Standardbibliotheksfunktionen befinden sich im `php.std`-Modul, zum Beispiel `php.std.file_get_contents()`.

- Kernfunktionen der Sprache befinden sich im `php.core`-Modul, zum Beispiel `php.core.get_included_files()`.

- Wenn der Funktionspräfix mit dem Erweiterungstitel übereinstimmt, wird der Präfix des Erweiterungstitels weggelassen, zum Beispiel `php.curl.curl_init()` sollte als `php.curl.init()` abgekürzt werden.

- Wenn der Klassennamen einen Namespace verwendet und mit dem Erweiterungstitel übereinstimmt, wird er zu einem CamelCase-Klassennamen umgewandelt, zum Beispiel `Swoole\Http\Server` wird zu `php.swoole.HttpServer`.

- Wenn der Funktionsname einen Namespace verwendet, wird er zu einem snake_case-Funktionsnamen umgewandelt, zum Beispiel `MongoDB\BSON\fromJSON` wird zu `php.mongodb.bson_fromjson`.

- Wenn der Funktions- oder Methodenname ein Python-Schlüsselwort ist, wird automatisch ein Unterstrich vorangefügt, zum Beispiel `gmp_import` wird zu `php.gmp._import`.

## Objektinstanzierung

```python
from php import redis

db = redis.Redis()
db.connect("127.0.0.1", 6379, -1)
db.set("key", "swoole")
print(db.get("key"))
```

## Funktionsinstanzierung

```python
from php import std
import phpy

errno = phpy.Reference()
errstr = phpy.Reference()
rs = std.stream_socket_client('tcp://127.0.0.1:9999', errno, errstr, 30)
```
