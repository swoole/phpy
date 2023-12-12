import sys

sys.path.append('/home/htf/workspace/python-php/tests/lib')
sys.path.append('/home/htf/workspace/python-php/lib')

from php import curl

ch = curl.init("https://www.baidu.com/")
curl.setopt(ch, curl.CURLOPT_RETURNTRANSFER, True)
rs = curl.exec(ch)
print(rs)
