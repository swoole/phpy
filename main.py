import sys

sys.path.append("./tests/lib")

import phpy

s = {1, 3, 5, 2023, 7, 9}

phpy.call('var_dump', s)
rs = phpy.call('array_search', 2023, s)
print(rs)


# phpy.include("main.php")
#
# phpy.call("main")
