dnl $Id$
dnl config.m4 for extension phpy

PHP_ARG_WITH([python_version],
  [version of python],
  [AS_HELP_STRING([[--with-python-version[=VERSION]]],
    [Specify version of python, or use default (ex: 3.12)])], [no], [no])

PHP_ARG_ENABLE([phpy],
  [whether to enable phpy support],
  [AS_HELP_STRING([--enable-phpy],
    [Enable phpy support])],
  [no])

if test "$PHP_PHPY" != "no"; then
  dnl modern version use python3-embed, old (<= 3.6) use python3
  if test "$PHP_PYTHON_VERSION" = "no"; then
    PKG_CHECK_MODULES([PYTHON], [python3-embed],,
      [PKG_CHECK_MODULES([PYTHON], [python3])]
    )
  else
    PKG_CHECK_MODULES([PYTHON], [python-${PHP_PYTHON_VERSION}-embed],,
      [PKG_CHECK_MODULES([PYTHON], [python-${PHP_PYTHON_VERSION}])]
    )
  fi
  PHP_EVAL_LIBLINE($PYTHON_LIBS, PHPY_SHARED_LIBADD)
  PHP_EVAL_INCLINE($PYTHON_CFLAGS)

  PHP_REQUIRE_CXX()

  PHP_SUBST(PHPY_SHARED_LIBADD)

  AC_DEFINE(HAVE_PHPY, 1, [ Have phpy support ])

  EXTRAS_CXXFLAGS="-Wall -Wno-unused-function -Wno-deprecated -Wno-deprecated-declarations -z now"
  EXTRAS_CXXFLAGS="$EXTRAS_CXXFLAGS -std=c++14"

  if test -f "$abs_srcdir/phpy.cc"; then
      phpy_source_dir=$abs_srcdir
  elif test -f "phpy.cc"; then
      phpy_source_dir=$(pwd)
  else
      phpy_source_dir="ext/phpy"
  fi

    dnl AC_MSG_RESULT([$phpy_source_dir])

    phpy_source_files=$(cd $phpy_source_dir && find src -type f -name "*.cc")
    phpy_source_files="phpy.cc $phpy_source_files"

    PHP_NEW_EXTENSION(phpy, $phpy_source_files , $ext_shared,, $EXTRAS_CXXFLAGS, cxx)

  dnl AC_MSG_RESULT([$ext_builddir])

    PHP_ADD_INCLUDE([$ext_srcdir/include])
    PHP_ADD_BUILD_DIR($ext_builddir/src)
    PHP_ADD_BUILD_DIR($ext_builddir/src/bridge)
    PHP_ADD_BUILD_DIR($ext_builddir/src/php)
    PHP_ADD_BUILD_DIR($ext_builddir/src/python)
fi
