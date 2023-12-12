import sys

sys.path.append('/home/htf/workspace/python-php/tests/lib')
sys.path.append('/home/htf/workspace/python-php/lib')

from php import gmp

sum = gmp.add("123456789012345", "76543210987655")
print(gmp.strval(sum))
