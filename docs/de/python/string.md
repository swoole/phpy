# Zeichenoperationen
Die `phpy.String`-Zeichenart entspricht einer Bytearray in `Python`. Der Inhalt enthält keine Kodierungsinformation und kann binäre Inhalte enthalten.
Sie ist nicht gleichbedeutend mit der `str`-Art in `Python`. Unter der Oberseite bietet `phpy` eine `API`-ähnliche der `str`-Stil, um Zeichen zu verarbeiten.


## Erstellung
```python
s1 = phpy.String("hello world")
s2 = phpy.call("random_bytes", 128)
```


## Länge
```python
print(len(s1))
print(len(s2))
```


## Nach Addition
```python
# Nachstrich hinzufügen
s1 += "hello"
# Nachbinärdaten hinzufügen
s1 += b"world"
# Nach einer weiteren phpy.String hinzufügen
s1 += phpy.String(", php ist die beste Programmiersprache")
```


## Enthalten
```python
# True zurückgeben
print(s1.__contains__("php")) 
# False zurückgeben
print(s1.__contains__("java"))
```


## Vergleich
```python
s3 = phpy.String("hello")
if s3 == "hello":
    print("==")
```


##字节abrufen
```python
print(s1[2])
```
Bitte beachten Sie, dass die Rückgabeformat von `phpy.String` mit `bytes` übereinstimmt und ein `uchar` ist.
Im Gegensatz zu `str`, das `UTF-8`-Kodierung verarbeitet und einen `UTF-8`-Breitenzeichen zurückgibt, zum Beispiel `str('中国')[0]` gibt das Zeichen `中` zurück.

## Umwandlung in die `Python` `bytes` Art

```python
print(bytes(s1))
```

> Bitte beachten Sie, dass dies zu einer Kopie des Speichers führen wird.
