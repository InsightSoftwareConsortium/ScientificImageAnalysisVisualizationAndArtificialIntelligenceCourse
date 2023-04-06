file_name = "data/PacMan.png"
reader = itk.ImageFileReader.New(FileName=file_name)
smoother = itk.RecursiveGaussianImageFilter.New(Input=reader.GetOutput())
smoother.SetSigma(5.0)
smoother.Update()
view(smoother.GetOutput(), ui_collapsed=True)
