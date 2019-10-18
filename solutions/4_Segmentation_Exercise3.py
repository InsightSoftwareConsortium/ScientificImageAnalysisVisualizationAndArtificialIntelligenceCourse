line = 0

if line == 0:
    basin_minimum = 1
    boundary_minimum = 5.0
    propagation_scaling = 1.0
    curvature_scaling = 2.0
    number_of_iterations = 100
elif line == 1:
    basin_minimum = 1
    boundary_minimum = 5.0
    propagation_scaling = 1.0
    curvature_scaling = 2.0
    number_of_iterations = 500
elif line == 2:
    basin_minimum = 1
    boundary_minimum = 5.0
    propagation_scaling = 1.0
    curvature_scaling = 4.0
    number_of_iterations = 100
else:
    basin_minimum = 1
    boundary_minimum = 20.0
    propagation_scaling = 1.0
    curvature_scaling = 1.0
    number_of_iterations = 100

explore_shape_detection_image_parameters(basin_minimum, boundary_minimum, 
                                         propagation_scaling, curvature_scaling, number_of_iterations)