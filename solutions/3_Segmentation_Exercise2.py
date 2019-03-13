input_image = itk.imread('data/BrainProtonDensitySlice.png', itk.ctype('unsigned char'))
isolated_connected = itk.IsolatedConnectedImageFilter.New(input_image)
isolated_connected.SetSeed1([85, 115])
isolated_connected.SetSeed2([89, 154])
isolated_connected.SetUpperValueLimit( 255 )
isolated_connected.FindUpperThresholdOff();
isolated_connected.Update()

view(isolated_connected)