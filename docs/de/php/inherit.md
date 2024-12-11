# Erben von `Python` Klassen

Um eine `Python` Klasse als Basisklasse für eine `PHP` Klasse zu verwenden, kann man den folgenden Methoden folgen.

## Composer-Paket installieren

Diese Funktion erfordert die zusätzliche Installation des `composer` Erweiterungspakets für `phpy`.

```shell
composer require swoole/phpy
```

## PHP-Klasse schreiben
```php
use phpy\PyClass;

#[Inherit('Animal', 'animal')]
class Dog extends PyClass
{
    protected string $weight;

    function __construct(string $name, int $age)
    {
        parent::__construct();
        // Diese Eigenschaft ist nicht in der PHP-Schicht definiert und wird als Python-Eigenschaft festgelegt
        $this->color = 'black';
        // Diese Eigenschaft wird von der PHP-Schicht definiert und wird nicht als Python-Eigenschaft festgelegt
        $this->weight = '10kg';
        // Lesen und Schreiben von Python-Eigenschaften
        $this->self()->color = 'black';
        // Aufrufen von Python-Methoden
        $this->get_age();
        $this->self()->get_age();
        // Aufrufen des Konstruktors der Elternklasse
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
    
    // Diese Methode wird nicht auf die Python-Schicht abgebildet und kann nicht in Python verwendet werden
    private function get_weight(): string
    {
        return $this->weight;
    }
}
```

- Die `PHP`-Klasse muss von der `PyClass`-Basisklasse erben
- Verwenden Sie das Attribut `[Inherit('Animal', 'animal')]` um die Erbschaftsbeziehung zu deklarieren
  - Der erste Parameter ist der Name der `Python`-Klasse, der zweite Parameter ist der Name des `Python`-Paket

  - Mehrere Erbschaften sind möglich, indem Sie mehrere `[Inherit]`-Attribute deklarieren
- Im Konstruktor der Tochterklasse muss der Konstruktor der Elternklasse aufgerufen werden `parent::__construct()`, sonst wird ein Fehler aufgetreten

## Aufrufen des Konstruktors der Basisklasse
```php
$this->super()->__init__($name, $age);
```

Muss nach `parent::__construct()` aufgerufen werden, sonst wird ein Fehler aufgetreten.

## Lesen und Schreiben von Eigenschaften
```php
$this->self()->color = 'black';
$this->color = 'red';
```

- Wenn die `PHP`-Klasse und die `Python`-Klasse denselben Eigenschaftsnamen haben, kann die `$this->self()`-Methode verwendet werden, um die `Python`-Eigenschaft zu访问
- Eine Eigenschaft, die in der `PHP`-Klasse nicht definiert ist, kann direkt mit `$this->{$attr}`访问 werden, was gleichbedeutend mit `$this->self()->{$attr}` ist

## Aufrufen von Methoden
```php
$this->self()->get_age();
$this->get_age();
```

- Wenn die `PHP`-Klasse und die `Python`-Überlieferungsklasse denselben Methodenamen haben, kann die `$this->self()->{$method}()`-Methode verwendet werden, um die `Python`-Methode aufzurufen
- Eine Methode, die in der `PHP`-Klasse nicht definiert ist, kann direkt mit `$this->{$method}()` aufgerufen werden, was gleichbedeutend mit `$this->self()->{$method}()` ist

## Aufrufen der Methode der Überlieferungsklasse
Wenn eine Tochterklasse und ihre Überlieferungsklasse denselben Methodenamen haben, kann die `$this->super()->{$method}()`-Methode verwendet werden, um die Methode der Überlieferungsklasse aufzurufen.

```php
$this->super()->speak('dog');
```

## Mehrfache Erbschaft

```php
#[Inherit('Animal', 'animal')]
#[Inherit('Base', 'dog')]
class Dog extends PyClass {}
```

Entsprechend dem folgenden `Python`-Code:
```python
class Dog(Animal, Base):
    pass
```

## Objekt an die Python-Schicht übergeben
```php
$framework = PyCore::import('framework');
$framework->run($this->self());
```

In einigen Szenarien ist es notwendig, ein `PHP`-Objekt an die `Python`-Schicht zu übergeben. Dies kann erreicht werden, indem die `$this->self()`-Methode verwendet wird, um das `Python`-Objekt zu erhalten und das Objekt an die `Python`-Schicht zu übergeben. Wenn innerhalb der `Python`-Schicht eine Methode des Objekts aufgerufen wird, wird die entsprechende Methode der `PHP`-Klasse aufgerufen.

> Nur `public`/`protected` Methoden können von Python aufgerufen werden
