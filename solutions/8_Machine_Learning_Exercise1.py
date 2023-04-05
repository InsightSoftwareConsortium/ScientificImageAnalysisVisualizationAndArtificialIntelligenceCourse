## cast the image type
InputImageType = type(itk_img)
OutputImageType = ImageType = itk.Image[itk.F, 3]  # type(well_callibrated_image)
cast_filter = itk.CastImageFilter[InputImageType, OutputImageType].New()
cast_filter.SetInput(itk_img)
cast_filter.Update()
casted_img = cast_filter.GetOutput()

cast_filter2 = itk.CastImageFilter[InputImageType, OutputImageType].New()
cast_filter2.SetInput(well_callibrated_image)
cast_filter2.Update()
casted_ref = cast_filter.GetOutput()

## align the histogram to the training image
histo_match_filter = itk.HistogramMatchingImageFilter[
    OutputImageType, OutputImageType
].New()
histo_match_filter.SetInput(casted_img)
histo_match_filter.SetReferenceImage(casted_ref)
histo_match_filter.Update()
matched_image = histo_match_filter.GetOutput()

## normalize the image
preprocessed_img = itk.normalize_image_filter(matched_image)

# template statistics
statistics_template = itk.StatisticsImageFilter[type(well_callibrated_image)].New()
statistics_template.SetInput(well_callibrated_image)
statistics_template.Update()
print(
    "Statistics of a template image, mean: {}, sigma: {}, min: {}, max: {}".format(
        statistics_template.GetMean(),
        statistics_template.GetSigma(),
        statistics_template.GetMinimum(),
        statistics_template.GetMaximum(),
    )
)
print("==============")
# new data statistics
statistics_image = itk.StatisticsImageFilter[type(preprocessed_img)].New()
statistics_image.SetInput(preprocessed_img)
statistics_image.Update()
print(
    "Statistics of the test image after preprocessing, mean: {}, sigma: {}, min: {}, max: {}".format(
        statistics_image.GetMean(),
        statistics_image.GetSigma(),
        statistics_image.GetMinimum(),
        statistics_image.GetMaximum(),
    )
)
