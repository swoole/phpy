import sys

sys.path.append('/home/htf/workspace/python-php/tests/lib')
sys.path.append('/home/htf/workspace/python-php/lib')

from php import core

print(core.zend_version())
