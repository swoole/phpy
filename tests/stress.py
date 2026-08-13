import phpy

phpy.include("./tests/lib/bridge_helpers.php")
cb = phpy.call("phpy_kw_closure")

for i in range(3000):
    r = cb(a=i, b=i + 1)
    assert r == i * 10 + (i + 1), (i, r)
    s = phpy.String("hello world number %d" % (i % 7))
    s2 = s + "!"
    assert str(s2).endswith("!")
    # correctness of `in` must hold
    assert ("world" in s) is True
    assert ("nope_xyz" in s) is False
    if i % 500 == 0:
        pass
print("STRESS OK")
