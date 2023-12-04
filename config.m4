dnl config.m4 for extension phpy

dnl Comments in this file start with the string 'dnl'.
dnl Remove where necessary.

dnl If your extension references something external, use 'with':

dnl PHP_ARG_WITH([phpy],
dnl   [for phpy support],
dnl   [AS_HELP_STRING([--with-phpy],
dnl     [Include phpy support])])

dnl Otherwise use 'enable':

PHP_ARG_ENABLE([phpy],
  [whether to enable phpy support],
  [AS_HELP_STRING([--enable-phpy],
    [Enable phpy support])],
  [no])

if test "$PHP_PHPY" != "no"; then
  dnl Write more examples of tests here...

  dnl Remove this code block if the library does not support pkg-config.
  dnl PKG_CHECK_MODULES([LIBFOO], [foo])
  dnl PHP_EVAL_INCLINE($LIBFOO_CFLAGS)
  dnl PHP_EVAL_LIBLINE($LIBFOO_LIBS, PHPY_SHARED_LIBADD)

  dnl If you need to check for a particular library version using PKG_CHECK_MODULES,
  dnl you can use comparison operators. For example:
  dnl PKG_CHECK_MODULES([LIBFOO], [foo >= 1.2.3])
  dnl PKG_CHECK_MODULES([LIBFOO], [foo < 3.4])
  dnl PKG_CHECK_MODULES([LIBFOO], [foo = 1.2.3])

  dnl Remove this code block if the library supports pkg-config.
  dnl --with-phpy -> check with-path
  dnl SEARCH_PATH="/usr/local /usr"     # you might want to change this
  dnl SEARCH_FOR="/include/phpy.h"  # you most likely want to change this
  dnl if test -r $PHP_PHPY/$SEARCH_FOR; then # path given as parameter
  dnl   PHPY_DIR=$PHP_PHPY
  dnl else # search default path list
  dnl   AC_MSG_CHECKING([for phpy files in default path])
  dnl   for i in $SEARCH_PATH ; do
  dnl     if test -r $i/$SEARCH_FOR; then
  dnl       PHPY_DIR=$i
  dnl       AC_MSG_RESULT(found in $i)
  dnl     fi
  dnl   done
  dnl fi
  dnl
  dnl if test -z "$PHPY_DIR"; then
  dnl   AC_MSG_RESULT([not found])
  dnl   AC_MSG_ERROR([Please reinstall the phpy distribution])
  dnl fi

  dnl Remove this code block if the library supports pkg-config.
  dnl --with-phpy -> add include path
  dnl


  PHP_ADD_INCLUDE(/opt/anaconda3/include/python3.11)
  PHP_ADD_LIBRARY_WITH_PATH(python3.11, /opt/anaconda3/lib, PHPY_SHARED_LIBADD)
  PHP_SUBST(PHPY_SHARED_LIBADD)

  dnl In case of no dependencies
  AC_DEFINE(HAVE_PHPY, 1, [ Have phpy support ])

  PHP_REQUIRE_CXX()

  CXXFLAGS="$CXXFLAGS -Wall -Wno-unused-function -Wno-deprecated -Wno-deprecated-declarations -z now"
  CXXFLAGS="$CXXFLAGS -std=c++14"

  swoole_source_file="phpy.cc \
        src/bridge/core.cc \
		src/php/object.cc src/php/type.cc src/php/dict.cc  src/php/core.cc src/php/fn.cc src/php/str.cc src/php/sequence.cc src/php/list.cc  src/php/set.cc src/php/tuple.cc src/php/module.cc \
        src/python/class.cc src/python/module.cc src/python/object.cc src/python/reference.cc src/python/resource.cc src/python/callable.cc \
        "

  PHP_NEW_EXTENSION(phpy, ${swoole_source_file} , $ext_shared)
fi
