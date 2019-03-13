import itk
import numpy as np

im=itk.imread('data/KitwareITK.jpg', itk.UC)
arr = itk.array_from_image(im)
arr[0,0]
print("Pixel in array: %f"%arr[0,0])
arr[0,0]=125
print("Pixel in array: %f"%arr[0,0])
print("Pixel in image: %f"%im.GetPixel([0,0]))
