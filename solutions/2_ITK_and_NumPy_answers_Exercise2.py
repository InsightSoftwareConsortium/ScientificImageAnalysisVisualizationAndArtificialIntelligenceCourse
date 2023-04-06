import itk
import numpy as np

image = itk.imread("data/KitwareITK.jpg", itk.UC)
array = itk.array_from_image(image)

array[0, 0]
print(f"Pixel in array: {array[0,0]}")

array[0, 0] = 125
print(f"Pixel in array: {array[0,0]}")
print(f"Pixel in image: {image.GetPixel([0,0])}")
