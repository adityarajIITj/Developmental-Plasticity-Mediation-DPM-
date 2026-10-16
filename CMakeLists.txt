cmake_minimum_required(VERSION 3.20)
project(DPMResearchScaffold VERSION 0.1.0 LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

add_library(dpm_core
    src/dpm/core.cpp
)
target_include_directories(dpm_core PUBLIC src)

include(CTest)
if(BUILD_TESTING)
    add_executable(dpm_scaffold_test tests/test_scaffold.cpp)
    target_link_libraries(dpm_scaffold_test PRIVATE dpm_core)
    add_test(NAME dpm_scaffold_test COMMAND dpm_scaffold_test)
endif()
