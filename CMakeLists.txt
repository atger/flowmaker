cmake_minimum_required(VERSION 3.25)

project("FlowMaker" 
    VERSION "0.1"
    DESCRIPTION "Application to write bioinformatics workflows"
    LANGUAGES CXX
)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

find_package(Qt6 REQUIRED COMPONENTS Core Gui Qml Quick QuickControls2)
qt_standard_project_setup()

add_subdirectory(src)