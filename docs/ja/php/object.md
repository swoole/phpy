# Pythonオブジェクト
`Pythonオブジェクト`は`PyCore`以外のすべての他のタイプの基底クラスです。組み込みクラスの対象外の对象は`Pythonオブジェクト`の実例です。`Pythonオブジェクト`は4つのマジックメソッドを実現しており、操作を`Python`オブジェクトにマッピングするために使用されます。

すべてのクラス方法、パラメータ、戻り値は`stubs`ディレクトリ内のファイルを参照してください。ドキュメントはこれ以上説明しません。

## 組み込みクラス

- `Pythonオブジェクト`：すべての他のタイプの基底クラス

- `PyDict`：辞書タイプ、PHPの連想配列に相当

- `PyList`：リストタイプ、PHPの索引配列に相当

- `PyTuple`：タプル、不変のリスト

- `PyStr`：文字列

- `PyModule`：`Python`パッケージ、`PyModule`も`Pythonオブジェクト`の子クラスです

## 継承関係

```
Pythonオブジェクト -> PyModule
         -> PySequenece -> PyList
                        -> PyTuple
         -> PySet
         -> PyStr
         -> PyDict
         -> PyType
```

## __get($name)
`Python`オブジェクトのプロパティを読取します。以下の操作は同等です。

```php
$pyobj->attr;
```

```py
pyobj.attr
```

## __set($name, $value)

`Python`オブジェクトのプロパティを設定します。以下の操作は同等です。

```php
$pyobj->attr = 'hello';
```

```py
pyobj.attr = 'hello'
```

## __call($name, $args)

`Python`オブジェクトの方法を呼び出します。以下の操作は同等です。

```php
$pyobj->fn($a, $b, $c);
```

```py
pyobj.fn(a, b, c)
```

## __invoke(...$args)

`callable`オブジェクトを実行します。通常は関数やオブジェクトの構築に使用されます。以下の操作は同等です。

```php
// $userはPyModuleです
$user = PyCore::import('app.user');
// Infoはapp.userの中のクラスです
$Info = $user->Info;
// Infoオブジェクトを生成します
$info = $Info('Rango', 2023);
```

```py
from app.user import Info

# Infoオブジェクトを生成します
info = Info('Rango', 2023);
```

## 名前付きパラメータ
名前付きパラメータの書き方をサポートしています。例：

### 名前付きパラメータを渡す
```php
kwargs($a, $b, $c, name: 'hello', world: 'rango');
```

-順序パラメータは必ず最初にあり、名前付きパラメータは必ず最後にあります

### 名前付きパラメータを受け取る
```php
function kwargs($a, $b, $c, $name, $world) {

}
```

### 可変名前付きパラメータ
```php
function kwargs(...$kwargs) {
    var_dump($kwargs);
}

```
- `$kwargs`は順序パラメータと名前付きパラメータの両方を含みます。例えば、先ほどの例では次のように得られます。
```php
array(
 0 => $a,
 1 => $b,
 2 => $c,
 'name' => 'hello',
 'world' => 'rango',
)
```

### 名前付きパラメータを透伝する
```php
function kwargs(...$kwargs) {
    kwargs_fn2(...$kwargs);
}
```

名前付きパラメータを別の関数に渡すことができます。
