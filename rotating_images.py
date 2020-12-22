#Rotating an image by means of the Rotational matrix.
#Commonly used in modern physics courses when dealing with rotating reference frames.

#Libraries I used.
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from math import ceil
import scipy.io
from scipy.io import loadmat
from scipy import signal

#Read image (.tif file).
img = plt.imread ("img_name.tif")

#Display the original image
original_fig = plt.figure()
original_fig.suptitle ("Original Image")
plt.imshow(img)
plt.show()

#get size of the image:
x_size, y_size = img.shape

#Find the midpoint of the image, this will be the basis of rotation.
mid_x = np.ceil (x_size/2)
mid_y = np.ceil (y_size/2)

#Create a mesh grid the same size as the image.
x = np.linspace (0, x_size, x_size)
y = np.linspace (0, y_size, y_size)
x_new, y_new = np.meshgrid (x,y)

#Declare the angle of rotation (in rads).
theta = 0

#Rotation matrix has the following setup for two dimensions:
# [ cos (-)    -sin (-) ]
# [ sin (-)     cos (-) ]
# When applying to our coordinates we get:
x_rotate = mid_x + (x_new - mid_x) * np.cos (theta) - (y_new - mid_y) * np.sin (theta)
y_rotate = mid_y + (x_new - mid_x) * np.sin (theta) + (y_new - mid_y) * np.cos (theta)

#Map the rotation into new image.
rotated_image =  scipy.ndimage.map_coordinates (img, (y_rotate, x_rotate))

#Display rotated image.
rotated_img = plt.figure()
rotated_img.suptitle ("Rotated Image")
plt.imshow(rotated_image)
plt.axis('off')
plt.show()



