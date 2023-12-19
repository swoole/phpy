import phpy
import random
from php import std

m1 = phpy.call('memory_get_usage')
c = 128
total = 0
for i in range(1, c):
    s = phpy.call('random_bytes', 8192 * i)
    assert s.len() == 8192 * i
    total += s.len()

m2 = phpy.call('memory_get_usage')
print(m2 - m1)
print(total)

