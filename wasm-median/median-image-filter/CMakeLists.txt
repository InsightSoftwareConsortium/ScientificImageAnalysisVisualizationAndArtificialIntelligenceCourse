add_executable(median-image-filter median-image-filter.cxx)
target_link_libraries(median-image-filter PUBLIC ${ITK_LIBRARIES})

add_test(NAME median-image-filter-help COMMAND median-image-filter --help)
