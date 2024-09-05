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

#[parent('Animal', 'animal')]
class Dog extends PyClass
{
    function __construct(string $name, int $age)
    {
        parent::__construct();
        $this->self()->color = 'black';
        $this->super()->__init__($name, $age);
    }

    function speak(string $name): void
    {
        echo "Dog $name, color: {$this->self()->color}, speak: wang wang wang\n";
        $this->super()->speak('dog');
    }
}
```

- `PHP` 类必须要继承自 `PyClass` 基类
- 使用 `#[parent('Animal', 'animal')]` 属性声明继承关系
  - 第一个参数为 `Python` 类名，第二个参数为 `Python` 包名
  - 支持多继承，多个 `#[parent]` 属性声明
- 在子类的构造方法必须执行父类的构造方法 `parent::__construct()`，否则会报错

## 调用基类构造方法
```php
$this->super()->__init__($name, $age);
```

必须在 `parent::__construct()` 之后调用，否则会报错。

## 读写 Python 属性
```php
$this->self()->color = 'black';
```

## 读写 PHP 属性
```php
$this->color = 'red';
```

## 调用 Python 对象方法
```php
$this->self()->speak('dog');
```

## 调用父类方法

当子类和父类有同名方法时，可以使用 `super()` 方法调用父类的方法。

```php
$this->super()->speak('dog');
```

## 多重继承

```php
#[parent('Animal', 'animal')]
#[parent('Base', 'dog')]
class Dog extends PyClass {}
```

## 设置代理文件路径
```php
phpy\PyClass::setProxyDir(__DIR__, true);
```

- 第一个参数为代理文件路径，将在此目录下创建 `__phpy_proxy__` 目录，并生成代理文件，默认为 `getcwd()` 路径
- 第二个参数为是否检测代理文件是否过期，当代理文件的修改时间早于 `PHP` 类文件时，将重新生成代理文件，默认为 `false`
