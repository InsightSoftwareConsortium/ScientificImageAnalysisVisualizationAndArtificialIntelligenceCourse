resampled_moving_image = itk.resample_image_filter(moving_image,
        transform=output_transform,
        use_reference_image=True,
        default_pixel_value=1,
        reference_image=fixed_image)
