mean_filter = itk.MeanImageFilter.New(image, radius=5)
mean_filter.Update()
mean_filtered_image = mean_filter.GetOutput()
view(mean_filtered_image)