# Inheriting `Python` Classes

You can use the following method to make a `Python` class the parent class of a `PHP` class.

## Install Composer Package

This function requires an additional installation of the `phpy` composer extension package.

```shell
composer require swoole/phpy
```

## Write PHP Class
```php
use phpy\PyClass;

#[Inherit('Animal', 'animal')]
class Dog extends PyClass
{
    protected string $weight;

    function __construct(string $name, int $age)
    {
        parent::__construct();
        // This attribute is not defined in the PHP layer and will be set as a Python attribute
        $this->color = 'black';
        // This attribute is defined in the PHP layer and will not be set as a Python attribute
        $this->weight = '10kg';
        // Read and write Python attribute
        $this->self()->color = 'black';
        // Call Python method
        $this->get_age();
        $this->self()->get_age();
        // Call parent class constructor
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
    
    // This method will not be mapped to the Python layer and cannot be used in Python
    private function get_weight(): string
    {
        return $this->weight;
    }
}
```

- `PHP` classes must inherit from the `PyClass` base class.
- Use the `#[Inherit('Animal', 'animal')]` attribute to declare the inheritance relationship.
  - The first parameter is the `Python` class name and the second parameter is the `Python` package name.

  - Supports multiple inheritance; you can add multiple `#[Inherit]` attributes.
- The constructor of the subclass must execute the parent class's constructor `parent::__construct()`, or it will throw an error.


## Call Base Class Constructor
```php
$this->super()->__init__($name, $age);
```

It must be called after `parent::__construct()`, otherwise an error will occur.


## Read and Write Properties
```php
$this->self()->color = 'black';
$this->color = 'red';
```

- If there are properties with the same name in both `PHP` and `Python` classes, the `Python` properties can be accessed using the `$this->self()` method.
- Properties not defined in the `PHP` class can be accessed directly with `$this->{$attr}`, equivalent to `$this->self()->{$attr}`.


## Call Methods
```php
$this->self()->get_age();
$this->get_age();
```

- If there are methods with the same name in both `PHP` and the `Python` parent class, the `Python` methods can be called using `$this->self()->{$method}()`.
- Methods not defined in the `PHP` class can be called directly with `$this->{$method}()`, equivalent to `$this->self()->{$method}()`.


## Call Parent Class Methods

When the subclass and parent class have methods with the same name, you can call the parent class's method using `$this->super()->{$method}()`.

```php
$this->super()->speak('dog');
```

## Multiple Inheritance

```php
#[Inherit('Animal', 'animal')]
#[Inherit('Base', 'dog')]
class Dog extends PyClass {}
```

This is equivalent to the following `Python` code:
```python
class Dog(Animal, Base):
    pass
```

## Passing Objects to the `Python` Layer
```php
$framework = PyCore::import('framework');
$framework->run($this->self());
```

In certain scenarios, it is necessary to pass `PHP` objects to the `Python` layer. You can use the `$this->self()` method to get the `Python` object and pass it to the `Python` layer. When calling the object’s methods internally in `Python`, it will invoke the methods of the `PHP` class.

> Only `public/protected` methods can be called by `Python`.


## Set Proxy File Path
```php
phpy\PyClass::setProxyDir(__DIR__, true);
```

- The first parameter is the path for the proxy file, and the `__phpy_proxy__` directory will be created in this directory, generating the proxy file, which defaults to the `getcwd()` path.
- The second parameter determines whether to check if the proxy file is outdated; if the modification time of the proxy file is earlier than that of the `PHP` class file, the proxy file will be regenerated, defaulting to `false`.
