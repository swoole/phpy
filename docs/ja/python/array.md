# 配列操作

`phpy.Array`は混合型であり、`List`または`Map`である可能性があります。

## 作成
```python
# List
l = phpy.Array([1, 3, 5, 2023, 7, 9])
# Map
m = phpy.Array({"hello": "world", "php": "swoole"})
```

## 読み取り
```python
print(l[3])
print(m["php"])
```

## 長さ
```python
print(len(l))
print(len(m))
```

## 書き込み
```python
# キーと値を設定
m["swoole"] = 'coroutine'
# 要素をリストの末尾に追加
l.append(9999)
```

## その他の方法

- `get(key)` 読み取り

- `set(key, value)` 書き込み

- `unset(key)` 削除

- `append(value)` 要素をリストの末尾に追加

- `count()` 要素の読み取り
- `collect()` Python原生の`dict`または`list`に変換
- `is_list()` 配列が`List`かどうかを検出
