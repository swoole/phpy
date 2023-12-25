# 数组操作

`phpy.Array` 是一个混杂类型，可能是 `List` 也可能是一个 `Map`。

## 创建
```python
# List
l = phpy.Array([1, 3, 5, 2023, 7, 9])
# Map
m = phpy.Array({"hello": "world", "php": "swoole"})
```

## 读取
```python
print(l[3])
print(m["php"])
```

## 长度
```python
print(len(l))
print(len(m))
```

## 写入
```python
# 设置 Key Value
m["swoole"] = 'coroutine'
# 追加元素到末尾
l.append(9999)
```

## 其他方法
- `get(key)` 读取
- `set(key, value)` 写入
- `unset(key)` 删除
- `append(value)` 追加元素到列表末尾
- `count()` 读取元素
- `collect()` 转为 `Python` 原生的 `dict` 或 `list`
- `is_list()` 检测数组是否为 `List`
