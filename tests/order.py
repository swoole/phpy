import phpy

phpy.include("./tests/lib/bridge_helpers.php")

cb2 = phpy.call("phpy_kw_closure")
assert cb2(a=3, b=7) == 37, "kw closure failed"

s = phpy.String("hello")
s2 = s + " world"
assert str(s2) == "hello world", "concat failed: %r" % str(s2)
print("OK")
