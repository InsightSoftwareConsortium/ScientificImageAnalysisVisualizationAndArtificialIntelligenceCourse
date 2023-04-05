input_image = itk.imread("data/BrainProtonDensitySlice.png", itk.ctype("unsigned char"))
isolated_connected = itk.IsolatedConnectedImageFilter.New(input_image)
isolated_connected.SetSeed1([98, 112])
isolated_connected.SetSeed2([98, 136])
isolated_connected.SetUpperValueLimit(245)
isolated_connected.FindUpperThresholdOff()
isolated_connected.Update()

view(isolated_connected, ui_collapsed=True)
