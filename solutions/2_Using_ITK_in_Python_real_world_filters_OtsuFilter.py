InputImageType = itk.Image[itk.ctype('float'), 2]
OutputImageType = itk.Image[itk.ctype('short'), 2]

otsu_filter = itk.OtsuThresholdImageFilter[InputImageType, OutputImageType].New()
otsu_filter.SetInput(image)
otsu_filter.Update()
otsu_filtered_image = otsu_filter.GetOutput()
view(otsu_filtered_image, ui_collapsed=True)
