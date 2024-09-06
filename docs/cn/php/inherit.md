# 继承 `Python` 类
 
将 `Python` 类作为 `PHP` 类的父类，可使用下面的方法实现。

## 安装 composer 包

此功能需要额外安装 `phpy` 的 `composer` 扩展包。

```shell
composer require swoole/phpy
```

## 编写 PHP 类
```php
use phpy\PyClass;

#[Inherit('Animal', 'animal')]
class Dog extends PyClass
{
    protected string $weight;

    function __construct(string $name, int $age)
    {
        parent::__construct();
        // 此属性未在 PHP 层定义，将会设置为 Python 属性
        $this->color = 'black';
        // 此属性由 PHP 层定义，不会设置为 Python 属性
        $this->weight = '10kg';
        // 读写 Python 属性
        $this->self()->color = 'black';
        // 调用 Python 方法
        $this->get_age();
        $this->self()->get_age();
        // 调用父类构造方法
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
    
    // 此方法不会映射到 Python 层，无法在 Python 中使用
    private function get_weight(): string
    {
        return $this->weight;
    }
}
```

- `PHP` 类必须要继承自 `PyClass` 基类
- 使用 `#[Inherit('Animal', 'animal')]` 属性声明继承关系
  - 第一个参数为 `Python` 类名，第二个参数为 `Python` 包名
  - 支持多继承，可添加多个 `#[Inherit]` 属性声明
- 在子类的构造方法必须执行父类的构造方法 `parent::__construct()`，否则会报错

## 调用基类构造方法
```php
$this->super()->__init__($name, $age);
```

必须在 `parent::__construct()` 之后调用，否则会报错。

## 读写属性
```php
$this->self()->color = 'black';
$this->color = 'red';
```

- `PHP` 类和 `Python` 类有同名属性，可以使用 `$this->self()` 方法访问 `Python` 属性
- 在 `PHP` 类中未定义的属性，可以直接使用 `$this->{$attr}` 访问，等同于 `$this->self()->{$attr}`

## 调用方法
```php
$this->self()->get_age();
$this->get_age();
```

- `PHP` 类和 `Python` 父类有同名方法，可以使用 `$this->self()->{$method}()` 调用 `Python` 方法
- 在 `PHP` 类中未定义的方法，可以直接使用 `$this->{$method}()` 调用，等同于 `$this->self()->{$method}()`

## 调用父类方法

当子类和父类有同名方法时，可以使用 `$this->super()->{$method}()` 方法调用父类的方法。

```php
$this->super()->speak('dog');
```

## 多重继承

```php
#[Inherit('Animal', 'animal')]
#[Inherit('Base', 'dog')]
class Dog extends PyClass {}
```

等同于如下的 `Python` 代码：
```python
class Dog(Animal, Base):
    pass
```


## 传递对象到 `Python` 层
```php
$framework = PyCore::import('framework');
$framework->run($this->self());
```

某些场景需要将 `PHP` 对象传递到 `Python` 层，可以使用 `$this->self()` 方法获取 `Python` 对象，
将对象传递给 `Python` 层。当在 `Python` 内部调用对象方法时，将会调用 `PHP` 类的方法。

> 仅 `public/protected` 方法可以被 `Python` 调用

## 设置代理文件路径
```php
phpy\PyClass::setProxyDir(__DIR__, true);
```

- 第一个参数为代理文件路径，将在此目录下创建 `__phpy_proxy__` 目录，并生成代理文件，默认为 `getcwd()` 路径
- 第二个参数为是否检测代理文件是否过期，当代理文件的修改时间早于 `PHP` 类文件时，将重新生成代理文件，默认为 `false`
