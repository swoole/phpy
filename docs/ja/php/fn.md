# コールバック関数

PHPの呼び出し可能なオブジェクトをPythonのコールバック関数として使用することができます。PyCore::fn(callable $fn)で包裹します。

```php
$m = PyCore::import('app.user');
$uuid = uniqid();
$rs = $m->test_callback(PyCore::fn(function ($namespace) use ($uuid) {
    var_dump($namespace);
    return $uuid;
}));
```

- `import app.user`はカスタムPythonパッケージをインポートしました。

- パッケージ内の関数`test_callback`を呼び出し、この関数はPython Callableオブジェクトを引数を受け取ります。

- Closureクロージャーオブジェクトをコールバックとして使用するためにPyCore::fn()で包裹しました。ここでは関数名文字列やオブジェクトメソッドの呼び出し方法もサポートされています。

- コールバック関数は文字列を返し、`test_callback`関数内でstrタイプの返値を得ます。

## クロージャー関数
最新のバージョンでは、コールバック関数のタイプがClosureの場合、PyCore::fn()で包裹する必要がなくなりました。底層では直接コールバックオブジェクトに変換されます。
しかし、arrayやstringタイプの関数名やクラスメソッドをコールバック関数として使用する場合、依然としてPyCore::fn()で封装する必要があります。

```php
# クロージャー関数は直接渡すことができます。
$m->test_callback(function ($namespace) use ($uuid) {
    return $uuid;
});

# 文字列関数名をコールバック関数として使用する場合、PyCore::fn()で封装する必要があります。
function test_fn() {
    return $uuid;
}
$m->test_callback(PyCore::fn('test_fn'));
```

## 例
ここではPython tkinterを例に使用しています：

```php
<?php
$tkinter = PyCore::import('tkinter');
$root = $tkinter->Tk();
$root->title('私のウィンドウ');
$root->geometry("500x500");
$root->resizable(False, False);

$button = $tkinter->Button($root, text: "クリックして!!", command: function () {
    var_dump(func_get_args());
    echo 'クリックして!!' . PHP_EOL;
});
$button->pack();

$tkinter->mainloop();
```

PHPはTk Buttonのコールバック関数として使用されています。
