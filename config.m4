dnl $Id$
dnl config.m4 for extension phpy

PHP_ARG_WITH([python_dir],
  [dir of python],
  [AS_HELP_STRING([[--with-python-dir[=DIR]]],
    [Specify python installation dir, default is /opt/anaconda3])], [no], [no])


PHP_ARG_WITH([python_version],
  [version of python],
  [AS_HELP_STRING([[--with-python-version[=VERSION]]],
    [Specify version of python, default is 3.11])], [no], [no])

PHP_ARG_WITH([python_config],
  [path of python_config],
  [AS_HELP_STRING([[--with-python-config[=PATH]]],
    [Specify path of python_config])], [no], [no])

PHP_ARG_ENABLE([phpy],
  [whether to enable phpy support],
  [AS_HELP_STRING([--enable-phpy],
    [Enable phpy support])],
  [no])

if test "$PHP_PHPY" != "no"; then
  if test "$PHP_PYTHON_CONFIG" != "no"; then
    INCLUDES="$INCLUDES $($PHP_PYTHON_CONFIG --includes)"
    LDFLAGS="$LDFLAGS $($PHP_PYTHON_CONFIG --embed --ldflags)"
  else
    if test "$PHP_PYTHON_DIR" = "no"; then
       PHP_PYTHON_DIR="/opt/anaconda3"
    fi
    if test "$PHP_PYTHON_VERSION" = "no"; then
      if test -f "${PHP_PYTHON_DIR}/bin/python"; then
        PHP_PYTHON_VERSION=$("${PHP_PYTHON_DIR}/bin/python" -c "import sys; print('%d.%d'%(sys.version_info.major, sys.version_info.minor))")
      elif test -f "${PHP_PYTHON_DIR}/python"; then
        PHP_PYTHON_VERSION=$("${PHP_PYTHON_DIR}/python" -c "import sys; print('%d.%d'%(sys.version_info.major, sys.version_info.minor))")
      else
        PHP_PYTHON_VERSION="3.11"
      fi
    fi
    AC_MSG_RESULT([PYTHON_DIR=${PHP_PYTHON_DIR}])
    AC_MSG_RESULT([PYTHON_VERSION=${PHP_PYTHON_VERSION}])

    PHP_ADD_INCLUDE("${PHP_PYTHON_DIR}/include/python${PHP_PYTHON_VERSION}")
    PHP_ADD_LIBRARY_WITH_PATH("python${PHP_PYTHON_VERSION}", "${PHP_PYTHON_DIR}/lib", PHPY_SHARED_LIBADD)
  fi

  PHP_SUBST(PHPY_SHARED_LIBADD)

  AC_DEFINE(HAVE_PHPY, 1, [ Have phpy support ])

  PHP_REQUIRE_CXX()

  CXXFLAGS="$CXXFLAGS -Wall -Wno-unused-function -Wno-deprecated -Wno-deprecated-declarations -z now"
  CXXFLAGS="$CXXFLAGS -std=c++14"

  phpy_source_file="phpy.cc \
        src/bridge/core.cc \
		src/php/object.cc src/php/type.cc src/php/error.cc src/php/iter.cc src/php/dict.cc src/php/core.cc \
		src/php/fn.cc src/php/str.cc src/php/sequence.cc src/php/list.cc  src/php/set.cc src/php/tuple.cc src/php/module.cc \
        src/python/class.cc src/python/module.cc src/python/object.cc src/python/reference.cc src/python/resource.cc src/python/callable.cc \
        "
  PHP_NEW_EXTENSION(phpy, ${phpy_source_file} , $ext_shared)
fi
