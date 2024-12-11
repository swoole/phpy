# Array Operations

`phpy.Array` is a mixed type that can either be a `List` or a `Map`.


## Creation
```python
# List
l = phpy.Array([1, 3, 5, 2023, 7, 9])
# Map
m = phpy.Array({"hello": "world", "php": "swoole"})
```


## Reading
```python
print(l[3])
print(m["php"])
```


## Length
```python
print(len(l))
print(len(m))
```


## Writing
```python
# Set Key Value
m["swoole"] = 'coroutine'
# Append element to the end
l.append(9999)
```




## Other Methods

- `get(key)` Read

- `set(key, value)` Write

- `unset(key)` Delete

- `append(value)` Append element to the end of the list

- `count()` Read elements
- `collect()` Convert to native `Python` `dict` or `list`
- `is_list()` Check if the array is a `List`
