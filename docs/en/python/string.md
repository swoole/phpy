# String Operations
`phpy.String` string type is equivalent to a byte array in `Python`. The content does not contain encoding information and may contain binary content. It is not the same as `Python`'s `str` type. The `phpy` underlying system provides an API similar to the `str` style to operate on strings.


## Creation
```python
s1 = phpy.String("hello world")
s2 = phpy.call("random_bytes", 128)
```


## Length
```python
print(len(s1))
print(len(s2))
```


## Append
```python
# Append str
s1 += "hello"
# Append bytes
s1 += b"world"
# Append another phpy.String
s1 += phpy.String(", php is the best programming language")
```


## Containment
```python
# Returns True
print(s1.__contains__("php")) 
# Returns False
print(s1.__contains__("java"))
```


## Comparison
```python
s3 = phpy.String("hello")
if s3 == "hello":
    print("==")
```


## Get Byte
```python
print(s1[2])
```

Please note that the format returned by `phpy.String` is consistent with `bytes`, which is a `uchar`. However, it differs from `str`; `str` handles `UTF-8` encoding and returns a `UTF-8` wide character, for example, `str('中国')[0]` returns `中`.


## Convert to `Python`'s `bytes` Type

```python
print(bytes(s1))
```

> Please note that this will result in a memory copy.
