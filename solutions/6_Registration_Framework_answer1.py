registration = itk.ImageRegistrationMethodv4.New(fixed_image=fixed_image,
        moving_image=moving_image,
        metric=metric,
        optimizer=optimizer,
        initial_transform=initial_transform)
