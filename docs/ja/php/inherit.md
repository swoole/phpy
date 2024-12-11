```
# Pythonクラスの継承

PHPクラスをPythonクラスの親クラスとして継承するには、以下の方法を使用できます。

## Composerパッケージのインストール

この機能は、phpyのcomposer拡張パッケージを別途インストールする必要があります。

```shell
composer require swoole/phpy
```

## PHPクラスの作成
```php
use phpy\PyClass;

#[Inherit('Animal', 'animal')]
class Dog extends PyClass
{
    protected string $weight;

    function __construct(string $name, int $age)
    {
        parent::__construct();
        // この属性はPHP層で定義されていないため、Python属性として設定されます
        $this->color = 'black';
        // この属性はPHP層で定義されているため、Python属性としては設定されません
        $this->weight = '10kg';
        // Python属性の読み書き
        $this->self()->color = 'black';
        // Pythonメソッドの呼び出し
        $this->get_age();
        $this->self()->get_age();
        // 親クラスのコンストラクタの呼び出し
        $this->super()->__init__($name, $age);
    }

    public function speak(string $name): void
    {
        echo "Dog $name, color: {$this->self()->color}, speak: wang wang wang\n";
        $this->super()->speak('dog');
    }
    
    protected function test()
    {
        debug_print_backtrace();
    }
    
    // Python層にはマッピングされず、Pythonでは使用できません
    private function get_weight(): string
    {
        return $this->weight;
    }
}
```

- PHPクラスはPyClass基本クラスを継承しなければなりません
- #[Inherit('Animal', 'animal')]属性を使用して継承関係を宣言します
  - 第一引数はPythonクラス名、第二引数はPythonパッケージ名です

  - 多重継承もサポートされており、複数の#[Inherit]属性を宣言することができます
- 子クラスのコンストラクタでは必ず親クラスのコンストラクタを呼び出さなければなりませんparent::__construct()、そうでなければエラーが発生します

## 親クラスのコンストラクタの呼び出し
```php
$this->super()->__init__($name, $age);
```

parent::__construct()の後に呼び出さなければなりません。そうでなければエラーが発生します。

## プロパティの読み書き
```php
$this->self()->color = 'black';
$this->color = 'red';
```

- PHPクラスとPythonクラスに同名のプロパティがある場合、$this->self()メソッドを使用してPythonプロパティにアクセスできます
- PHPクラスで定義されていないプロパティは、直接$this->{$attr}でアクセスでき、$this->self()->{$attr}と同等です

## メソッドの呼び出し
```php
$this->self()->get_age();
$this->get_age();
```

- PHPクラスとPython親クラスに同名のメソッドがある場合、$this->self()->{$method}()`を使用してPythonメソッドを呼び出します
- PHPクラスで定義されていないメソッドは、直接$this->{$method}()`で呼び出すことができ、$this->self()->{$method}()`と同等です

## 親クラスメソッドの呼び出し

子クラスと親クラスに同名のメソッドがある場合、$this->super()->{$method}()`メソッドを使用して親クラスのメソッドを呼び出します。

```php
$this->super()->speak('dog');
```

## 多重継承

```php
#[Inherit('Animal', 'animal')]
#[Inherit('Base', 'dog')]
class Dog extends PyClass {}
```

これは以下のPythonコードと同等です：
```python
class Dog(Animal, Base):
    pass
```

## PHPオブジェクトをPython層に渡す
```php
$framework = PyCore::import('framework');
$framework->run($this->self());
```

一部のシナリオでは、PHPオブジェクトをPython層に渡す必要があります。$this->self()メソッドを使用してPythonオブジェクトを取得し、Python層にオブジェクトを渡すことができます。Python内でオブジェクトのメソッドを呼び出すと、PHPクラスのメソッドが呼び出されます。

> Pythonが呼び出すことができるのはpublic/protectedメソッドのみです

## プロキシファイルパスを設定する
```php
phpy\PyClass::setProxyDir(__DIR__, true);
```

- 第一引数はプロキシファイルのPATHであり、このディレクトリの下に__phpy_proxy__ディレクトリが作成され、プロキシファイルが生成されます。デフォルトはgetcwd()のPATHです
- 第二引数はプロキシファイルが过期しているかどうかを検出するかどうかです。プロキシファイルの変更時間がPHPクラスファイルよりも古い場合、プロキシファイルが再生成されます。デフォルトはfalseです
```
