cmake_minimum_required(VERSION 3.2)
project(VisualDL)

find_program(CCACHE_FOUND ccache)
if(CCACHE_FOUND)
  set_property(GLOBAL PROPERTY RULE_LAUNCH_COMPILE ccache)
  set_property(GLOBAL PROPERTY RULE_LAUNCH_LINK ccache)
endif(CCACHE_FOUND)

set(CMAKE_MODULE_PATH ${CMAKE_MODULE_PATH} "${CMAKE_CURRENT_SOURCE_DIR}/cmake")
set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_FLAGS "-fPIC")


set(THIRD_PARTY_PATH "${CMAKE_BINARY_DIR}/third_party" CACHE STRING
        "A path setting third party libraries download & build directories.")

include(external/zlib)      # download, build, install zlib
if (NOT ON_RELEASE)
  include(external/gflags)    # download, build, install gflags
  include(external/glog)      # download, build, install glog
endif(NOT ON_RELEASE)
include(external/gtest)     # download, build, install gtest
include(external/eigen)     # download eigen
include(external/pybind11)  # download pybind11
include(external/protobuf)  # download, build, install protobuf
include(external/python)    # find python and set path
