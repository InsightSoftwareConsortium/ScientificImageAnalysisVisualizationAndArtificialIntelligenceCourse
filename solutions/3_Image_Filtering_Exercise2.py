file_name = "data/PacMan.png"
reader = itk.ImageFileReader.New(FileName=file_name)
smoother = itk.RecursiveGaussianImageFilter.New(Input=reader.GetOutput())
smoother.SetSigma(5.0)
smoother.Update()
smoother.SetSigma(smoother.GetSigma())
# smoother.Modified()
smoother.Update()
