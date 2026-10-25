add_executable(lingmo-toolkit-demo
    demo/main.cpp
)

target_link_libraries(lingmo-toolkit-demo PRIVATE lingmo-toolkit)

add_executable(lingmo-toolkit-gallery
    gallery/main.cpp
)

target_link_libraries(lingmo-toolkit-gallery PRIVATE lingmo-toolkit)
