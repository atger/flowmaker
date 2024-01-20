qt_add_executable(flowmaker 
    main.cpp
)

file(GLOB_RECURSE _qml RELATIVE ${CMAKE_CURRENT_SOURCE_DIR} "*.qml")
message(STATUS "FILES: ${_qml}")
qt_add_resources(flowmaker "qml"
    FILES
        ${_qml}
)

target_link_libraries(flowmaker
    PUBLIC
        Qt6::Core
        Qt6::Gui
        Qt6::Qml
        Qt6::Quick
        Qt6::QuickControls2
)

set_target_properties(flowmaker PROPERTIES
    WIN32_EXECUTABLE ON
    MACOSX_BUNDLE ON
)