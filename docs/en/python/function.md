# Function List

## include Load File
The `phpy` module provides functions for loading and executing `PHP` code.
```python
phpy.include("vendor/autoload.php")
```

## globals Get Global Variables
```python
print(phpy.globals("_ENV"))
```
Please note that the variable name should not include the `$` symbol.

## constant Get the Value of a Constant
```python
print(phpy.constant("PHP_OS"))
```

## eval Execute a Piece of `PHP` Code

```python
phpy.eval("var_dump(get_loaded_extensions());")
```

## call Call a `PHP` Function

It can be an extension function or a user-defined function. The first parameter is the name of the function, which must be a string. Other parameters will be passed as arguments to the called `PHP` function.

- If a parameter is of reference type, you can use `phpy.Reference()` to wrap it.
- Supports calling static methods of a class, for example: `phpy.call("Test::main"))`

```python
print(phpy.call("file_get_contents", "/tmp/file.txt"))
```