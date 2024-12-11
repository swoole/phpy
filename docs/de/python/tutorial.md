# Nutzung von PHP-Funktionen in Python

In Python-Code werden PHP-Funktionen aufgerufen. Der Modulname lautet `phpy`, importieren kann man es einfach.

- [Funktionsliste](function.md)

- [Objektoperationen](object.md)

- [Klassensystem](class.md)

- [Referenzdatenarten](reference.md)
- [Modulverpackung](module.md)

## Beispiel
```python
from php import curl

ch = curl.init("https://www.baidu.com/")
curl.setopt(ch, curl.CURLOPT_RETURNTRANSFER, True)
rs = curl.exec(ch)
print(rs)
```

Im obigen Code wurde die `PHP`-`curl`-Erweiterung verwendet, um die Startseite von Baidu zu anfordern.

## Modulverpackung
Neben dem direkten Nutzen des `phpy`-Moduls kann man auch die durch Reflektionswerkzeuge automatisch generierten Verpackungsmodule verwenden.

### Generierung
```shell
php tools/gen-pymod.php
```

### Nutzung
```python
from php import curl

ch = curl.init("https://www.baidu.com/")
curl.setopt(ch, curl.CURLOPT_RETURNTRANSFER, True)
rs = curl.exec(ch)
print(rs)
```
