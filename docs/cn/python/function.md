# 函数列表


## include 加载文件
`phpy` 模块提供了函数用于加载执行 `PHP` 的代码。
```python
phpy.include("vendor/autoload.php")
```

## globals 获取全局变量
```python
print(phpy.globals("_ENV"))
```
请注意变量名称不要添加 `$` 符号

## constant 获取常量的值
```python
print(phpy.constant("PHP_OS"))
```

## eval 执行一段 `PHP` 代码

```python
phpy.eval("var_dump(get_loaded_extensions());")
```

## call 调用 `PHP` 函数

可以是扩展函数或者用户自定义函数。第一个参数是函数的名称，必须为字符串。其他参数将作为被调用的 `PHP` 函数参数传递。

- 若某个参数是引用类型，可以使用 `phpy.Reference()` 来包裹实现
- 支持调用类的静态方法，例如：`phpy.call("Test::main"))`

```python
print(phpy.call("file_get_contents", "/tmp/file.txt"))
```
