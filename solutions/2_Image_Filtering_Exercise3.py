fileName = 'data/PacMan.png'
reader = itk.ImageFileReader.New(FileName=fileName)
smoother = itk.MedianImageFilter.New(Input=reader.GetOutput())
smoother.SetRadius(5)
smoother.Update()
view(smoother)