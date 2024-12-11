# ユーザーガイド

このライブラリの目的は、PHPの不足をPythonのエコシステムで補うことです。
PHPに既存の機能特性があれば、直接PHP言語を使用すればよいのですが、それがない場合はPythonエコシステムで利用可能なライブラ리를探すことができます。

phpyはPythonのライブラリをPHPエコシステムに導入するだけですが、使用される構文はすべてPHPであり、追加の学習コストは必要ありません。

Pythonはすべてがオブジェクトです。モジュール、クラス、関数、整数、浮動小数点、None、ブール値、オブジェクト、辞書、リスト、集合、タプルなどです。これらはすべてPyObjectのインスタンスです。

私たちが通常プログラミングでやることは、大まかに4つのことです。

- PyCore::import() 패키지를導入する
- オブジェクトの方法を実行する：$object->fn()
- オブジェクトのプロパティを読み書きする：$object->attr 和 $object->attr = $value
- built-in関数 PyCore::$fn() を呼び出して基本的な機能を実現する。例えば、import()は実際にはbuilt-in関数です。

## 例

```php
// Pythonのosパッケージを導入する
$os = PyCore::import('os');
// 関数を実行する
$uname = $os->uname();
// プロパティを読む
echo $uname->sysname; 
// プリント
echo strval(PyCore::str($uname));
```
