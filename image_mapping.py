#I used the following libraries:
import matplotlib.pyplot as plt
from PIL import Image
import cv2

#Load the image and sub-image (I used .tif files):
img = plt.imread ("image_name.tif")
sub_img = plt.imread ("subimage_name.tif")

#Can introduce Gaussian noise:
"""std_dev = 60
r = std_dev * np.random.rand(xsize,ysize)
r_new = r.astype(np.uint8)
new_img = img + r_new"""

#Obtain parameters of the sub-image:
width, height = sub_img.shape

#I used the following correlation method:
method = cv2.TM_CCOEFF_NORMED

#Match sub-image with image:
correlation = cv2.matchTemplate (img, sub_img, method)

#Find the locations of maximum and minimum correlation:
min_corr, max_corr, min_loc, max_loc = cv2.minMaxLoc(corr)

#Create a rectangle to match image and sub-image:
top_left = max_loc
bottom_right = (top_left[0] + width, top_left[0] + height)
rect = cv2.rectangle(img, top_left, bottom_right, 255, 10)

#Display the result where the sub-image was found in the large image:
plt.imshow (rect)
plt.show()





