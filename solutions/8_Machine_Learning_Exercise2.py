## review the statistics
statistics_image = itk.StatisticsImageFilter[type(norm_cast_hipp_slice)].New()
statistics_image.SetInput(norm_cast_hipp_slice)
statistics_image.Update()
print('Statistics of a template image, mean: {}, sigma: {}, min: {}, max: {}'
      .format(statistics_template.GetMean(), 
      statistics_template.GetSigma(), 
      statistics_template.GetMinimum(), 
      statistics_template.GetMaximum())) 
print('==============')
print('Statistics of the transformed data, mean: {}, sigma: {}, min: {}, max: {}'
.format(statistics_image.GetMean(), 
      statistics_image.GetSigma(), 
      statistics_image.GetMinimum(), 
      statistics_image.GetMaximum())) 