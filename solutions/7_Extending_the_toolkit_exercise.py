textures = itk.coocurrence_texture_features_image_filter(
    image,
    mask_image=mask,
    number_of_bins_per_axis=10,
    histogram_minimum=0,
    histogram_maximum=4200,
    neighborhood_radius=6,
)
texture_array = itk.array_view_from_image(textures)
view(
    texture_array[:, :, :, 1].reshape(texture_array.shape[:-1]).copy(),
    mode="z",
    cmap="jet",
)
