fileName = "data/PacMan.png"
reader = itk.ImageFileReader.New(FileName=fileName)
smoother = itk.RecursiveGaussianImageFilter.New(Input=reader.GetOutput())
writer = itk.ImageFileWriter.New(Input=smoother.GetOutput())
writer.SetFileName("my_output.jpg")
writer.SetNumberOfStreamDivisions(5)
writer.Update()
