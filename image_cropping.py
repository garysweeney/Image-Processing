#I used the following libraries, not all are required:
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from math import ceil

#Open image (I used a .tif file):
img = plt.imread ("img_name.tif")

#Find size of the image:
x_size, y_size = img.shape

#Suppose we want to display the central third of the image WRT to x and y:
min_x = int (x_size/3)
max_x = x_size - min_x
min_y = int (y_size/3)
max_y = y_size - min_x

cropped_img = img [x_min : x_max, y_min : y_max]

#display cropped image:
plt.imshow (cropped_img)
plt.show()
