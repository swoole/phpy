```
# メモリコピー

PythonがPHP関数/メソッドを呼び出す際、パラメータや戻り値にはメモリコピーが存在する可能性があります。パフォーマンスに敏感なプログラムを書く際には、メモリコピーのコストに注意が必要です。

## パラメータ

- 整数型、布尔型、浮動小数点型、nullは常に値転送されます

- オブジェクト、リソース、参照は常に参照転送され、メモリはコピーされません
- 文字列、配列は再帰的な深いコピーを行い、ネイティブタイプに変換されます

```python
arg1 = 1234
arg2 = 1234.5678
arg3 = True

arg4 = phpy.Object('stdClass')
arg5 = phpy.Reference()
arg6 = phpy.call('fopen', "php://input", "r")

arg7 = {'hello' : 'world'}
arg8 = "hello world"
arg9 = [1, 2, 3, 4, 5]

phpy.call('test', arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9)
```

- `arg1`、`arg2`、`arg3`はPHPの整数型、浮動小数点型、布尔型に変換され、直接値がコピーされます

- `arg4`、`arg5`、`arg6`はPHPに直接参照を転送し、メモリコピーは発生しません
- `arg6`、`arg7`、`arg8`は反復的に深くメモリをコピーし、PHPの`array`、`string`に変換されます

## 戻り値

- 整数型、布尔型、浮動小数点型、nullはPythonのネイティブタイプに変換されます

- Pythonから返されるその他の内容はすべて`PyObject`タイプです
- PHPコードでも`PyObject`タイプを使用し、Pythonのネイティブタイプを透明に転送することができます

## メモリコピーを避ける
`phpy.String`、`phpy.Array`オブジェクトを使用することで、PHP関数を呼び出す際にメモリをコピーすることはありません。
```
