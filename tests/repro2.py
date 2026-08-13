import phpy

phpy.include("./tests/lib/bridge_helpers.php")

cb = phpy.call("phpy_kw_closure")
print("kw result:", cb(a=3, b=7))  # expect 37

s = phpy.String("hello world")
print("str:", str(s))
print("xyz in s (expect False):", ("xyz" in s))
print("world in s (expect True):", ("world" in s))
