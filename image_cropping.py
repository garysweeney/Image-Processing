#I used the following libraries, not all are required:
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from math import ceil

#Open image (I used a .tif file):
img = plt.imread ("LowDoseCT.tif")

#Display original image
original_image = plt.figure()
original_image.suptitle("Low Dose CT Scan")
original_image = plt.axis('off')
original_image = plt.imshow(img,cmap='gray')
original_image = plt.show()

#Find size of the image:
x_size, y_size = img.shape

#Suppose we want to display the central third of the image WRT to x and y:
min_x = int (x_size/3)
max_x = x_size - min_x
min_y = int (y_size/3)
max_y = y_size - min_x

cropped_img = img [min_x : max_x , min_y : max_y]

#display cropped image:
plt.imshow (cropped_img)
plt.show()
