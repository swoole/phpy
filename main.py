import sys

sys.path.append("./tests/lib")

import phpy

o = phpy.Object('redis')
assert o.call('connect', '127.0.0.1', 6379)
# rdata = phpy.call('uniqid')
# assert o.call('set', 'key', rdata)
# assert o.call('get', 'key') == rdata

# phpy.include("main.php")
#
# phpy.call("main")
