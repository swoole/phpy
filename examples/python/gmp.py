from php import gmp

sum = gmp.add("123456789012345", "76543210987655")
print(gmp.strval(sum))
