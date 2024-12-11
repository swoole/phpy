Socket API
=====
「phpy」プログラミング開発において、しばしば「Socket API」を使用してネットワーク通信プログラムを書く必要があります。
以下の方法を利用して、「Python Socket オブジェクト」と「PHP Streamリソース」を相互に変換することができます。

PythonからPHPへ
-----
```php
$socket = PyCore::import('socket');
const HOST = "127.0.0.1";
const PORT = 5432;

$client = $socket->socket($socket->AF_INET, $socket->SOCK_STREAM);
$client->connect(PyCore::tuple([HOST, PORT]));

$fp = fopen('php://fd/' . $client->fileno(), 'rw');
fwrite($fp, $msg);
$data = fread($fp, 1024);
fclose($fp);
```

- Pythonの`Socket.fileno()`メソッドを使用してファイル記述子を取得する
- PHPで`fopen('php://fd/{$fileno}')`を使用して、ファイルハンドルの対応する`Socket`を`PHP Stream`に変換する
- `fwrite/fread/fclose`を使用して、ハンドルの読み書き・閉鎖を行う

`fopen()`はファイル記述子をコピーするため、「Python Socketオブジェクト」が閉じられる時も、「php://fd/{$fileno}」に対応する`Socket`は影響を受けず、「Python Socket API」を使用してこのネットワーク接続に対してデータ転送操作を行うことができます。

PHPからPythonへ
----
```php
$socket = PyCore::import('socket');

$HOST = "127.0.0.1";
$PORT = 5432;

$fp = stream_socket_client("tcp://$HOST:$PORT", $errno, $errstr, 30);
if (!$fp) {
    exit("Error: $errstr ($errno)\n");
}
$client = $socket->fromfd(PyCore::fileno($fp), $socket->AF_INET, $socket->SOCK_STREAM);
fclose($fp);
```

- PHPの`PyCore::fileno($fp)`メソッドを使用して`PHP Stream`のファイル記述子を取得する
- Pythonで`Socket.fromfd()`を使用して、ファイルハンドルの対応する`Socket`を「Python Socketオブジェクト」に変換する

`Socket.fromfd()`はファイル記述子をコピーするため、「Python Socket」が閉じられる時も、「PHP Stream」は影響を受けず、PHPの`fwrite/fread/fclose`を使用してこのネットワーク接続に対してデータ転送操作を行うことができます。
