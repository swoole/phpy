# 異常処理

`phpy`は`Python`の異常を封装し、`PyError`タイプを提供しています。これにより、`PHP`コードで`Python`の異常をキャッチすることができます。

## 継承関係
`PyError`は`Exception`クラスのサブクラスです。

## 属性リスト

- `error`：エラーオブジェクト

- `type`：エラータイプ

- `value`：エラー値
- `traceback`：エラーのバックトレーススタック

これらの属性は`PyObject`オブジェクトまたは`null`です。

## 異常キャッチ

```php
try {
    PyCore::import('not_exists');
} catch (PyError $e) {
    PyCore::print($e->error);
    PyCore::print($e->type);
    PyCore::print($e->value);
    PyCore::print($e->traceback);
}
```

- `$e->value`の文字列値は自動的に例外メッセージとして設定されており、`$e->getMessage()`で取得できます。
- `PyError`では`$e->code`のエラーコードを設定していませんので、使用しないでください。
