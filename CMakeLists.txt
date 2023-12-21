cmake_minimum_required(VERSION 3.16)

project(phpy)

#set(CMAKE_BUILD_TYPE Released)
set(CMAKE_CXX_STANDARD 14)
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++14 -Wall -g -z now")

if (NOT DEFINED PHP_CONFIG)
  set(PHP_CONFIG "php-config")
endif()

if (NOT DEFINED PYTHON_CONFIG)
  set(PYTHON_CONFIG "python3-config")
endif()

file(GLOB_RECURSE SOURCE_FILES FOLLOW_SYMLINKS src/*.cc)

execute_process(COMMAND ${PHP_CONFIG} --includes
        OUTPUT_VARIABLE PHP_INCLUDES
        OUTPUT_STRIP_TRAILING_WHITESPACE
        )

execute_process(COMMAND ${PHP_CONFIG} --prefix
        OUTPUT_VARIABLE PHP_PREFIX
        OUTPUT_STRIP_TRAILING_WHITESPACE
        )

execute_process(COMMAND ${PYTHON_CONFIG} --includes
        OUTPUT_VARIABLE PYTHON_INCLUDES
        OUTPUT_STRIP_TRAILING_WHITESPACE
        )

execute_process(COMMAND ${PYTHON_CONFIG} --ldflags
        OUTPUT_VARIABLE PYTHON_LDFLAGS
        OUTPUT_STRIP_TRAILING_WHITESPACE
        )

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} ${PHP_INCLUDES} ${PYTHON_INCLUDES}")
set(CMAKE_LDFLAGS "${CMAKE_LDFLAGS} ${PYTHON_LDFLAGS}")

set(phpy_includes ./ ./include/ /opt/anaconda3/include/python3.11)
set(phpy_libraries php)
set(phpy_link_directories /usr/local/lib /opt/anaconda3/lib ${PHP_PREFIX}/lib)

if (DEFINED enable_asan)
    set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -fsanitize=address -fno-omit-frame-pointer")
endif()

set(CMAKE_SHARED_LIBRARY_PREFIX "")

add_definitions(-DHAVE_PHP_EMBED)

include_directories(BEFORE ${phpy_includes})
link_directories(${phpy_link_directories})
add_library(phpy SHARED ${SOURCE_FILES})

set_target_properties(phpy PROPERTIES OUTPUT_NAME "tests/lib/phpy")
target_link_libraries(phpy ${phpy_libraries})
