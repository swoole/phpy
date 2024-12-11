# Funktionsliste



## include Lade Datei
Das `phpy` Modul bietet Funktionen zur加载ausführung von `PHP`-Code.
```python
phpy.include("vendor/autoload.php")
```


## globals Erhalte globale Variablen
```python
print(phpy.globals("_ENV"))
```
Bitte beachten Sie, dass Sie beim Namen der Variablen das `$`-Zeichen nicht hinzufügen sollten.


## constant Erhalte den Wert einer Konstante
```python
print(phpy.constant("PHP_OS"))
```


## eval Ausführen eines Abschnitts `PHP`-Code

```python
phpy.eval("var_dump(get_loaded_extensions());")
```


## call Aufrufen einer `PHP`-Funktion

Kann sowohl eine Erweiterungsfunktion als auch eine benutzerdefinierte Funktion sein. Der erste Parameter ist der Name der Funktion, der als String angegeben werden muss. Die anderen Parameter werden als Argumente für die aufgerufene `PHP`-Funktion übergeben.


- Wenn ein Parameter ein Verweistyp ist, kann er mit `phpy.Reference()` umhüllt werden, um dies zu erreichen
- Es ist möglich, statische Methoden von Klassen aufzurufen, zum Beispiel: `phpy.call("Test::main"))`

```python
print(phpy.call("file_get_contents", "/tmp/file.txt"))
```
