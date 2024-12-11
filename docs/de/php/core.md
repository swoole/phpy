# Kern

Alle eingebauten Funktionen von `Python` sind als statische Methoden der `PyCore`-Klasse implementiert. Referenz für die Verwendung eingebauter Methoden finden Sie in der `Python`-Dokumentation.


## Importieren von Paketen
```php
$os = PyCore::import('os');
```

Erfolgreich zurückgegeben wird ein `PyModule`-Objekt. Man kann sowohl eingebundene `Python`-Pakete importieren als auch Drittanbieter-Pakete oder von Benutzern自定义的Pakete.

Es ist nur möglich, Module zu laden, die `Python`-Syntax `from module import class` wird nicht unterstützt. Stattdessen kann man die folgende Syntax verwenden:

```php
$module = PyCore::import($moduleName);
$class = $m->$className;
```

Die `Python`-Unterseite cacht bereits geladene Module, und wenn sie das zweite Mal geladen werden, wird sie automatisch aus dem Cache zurückgegeben und nicht erneut geladen. Daher kann es auch in Umgebungen mit kurzer Lebensdauer wie `PHP-FPM/Apache` verwendet werden, ohne dass es Performanceprobleme gibt.


## Ladepfade
Man kann directories hinzufügen, indem man `PyCore::import('sys')->path->append()` verwendet.
Zum Beispiel kann ein vom Benutzer自定义的Package wie `/workspace/app/user.py` auf die folgenden Weise geladen werden:

1. `PyCore::import('sys')->path->append('/workspace')` fügt `/workspace` hinzu
2. `PyCore::import('app.user')` sucht automatisch im `sys.path` nach dem entsprechenden `app/user.py` Package und lädt es ein




## eingebauten Methoden

- `PyCore::import($module)` lädt ein Modul ein

- `PyCore::str()` konvertieren Sie ein Objekt in einen String

- `PyCore::repr()` 

- `PyCore::type()` erhalten Sie den Typ des Objekts

- `PyCore::locals()` erhalten Sie alle lokalen Variablen des aktuellen Rauminhaltes

- `PyCore::globals()` erhalten Sie alle globalen Variablen

- `PyCore::hash()` erhalten Sie den Hashwert

- `PyCore::hasattr()` überprüfen Sie, ob ein Objekt eine bestimmte Eigenschaft hat

- `PyCore::id()` erhalten Sie die interne Nummer des Objekts

- `PyCore::len()` erhalten Sie die Länge

- `PyCore::dir()` erhalten Sie alle Eigenschaften und Methoden des Objekts

- `PyCore::int()` erstellen Sie ein Integer

- `PyCore::float()` erstellen Sie eine Floating-Point-Zahl

- `PyCore::fn()` erstellen Sie eine callable Funktion

- `PyCore::eval()` führen Sie Python-Code aus

- `PyCore::dict()` erstellen Sie ein Dictionary-Objekt

- `PyCore::set()` erstellen Sie ein Set-Objekt

- `PyCore::range()` erstellen Sie eine Range-Sequenz

- `PyCore::scalar($pyobj)` konvertieren Sie ein `PyObject` in einen PHP-Scalartyp, zum Beispiel wird `PyStr` zu einem `PHP String`, `Dict/Tuple/Set/List` zu einem `Array`
- `PyCore::fileno($fp)` erhalten Sie den Dateideskriptor des PHP Stream-Ressourcen, beachten Sie, dass nur Ressourcen der Typen `tcp/udp/unix` unterstützt werden

> `PyCore` implementiert die magische Methode `__callStatic()`, so dass bei der Ausführung statischer Methoden von `PyCore` automatisch die entsprechenden Methoden aus dem `builtins`-Modul von `Python` aufgerufen werden,
> zum Verstehen der Verwendung anderer eingebauter Methoden siehe [Built-in Functions](https://docs.python.org/3/library/functions.html)


## Probleme mit dynamischen Linker-Bibliotheken
Beim Importieren von Bibliotheken treten Fehler bei der dynamischen Linker-Bibliothek auf, was möglicherweise auf einen falschen `LD`-Pfad zurückzuführen ist. Man kann die Umgebungsvariable `LD_LIBRARY_PATH` festlegen, um den Pfad zur dynamischen Bibliothek der `Python C Module` anzugeben.

> Verwenden Sie `:` zum Trennen mehrerer Pfade

```shell
# Nur die base Umgebung von anaconda3 verwenden
export LD_LIBRARY_PATH=/opt/anaconda3/lib
# Eine besondere Umgebung namens cef verwenden
export LD_LIBRARY_PATH=/opt/anaconda3/envs/cef/lib:/opt/anaconda3/lib
php plot.php
```

Diese Methode ist nur für die aktuelle `bash`-Sitzung wirksam und beeinflusst nicht das globale System. Bearbeiten Sie nicht direkt `/etc/ld.so.conf.d/*.conf`, um `/opt/anaconda3/lib` hinzuzufügen, da dies möglicherweise zu Konflikten mit der `libc`-Bibliothek führen kann und die normale Funktion anderer Betriebssystemprogramme beeinträchtigen könnte.


## Sensibilität gegenüber Groß-/Kleinschreibung
In `Python` sind alle Funktionen, Methoden, Variablen und Eigenschaften in ihrer Benennung vollständig klein- und großgeschrieben, und beim Aufrufen müssen Sie den genauen Namen verwenden, der in `Python` verwendet wird.

Zum Beispiel:

```python
def TestUser():
    pass
```

In PHP-Code muss man `$module->TestUser()` verwenden, andere写法 wie `$module->testUser()` oder `$module->testuser()` sind falsche Schreibweisen.


## Umgebungsvariablen
In `phpy` wurde die `os.environ` von `Python` nicht automatisch initialisiert, daher ist `environ` ein leeres Dictionary. Man muss die Umgebungsvariablen aus `$_ENV` iterieren und in die Python-Umwelt einbringen.

```php
$os = PyCore::import('os');
foreach($_ENV as $k => $v) {
    $os->environ->__setitem__($k, $v);
}
```


## undefined symbol:ffi_type_uint32, version LIBFFI_BASE_7.0
Es gibt ein Konfliktproblem mit dem Pfad der dynamischen Linker-Bibliothek, das durch die folgenden Methoden gelöst werden kann.
Wenn das Problem weiterhin besteht, wird empfohlen, die von System bereitgestellte Python-Umwelt anstelle der von conda erstellten Umgebung zu verwenden.

```shell
export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libffi.so.7
```

## Importieren fehlgeschlagen
In den meisten Fällen ist `from a import b` gleichbedeutend mit `PyCore::import('a')->b`, aber einige spezielle Bibliotheken können nicht auf die oben genannte Weise richtig geladen werden. Stattdessen kann man die folgende Methode verwenden:

```php
# Nicht geladen
$b = PyCore::import('a')->b;
# Ersetzen Sie dies durch den folgenden Code
$b = PyCore::import('a.b');
```
