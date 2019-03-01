import itk
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline

im=itk.imread('data/CBCT-TextureInput.png', itk.F)
sobel=itk.sobel_edge_detection_image_filter(im)
arr = itk.array_from_image(sobel)
plt.gray()
plt.imshow(arr)
plt.axis('off')
