clang-format -i src/python/*.cc
clang-format -i src/php/*.cc
clang-format -i src/bridge/*.cc
clang-format -i include/*.h

composer cs-fix stubs/
