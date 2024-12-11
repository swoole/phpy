# クラス操作

## クラスをロードする
```python
cls = phpy.Class("class_name")
```

## クラスの静的な属性を読む
```python
value = cls.get("name")
```

## クラスの静的な属性を設定する
```python
cls.set("name", value)
```

## インスタンスを作成する
```python
object = cls.new(arg1, arg2, arg3, ...)
```
