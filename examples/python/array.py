import phpy
import math

phpy.include("./tests/lib/PhpyObject.php")
phpy.include("./tests/lib/TestClass.php")


print(phpy.call('memory_get_usage'))
for i in range(32):
    items = phpy.globals('_SERVER')

print(phpy.call('memory_get_usage'))
