#The libraries I used, not all are required. 
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from math import ceil
import scipy.fftpack
from scipy.fft import fft, ifft
import scipy.io
from scipy.io import loadmat
from scipy import signal
import cv2

#import the image
#Can use matplotlib or openCV
img_plt = plt.imread ("img_name.jpg")
img_cv2 = cv2.imread ("img_name.jpg")

#The following code is used for Matplotlib:
#To get the red channel we use:
red_img = img_plt[:,:,0]
#To get the green channel we use:
red_img = img_plt[:,:,1]
#To get the blue channel we use:
red_img = img_plt[:,:,2]

#OpenCV allows for much easier splitting:
b_img, g_img, r_img = cv2.split (img_cv2)

#If we want to merge the channels, do the following:
#Create a zero matrix to sub in for the channel we want to eliminate:
zeros = np.zeros (b_img.shape, np.uint8)  #The shape of all three channels is the same.

#Merging:
b_g_img = cv2.merge (b_img, g_img, zeros)
b_r_img = cv2.merge (b_img, zeros, r_img)
g_r_img = cv2.merge (zeros, g_img, r_img)

#If we want our results in grayscale:
bg_to_gray = cv2.cvtColor (b_g_img, cv2.COLOR_BGR2GRAY)
br_to_gray = cv2.cvtColor (b_r_img, cv2.COLOR_BGR2GRAY)
gr_to_gray = cv2.cvtColor (g_r_img, cv2.COLOR_BGR2GRAY)

#Displaying using OpenCV:
cv2.imshow("Blue Channel", b_img)
cv2.imshow("Green Channel", g_img)
cv2.imshow("Red Channel", r_img)
cv2.imshow("Blue-Green Channel", b_g_img)
cv2.imshow("Blue-Red Channel", b_r_img)
cv2.imshow("Green-Red Channel", g_r_img)
cv2.imshow("Blue-Green Channel in Gray", bg_to_gray)
cv2.imshow("Blue-Red Channel in Gray", br_to_gray)
cv2.imshow("Green-Red Channel in Gray", gr_to_gray)
cv2.waitKey(0)
cv2.destroyAllWindows()

