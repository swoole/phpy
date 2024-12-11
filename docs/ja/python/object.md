# オブジェクト操作

## クラスのインスタンスを作成する

```python
object = phpy.Object("mysqli", arg1, arg2, arg3, ...)
```

## プロパティを読む
```python
value = object.get("name")
```

## プロパティを設定する
```python
object.set("name", value)
```

## メソッドを呼び出す
```python
return_value = object.call("name", arg1, arg2, arg3, ...)
```

> メソッドでなければならず、クラスの静的なメソッドは `phpy.call()` 関数で呼び出してください。
