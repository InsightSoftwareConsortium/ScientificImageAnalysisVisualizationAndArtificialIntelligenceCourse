registration = itk.ImageRegistrationMethodv4.New(
    FixedImage=fixedImage,
    MovingImage=movingImage,
    Metric=metric,
    Optimizer=optimizer,
    InitialTransform=initialTransform,
)
