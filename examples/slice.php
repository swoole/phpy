<?php
$s = new PyStr("Python Programming");

# 获取前三个字符
# Python: print(s[0:3])
PyCore::print($s[PyCore::slice(0, 3)]);  # 输出: "Pyt"

# 获取从索引 7 到索引 12 的字符
# Python: print(s[7:12])  # 输出: "Progr"
PyCore::print($s[PyCore::slice(7, 12)]);  # 输出: "Progr"

# 获取整个字符串
# Python: print(s[:])  # 输出: "Python Programming"
PyCore::print($s[PyCore::slice(null)]);  # 输出: "Python Programming

# 使用步长
# Python: print(s[::2])  # 输出: "Pto rgamn"（每两个字符取一个）
PyCore::print($s[PyCore::slice(null, null, 2)]);  # 输出: "Pto rgamn"

# 反向切片
# Python: print(s[::-1])  # 输出: "gnimmargorP nohtyP"（字符串反转）
PyCore::print($s[PyCore::slice(null, null, -1)]);  # 输出: "gnimmargorP nohtyP"

# 获取最后一个字符
# Python: print(s[-1])  # 输出: "g"
PyCore::print($s[PyCore::slice(-1, null)]);  # 输出: "g"

# 获取倒数第三个到倒数第一个字符
# Python: print(s[-3:-1])  # 输出: "in"
PyCore::print($s[PyCore::slice(-3, -1)]);  # 输出: "in"
