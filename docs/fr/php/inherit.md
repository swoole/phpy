# hériter de la classe `Python`

Pour hériter d'une classe `Python` en tant que classe `PHP`, utilisez la méthode suivante.

## Installer le paquet Composer

Cette fonction nécessite l'installation supplémentaire du paquet `composer` pour `phpy`.

```shell
composer require swoole/phpy
```

## Écrire la classe PHP
```php
use phpy\PyClass;

#[Inherit('Animal', 'animal')]
class Dog extends PyClass
{
    protected string $weight;

    function __construct(string $name, int $age)
    {
        parent::__construct();
        // Cette propriété n'est pas définie au niveau PHP, elle sera définie comme propriété Python
        $this->color = 'black';
        // Cette propriété est définie au niveau PHP, elle ne sera pas définie comme propriété Python
        $this->weight = '10kg';
        // Lire la propriété Python
        $this->self()->color = 'black';
        // Appeler la méthode Python
        $this->get_age();
        $this->self()->get_age();
        // Appeler le constructeur de la classe parent
        $this->super()->__init__($name, $age);
    }

    public function speak(string $name): void
    {
        echo "Dog $name, couleur: {$this->self()->color}, parle: wang wang wang\n";
        $this->super()->speak('dog');
    }
    
    protected function test()
    {
        debug_print_backtrace();
    }
    
    // Cette méthode ne sera pas mappée au niveau Python, elle ne peut pas être utilisée en Python
    private function get_weight(): string
    {
        return $this->weight;
    }
}
```

- La classe `PHP` doit hériter de la classe de base `PyClass`
- Utilisez l'attribut `#[Inherit('Animal', 'animal')]` pour déclarer la relation de héritage
  - Le premier argument est le nom de la classe `Python`, le deuxième argument est le nom du paquet `Python`

  - Prend en charge l'héritage multiple, plusieurs attributs `#[Inherit]` peuvent être ajoutés pour déclarer des relations de héritage
- Dans la méthode de constructeur de la sous-classe, il est essentiel d'exécuter le constructeur de la classe parent `parent::__construct()`, sinon une erreur se produira

## Appeler le constructeur de la classe parent
```php
$this->super()->__init__($name, $age);
```

Il doit être appelé après `parent::__construct()`, sinon une erreur se produira.

## Lire les propriétés
```php
$this->self()->color = 'black';
$this->color = 'red';
```

- La classe `PHP` et la classe `Python` ont des propriétés du même nom, vous pouvez utiliser la méthode `$this->self()` pour accéder à la propriété `Python`
- Pour les propriétés qui ne sont pas définies dans la classe `PHP`, vous pouvez directement utiliser `$this->{$attr}` pour accéder, ce qui est équivalent à `$this->self()->{$attr}`

## Appeler les méthodes
```php
$this->self()->get_age();
$this->get_age();
```

- La classe `PHP` et la classe parent `Python` ont des méthodes du même nom, vous pouvez utiliser la méthode `$this->self()->{$method}()` pour appeler la méthode `Python`
- Pour les méthodes qui ne sont pas définies dans la classe `PHP`, vous pouvez directement utiliser `$this->{$method}()` pour les appeler, ce qui est équivalent à `$this->self()->{$method}()`

## Appeler la méthode de la classe parent

Lorsque la sous-classe et la classe parent ont des méthodes du même nom, vous pouvez utiliser la méthode `$this->super()->{$method}()` pour appeler la méthode de la classe parent.

```php
$this->super()->speak('dog');
```

## Héritage multiple

```php
#[Inherit('Animal', 'animal')]
#[Inherit('Base', 'dog')]
class Dog extends PyClass {}
```

Cela équivaut au code `Python` suivant :
```python
class Dog(Animal, Base):
    pass
```

## Passer un objet au niveau Python
```php
$framework = PyCore::import('framework');
$framework->run($this->self());
```

Dans certains cas, il est nécessaire de passer un objet `PHP` au niveau `Python`. Vous pouvez utiliser la méthode `$this->self()` pour obtenir l'objet `Python` et le transmettre au niveau `Python`. Lorsque la méthode de l'objet est appelée à l'intérieur du `Python`, la méthode de la classe `PHP` sera appelée.

> Seules les méthodes `public` et `protected` peuvent être appelées par le `Python`

## Établir le chemin du fichier proxy
```php
phpy\PyClass::setProxyDir(__DIR__, true);
```

- Le premier argument est le chemin du fichier proxy, une directory `__phpy_proxy__` sera créée dans ce chemin, et des fichiers proxies seront générés, par défaut c'est le chemin actuel.
- Le deuxième argument est une valeur booléenne indiquant si l'on doit vérifier si le fichier proxy est obsolète. Lorsque la date de modification du fichier proxy est antérieure à celle du fichier de la classe `PHP`, le fichier proxy sera régénéré, par défaut c'est `false`.
