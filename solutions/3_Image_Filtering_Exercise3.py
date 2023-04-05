file_name = "data/PacMan.png"
reader = itk.ImageFileReader.New(FileName=file_name)

# `view` returns the widget object
viewer = view(image, annotations=False)

# Create an itk smoother filter object. By re-using the object, output memory-reallocation is avoided
smoother = itk.MedianImageFilter.New(reader.GetOutput())


# Define a function to use with ipywidgets `interactive`
def smooth_and_view(radius=2):
    smoother.SetRadius(radius)
    smoother.Update()
    # Update the image used in the viewer
    viewer.image = smoother.GetOutput()


slider = interactive(smooth_and_view, radius=(0, 10, 1))

widgets.VBox([viewer, slider])
