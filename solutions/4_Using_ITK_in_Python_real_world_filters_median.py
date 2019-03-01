median_filtered_image = itk.median_image_filter(image, radius = 5)
view(median_filtered_image)