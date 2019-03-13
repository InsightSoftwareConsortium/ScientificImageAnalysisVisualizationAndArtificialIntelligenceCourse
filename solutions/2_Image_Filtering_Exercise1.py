fileName = 'data/PacMan.png'
reader = itk.ImageFileReader.New(FileName=fileName)
smoother = itk.RecursiveGaussianImageFilter.New(Input=reader.GetOutput())
smoother.SetSigma(5.0)
smoother.Update()
view(smoother.GetOutput())