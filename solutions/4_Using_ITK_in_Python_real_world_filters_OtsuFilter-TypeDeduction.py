otsu_filter = itk.OtsuThresholdImageFilter.New(image)
otsu_filter.Update()
otsu_filtered_image = otsu_filter.GetOutput()
print(otsu_filtered_image)