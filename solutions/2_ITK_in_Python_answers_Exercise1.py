import itk
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline

image = itk.imread('data/CBCT-TextureInput.png', itk.F)

sobel=itk.sobel_edge_detection_image_filter(image)

array = itk.array_from_image(sobel)
plt.gray()
plt.imshow(array)
plt.axis('off')
