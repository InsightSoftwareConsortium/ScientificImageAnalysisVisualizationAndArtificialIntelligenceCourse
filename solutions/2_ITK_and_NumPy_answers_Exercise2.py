import itk
import numpy as np

image = itk.imread('data/KitwareITK.jpg', itk.UC)
array = itk.array_from_image(image)

array[0,0]
print("Pixel in array: %f" % array[0,0])

array[0,0] = 125
print("Pixel in array: %f" % array[0,0])
print("Pixel in image: %f" % image.GetPixel([0,0]))
