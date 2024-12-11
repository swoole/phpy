# メモリコピー

`PHP`が`Python`の関数/メソッドを呼び出す際、パラメータや戻り値にはメモリコピーが存在する可能性があり、パフォーマンスに敏感なプログラムを書く際にはメモリコピーのコストに注意する必要があります。

## パラメータ

- 整数型、布尔型、浮動小数点型、nullは常に値渡し

- オブジェクト、リソース、参照は常に参照渡しで、メモリはコピーされません
- 文字列、配列は再帰的な深いコピーを行い、原生タイプに変わります

```php 
$user = PyCore::import("user");
$arg1 = 1234;
$arg2 = 1234.5678;
$arg3 = true;

$arg4 = new PyDict();
$arg5 = new stdClass();
$arg6 = fopen("php://input", "r");

$arg7 = ['hello' => 'world'];
$arg8 = "hello world";
$arg9 = [1, 2, 3, 4, 5];

$user->test($arg1, $arg2, $arg3, $arg4, $arg5, $arg6, $arg7, $arg8, $arg9);
```

- `$arg1`、`$arg2`、`$arg3`はPythonの整数型、浮動小数点型、布尔型に変わり、直接数值がコピーされます

- `$arg4`、`$arg5`、`$arg6`は直接参照をPythonに渡し、メモリコピーは発生しません
- `$arg6`、`$arg7`、`$arg8`は traversal 和 deep memory copyを行い、Pythonの`list`、`dict`、`str`に変わります

## 戻り値

- 整数型、布尔型、浮動小数点型、null（`None`と`null`）はPHPの原生タイプに変わります

- Pythonから返されるその他の内容はすべて`PyObject`タイプです
- Pythonコード内で直接`phpy.String`や`phpy.Array`などのPHP原生タイプを使用することで、透明な転送传递给えることができます

## メモリコピーを避ける
`PyObject::object($value)`メソッドを使用して文字列や配列タイプを`PyObject`に変換すると、Pythonコード内で得られるタイプは`phpy.String`と`phpy.Array`になります。

この方法はPythonコード内で`phpy`のタイプシステムに適応する必要があります。
