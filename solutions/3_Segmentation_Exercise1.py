input_image = itk.imread('data/BrainProtonDensitySlice.png', itk.ctype('unsigned char'))
connected_threshold = itk.ConnectedThresholdImageFilter.New(input_image)
connected_threshold.SetLower(190)
connected_threshold.SetUpper(255)
connected_threshold.SetReplaceValue( 255 )
connected_threshold.SetSeed( [100, 110] );
connected_threshold.Update()

view(connected_threshold)