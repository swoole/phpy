# 字符串操作
`phpy.String` 字符串类型相当于 `Python` 中的字节数组。内容中不包含编码信息，并且可能会存在二进制内容。
与 `Python` 的 `str` 类型并不等同。`phpy` 底层提供了类似于 `str` 风格的 `API`来操作字符串。

## 创建
```python
s1 = phpy.String("hello world")
s2 = phpy.call("random_bytes", 128)
```

## 长度
```python
print(len(s1))
print(len(s2))
```

## 追加
```python
# 追加 str
s1 += "hello"
# 追加 bytes
s1 += b"world"
# 追加另外一个 phpy.String
s1 += phpy.String(", php is the best program language")
```

## 包含
```python
# 返回 True
print(s1.__contains__("php")) 
# 返回 False
print(s1.__contains__("java"))
```

## 比较
```python
s3 = phpy.String("hello")
if s3 == "hello":
    print("==")
```

## 取字节
```python
print(s1[2])
```

请注意 `phpy.String`返回的格式与 `bytes` 一致，是一个 `uchar`。
但与 `str` 不同，`str` 会处理 `UTF-8` 编码返回一个 `UTF-8` 的宽字符，例如 `str('中国')[0]` 返回的是 `中`。

## 转为 `Python` 的 `bytes` 类型

```python
print(bytes(s1))
```

> 请注意这里将产生一次内存复制
