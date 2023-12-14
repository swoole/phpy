```php
$info = $Info();
```

```py
info = Info()
``````py
$info = Info('Rango', 2023)
```

```py
from app.user import Info

# Create an Info object
info = Info('Rango', 2023)
```

## Named Parameters
Supports named parameters. Example:

### Passing named parameters
```php
kwargs($a, $b, $c, name: 'hello', world: 'rango');
```

- Positional parameters must come first, named parameters must come last.

### Receiving named parameters
```php
function kwargs($a, $b, $c, $name, $world) {

}
```

### Variable named parameters
```php
function kwargs(...$kwargs) {
    var_dump($kwargs);
}
```
- `$kwargs` will contain both the positional parameters and the named parameters, for example in the previous example it will receive:
```php
array(
 0 => $a,
 1 => $b,
 2 => $c,
 'name' => 'hello',
 'world' => 'rango',
)
```

### Forwarding named parameters
```php
function kwargs(...$kwargs) {
    kwargs_fn2(...$kwargs);
}
```

It is possible to forward the named parameters to another function.