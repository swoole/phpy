# 文字列操作
`phpy.String` 文字列タイプは `Python` のバイト配列に相当します。内容にはエンコード情報が含まれておらず、バイナリコンテンツが存在する可能性があります。
`Python` の `str` 型とは異なります。`phpy` の下層では `str`スタイルの `API`が提供されており、文字列を操作することができます。

## 作成
```python
s1 = phpy.String("hello world")
s2 = phpy.call("random_bytes", 128)
```

## 長さ
```python
print(len(s1))
print(len(s2))
```

## 追加
```python
# strを追加
s1 += "hello"
# bytesを追加
s1 += b"world"
#別の phpy.String を追加
s1 += phpy.String(", php is the best program language")
```

## 含まれる
```python
# True 返回
print(s1.__contains__("php")) 
# False 返回
print(s1.__contains__("java"))
```

## 比較
```python
s3 = phpy.String("hello")
if s3 == "hello":
    print("==")
```

## バイトを取り出す
```python
print(s1[2])
```

`phpy.String`が返すフォーマットは `bytes`と一致しており、`uchar`です。
しかし `str`とは異なり、`str`は `UTF-8`エンコーディングを処理し、`UTF-8`の広字符を返します。例えば `str('中国')[0]`は `中`を返します。

## Pythonの`bytes`型に変換する

```python
print(bytes(s1))
```

> ここではメモリコピーが発生することを请注意してください
