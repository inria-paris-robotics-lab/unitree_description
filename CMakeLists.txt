cmake_minimum_required(VERSION 3.22)

set(PROJECT_ORG "inria-paris-robotics-lab")
set(PROJECT_NAME unitree_description)
set(PROJECT_DESCRIPTION "Description files (urdf/srdf/...) for the Unitree Go2, calibrated to INRIA Paris instances of the robot.")
set(PROJECT_URL "https://github.com/inria-paris-robotics-lab/unitree_description")

# Check if the submodule cmake have been initialized
set(JRL_CMAKE_MODULES "${CMAKE_CURRENT_LIST_DIR}/cmake")
if(EXISTS "${JRL_CMAKE_MODULES}/base.cmake")
    message(STATUS "JRL cmakemodules found in 'cmake/' git submodule")
else()
    find_package(jrl-cmakemodules QUIET CONFIG)
    if(jrl-cmakemodules_FOUND)
        get_property(
            JRL_CMAKE_MODULES
            TARGET jrl-cmakemodules::jrl-cmakemodules
            PROPERTY INTERFACE_INCLUDE_DIRECTORIES)
            message(STATUS "JRL cmakemodules found on system at ${JRL_CMAKE_MODULES}")
    else()
        message(STATUS "JRL cmakemodules not found. Let's fetch it.")
        include(FetchContent)
        FetchContent_Declare(
            "jrl-cmakemodules"
            GIT_REPOSITORY "https://github.com/jrl-umi3218/jrl-cmakemodules.git")
            FetchContent_MakeAvailable("jrl-cmakemodules")
            FetchContent_GetProperties("jrl-cmakemodules" SOURCE_DIR JRL_CMAKE_MODULES)
    endif()
endif()

# JRL-cmakemodule setup var
set(PROJECT_USE_CMAKE_EXPORT TRUE)

include("${JRL_CMAKE_MODULES}/base.cmake")
include("${JRL_CMAKE_MODULES}/python.cmake")

# Project setup
compute_project_args(PROJECT_ARGS LANGUAGES CXX)
project(${PROJECT_NAME})

add_library(${PROJECT_NAME} INTERFACE)

target_compile_definitions( ${PROJECT_NAME} INTERFACE
    $<INSTALL_INTERFACE:GO2_DESCRIPTION_MODEL_DIR="$<INSTALL_PREFIX>/share/${PROJECT_NAME}/model">
    $<BUILD_INTERFACE:GO2_DESCRIPTION_MODEL_DIR="${CMAKE_CURRENT_SOURCE_DIR}/model">
)

install(TARGETS ${PROJECT_NAME} EXPORT ${TARGETS_EXPORT_NAME})
install(DIRECTORY model DESTINATION share/${PROJECT_NAME})

# Python
findpython(REQUIRED)
add_subdirectory(python)

setup_project_finalize()