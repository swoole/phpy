# コア

すべての `Python` の組み込み関数は `PyCore` クラスの静的な方法として提供されており、組み込み方法の使用は `Python` ドキュメントを参照してください。

## パッケージの導入
```php
$os = PyCore::import('os');
```
成功すると `PyModule` オブジェクトが返されます。`Python`の組み込みパッケージだけでなく、サードパーティのパッケージやユーザー定義のパッケージも導入できます。

モジュールのみをロードでき、`Python`の `from module import class` 文法はサポートされていません。以下の文法で代替できます。

```php
$module = PyCore::import($moduleName);
$class = $m->$className;
```

`Python`は既にロードされたモジュールをキャッシュしており、2回目のロード時にはキャッシュされたモジュールを自動的に返しますので、重複してロードすることはありません。そのため、`PHP-FPM/Apache`などの短寿命環境でも使用でき、性能問題はありません。

## ロードパス
一部のディレクトリをロードパスリストに追加するために `PyCore::import('sys')->path->append()` を使用できます。
例えば：`/workspace/app/user.py` 自定义のパッケージは、以下のステップでロードできます：

1. `PyCore::import('sys')->path->append('/workspace')` `/workspace` を `sys.path`に追加
2. `PyCore::import('app.user')` 自動的に `sys.path`で検索し、対応する `app/user.py` パッケージをロードします

## 組み込み方法

- `PyCore::import($module)` モジュールを導入する

- `PyCore::str()` オブジェクトを文字列に変える

- `PyCore::repr()` 

- `PyCore::type()` オブジェクトのタイプを取得する

- `PyCore::locals()` 現在のスコープの内容のすべての局部変数を取得する

- `PyCore::globals()` すべてのグローバル変数を取得する

- `PyCore::hash()` ハッシュ値を取得する

- `PyCore::hasattr()` オブジェクトに特定の属性があるかどうかを検出する

- `PyCore::id()` オブジェクトの内部番号を取得する

- `PyCore::len()` 長さを取得する

- `PyCore::dir()` オブジェクトのすべての属性、方法を取得する

- `PyCore::int()` 整数を構築する

- `PyCore::float()` 浮点数を構築する

- `PyCore::fn()` 呼び出し可能な関数を構築する

- `PyCore::eval()` Pythonコードを実行する

- `PyCore::dict()` 単語の辞書オブジェクトを構築する

- `PyCore::set()` 集合オブジェクトを構築する

- `PyCore::range()` ランジェンス系列を構築する

- `PyCore::scalar($pyobj)` Pythonの `PyObject` オブジェクトをPHPのスカラータイプに変換します。例えば、`PyStr`はPHPの文字列に、`Dict/Tuple/Set/List`は `Array`に変わります。
- `PyCore::fileno($fp)` PHPストリームリソースのファイル記述子を取得します。ただし、`tcp/udp/unix`タイプのリソースのみサポートされています。

> `PyCore`は `__callStatic()` メイジメソッドを実現しており、`PyCore`の静的な方法の呼び出しは自動的にPythonの `builtins` モジュールの対応するメソッドを呼び出します。
> 組み込み方法の使用については [Built-in Functions](https://docs.python.org/3/library/functions.html)を参照してください。

## 動的リンクライブラリの問題
ライブラリの導入時に動的リンクライブラリのエラーが発生する可能性があります。その原因は `LD` パスが間違っているためかもしれません。Python Cモジュールの動的ライブラリパスを環境変数で指定することができます。

> 多个のパスを `:`で分割して設定することもできます。

```shell
# anaconda3 base環境のみを使用している場合
export LD_LIBRARY_PATH=/opt/anaconda3/lib
# cefという特別な環境を使用している場合
export LD_LIBRARY_PATH=/opt/anaconda3/envs/cef/lib:/opt/anaconda3/lib
php plot.php
```

この方法は現在の `bash` 会話にのみ有効であり、グローバルには影響しません。直接 `/etc/ld.so.conf.d/*.conf`に `/opt/anaconda3/lib`を追加することはお勧めしません。これは `libc`ライブラリの衝突を引き起こし、オペレーティングシステムの他のプログラムの正常な実行に影響を与える可能性があります。

## 大文字小文字の敏感性
Pythonでは、すべての関数、方法、変数、属性などが大文字と小文字が区別される名前で命名されており、呼び出す際にはPythonの大文字と小文字が完全に一致する名前を使用しなければなりません。

例えば：

```python
def TestUser():
    pass
```

PHPコードでは `$module->TestUser()` を使用しなければならず、他の方法である `$module->testUser()`や `$module->testuser()`は間違った書き方です。

## 環境変数
phpyではPythonの`os.environ`が自動的に初期化されていないため、environは空の辞書です。環境変数を注入するために`$_ENV`を繰り返し遍历する必要があります。

```php
$os = PyCore::import('os');
foreach($_ENV as $k => $v) {
    $os->environ->__setitem__($k, $v);
}
```

## undefined symbol:ffi_type_uint32, version LIBFFI_BASE_7.0
動的リンクライブラリのパスに衝突がある可能性があります。以下の方法で解決を試みることができます。
問題が依然としてあれば、システムに付属しているPython環境をcondaで作成した環境に代えることをお勧めします。

```shell
export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libffi.so.7
```

## Import 失败
ほとんどの場合、「from a import b」は「PyCore::import('a')->b」と同等ですが、一部の特殊なライブラリは上記の方法で正しくロードできない場合があります。以下の方法で置き換えることができます：

```php
# 加载できない
$b = PyCore::import('a')->b;
# 以下のコードに置き換える
$b = PyCore::import('a.b');
```
