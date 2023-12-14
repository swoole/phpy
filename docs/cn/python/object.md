# 对象操作

## 创建一个类的对象

```python
object = phpy.Object("mysqli", arg1, arg2, arg3, ...)
```

## 读取属性
```python
value = object.get("name")
```

## 设置属性
```python
object.set("name", value)
```

## 调用方法
```python
return_value = object.call("name", arg1, arg2, arg3, ...)
```

> 必须是对象的方法，类静态方法请使用 `phpy.call()` 函数调用
