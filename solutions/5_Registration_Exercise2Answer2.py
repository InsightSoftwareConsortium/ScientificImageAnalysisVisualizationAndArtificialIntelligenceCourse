resampler = itk.ResampleImageFilter.New(
    Input=movingImage,
    Transform=outputCompositeTransform,
    UseReferenceImage=True,
    ReferenceImage=fixedImage,
)
