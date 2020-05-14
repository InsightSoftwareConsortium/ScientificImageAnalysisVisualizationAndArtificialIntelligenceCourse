median_filtered_image = itk.MedianImageFilter(image, radius=5)
view(median_filtered_image, ui_collapsed=True)
