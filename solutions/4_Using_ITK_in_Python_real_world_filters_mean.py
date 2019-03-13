mean_filtered_image = itk.mean_image_filter(image, radius = 5)
view(mean_filtered_image)