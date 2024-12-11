# 関数リスト

## include ファイルの読み込み
`phpy` モジュールは、PHP実行用のコードをロードするための関数を提供しています。
```python
phpy.include("vendor/autoload.php")
```

## globalsグローバル変数の取得
```python
print(phpy.globals("_ENV"))
```
変数の名前には `$`記号を加える必要はありません。

## constant 定数の値の取得
```python
print(phpy.constant("PHP_OS"))
```

## eval PHPコードの実行

```python
phpy.eval("var_dump(get_loaded_extensions());")
```

## call PHP関数の呼び出し

拡張関数やユーザー定義関数均可。最初の引数は関数の名前で、文字列でなければなりません。その他の引数は、呼び出されるPHP関数の引数として渡されます。

- 引数が参照型の場合、`phpy.Reference()`でラップして実現できます
- クラスの静的方法を呼び出すこともサポートされています。例えば：`phpy.call("Test::main")`

```python
print(phpy.call("file_get_contents", "/tmp/file.txt"))
```
