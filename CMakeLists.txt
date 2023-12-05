cmake_minimum_required(VERSION 3.16)

project(phpy)

#set(CMAKE_BUILD_TYPE Released)
set(CMAKE_CXX_STANDARD 14)
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++14 -Wall -g -z now")

file(GLOB_RECURSE SOURCE_FILES FOLLOW_SYMLINKS src/*.cc)

set(phpy_includes ./ ./include/ /opt/anaconda3/include/python3.11 /opt/php-8.1/include/php /opt/php-8.1/include/php/Zend /opt/php-8.1/include/php/main /opt/php-8.1/include/php/TSRM)
set(phpy_libraries php)
set(phpy_link_directories /usr/local/lib /opt/anaconda3/lib /opt/php-8.1/lib)

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
