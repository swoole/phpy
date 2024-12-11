# Module d'encapsulation
Le module `phpy` utilise des outils de réflexion pour générer automatiquement des modules d'encapsulation pour toutes les fonctions et classes de extensions PHP, avec le nom de package `php` qui peut être utilisé directement

```python
from php import [ext-name]
```

Pour importer les constantes, fonctions et classes définies dans l'extension PHP.

## Règles de nommage

- Le nom du module est entièrement en lowercase, par exemple `PDO`, le module correspondant est `php.pdo`

- Les fonctions de la bibliothèque standard sont dans le module `php.std`, par exemple `php.std.file_get_contents()`

- Les fonctions du cœur de la langue sont dans le module `php.core`, par exemple `php.core.get_included_files()`

- Lorsque le préfixe de la fonction correspond au nom de l'extension, le préfixe de l'extension est omis, par exemple `php.curl.curl_init()` doit être abrégé en `php.curl.init()`

- Lorsque le nom de la classe utilise un espace de nom et correspond au nom de l'extension, il est transformé en nom de classe en camelCase, par exemple `Swoole\Http\Server` devient `php.swoole.HttpServer`

- Lorsque le nom de la fonction utilise un espace de nom, il est transformé en nom de fonction en snake_case, par exemple `MongoDB\BSON\fromJSON` devient `php.mongodb.bson_fromjson`

- Lorsque le nom de la fonction ou de la méthode est une keyword Python, un préfixe d'underscore est automatiquement ajouté, par exemple `gmp_import` devient `php.gmp._import`

## Instances d'objets

```python
from php import redis

db = redis.Redis()
db.connect("127.0.0.1", 6379, -1)
db.set("key", "swoole")
print(db.get("key"))
```

## Instances de fonctions

```python
from php import std
import phpy

errno = phpy.Reference()
errstr = phpy.Reference()
rs = std.stream_socket_client('tcp://127.0.0.1:9999', errno, errstr, 30)
```
