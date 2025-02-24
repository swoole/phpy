dnl $Id$
dnl config.m4 for extension phpy

PHP_ARG_WITH([python_dir],
  [dir of python],
  [AS_HELP_STRING([[--with-python-dir[=DIR]]],
    [Specify python installation dir])], [no], [no])

PHP_ARG_WITH([python_version],
  [version of python],
  [AS_HELP_STRING([[--with-python-version[=VERSION]]],
    [Specify version of python])], [no], [no])

PHP_ARG_WITH([python_config],
  [path of python_config],
  [AS_HELP_STRING([[--with-python-config[=PATH]]],
    [Specify path of python_config, the default is python3-config])], [no], [no])

PHP_ARG_ENABLE([phpy],
  [whether to enable phpy support],
  [AS_HELP_STRING([--enable-phpy],
    [Enable phpy support])],
  [no])

AC_DEFUN([GET_PYTHON_LDFLAGS], [
  TMP_RESULT="$($PHP_PYTHON_CONFIG --embed --ldflags)"
  if test $? -eq 0; then
      PYTHON_LDFLAGS="$TMP_RESULT"
  elif test $? -eq 1; then
      PYTHON_LDFLAGS="$LDFLAGS $($PHP_PYTHON_CONFIG --ldflags)"
  else
      AC_MSG_ERROR([failed to execute `$PHP_PYTHON_CONFIG --ldflags`])
  fi
  LDFLAGS="$LDFLAGS $PYTHON_LDFLAGS"
])

AC_DEFUN([GET_PYTHON_INCLUDES], [
  TMP_RESULT="$INCLUDES $($PHP_PYTHON_CONFIG --includes)"
  if test $? -eq 0; then
      INCLUDES="$INCLUDES $TMP_RESULT"
  else
      AC_MSG_ERROR([failed to execute `$PHP_PYTHON_CONFIG --includes`])
  fi
])

AC_DEFUN([GET_PYTHON_VERSION_WITH_PYTHON_DIR], [
  PHP_PYTHON_VERSION=$("${PHP_PYTHON_DIR}/bin/python3" -c "import sys; print('%d.%d'%(sys.version_info.major, sys.version_info.minor))")
  if test $? -ne 0; then
      AC_MSG_ERROR([failed to execute `python3`])
  fi
])

if test "$PHP_PHPY" != "no"; then
  if test "$PHP_PYTHON_CONFIG" != "no"; then
    GET_PYTHON_INCLUDES()
    GET_PYTHON_LDFLAGS()
  elif test "$PHP_PYTHON_DIR" != "no"; then
    GET_PYTHON_VERSION_WITH_PYTHON_DIR()
    AC_MSG_RESULT([Python DIR: ${PHP_PYTHON_DIR}])
    AC_MSG_RESULT([Python Version: ${PHP_PYTHON_VERSION}])
    PHP_ADD_LIBRARY("python${PHP_PYTHON_VERSION}", 1, PHPY_SHARED_LIBADD)
    PHP_ADD_LIBPATH("${PHP_PYTHON_DIR}/lib/python${PHP_PYTHON_VERSION}", PHPY_SHARED_LIBADD)
    PHP_ADD_INCLUDE("${PHP_PYTHON_DIR}/include/python${PHP_PYTHON_VERSION}")
  elif test "$PHP_PYTHON_VERSION" != "no"; then
    AC_MSG_RESULT([Python Version: ${PHP_PYTHON_VERSION}])
    dnl modern version use python3-embed, old (<= 3.6) use python3
    PKG_CHECK_MODULES([PYTHON], [python-${PHP_PYTHON_VERSION}-embed],,
      [PKG_CHECK_MODULES([PYTHON], [python-${PHP_PYTHON_VERSION}])]
    )
    PHP_EVAL_LIBLINE($PYTHON_LIBS, PHPY_SHARED_LIBADD)
    PHP_EVAL_INCLINE($PYTHON_CFLAGS)
  else
    PHP_PYTHON_CONFIG="python3-config"
    GET_PYTHON_INCLUDES()
    GET_PYTHON_LDFLAGS()
  fi

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
