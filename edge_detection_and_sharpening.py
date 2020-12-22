#I used these libraries, but not all are required.
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

#Read image (.tif file).
img = plt.imread("image_name.tif")

#Display the image.
original_fig = plt.figure()
original_fig.suptitle("Original Image")
plt.imshow(img, cmap = 'gray')  #cmap = 'gray' displays a grayscale version of the image.
plt.axis('off')
plt.show()

#To sharpen the edges of an image or show the edges in the image the Laplacian fiter is commonly used.
#Involves taking the derivative with respect to pixel edges to sharped and show prevelant edges in the image.
#I found these two version to work best for the purpose.
#Edge detection:
Laplace_edge_detection = [[ 0.33333333,  0.33333333,  0.33333333],
                          [ 0.33333333, -2.66666667,  0.33333333],
                          [ 0.33333333,  0.33333333,  0.33333333]]
                          
#Sharpening:
Laplace_sharpening = [[0,-1,0],[-1,8,-1],[0,-1,0]]

#Need to pad with 0s to ensure that both matrices are the same size as the image we plan to convolve with:
#Find the image size:
x_size, y_size = img.shape
kern_edge_x, kern_edge_y = Laplace_edge_detection.shape 
kern_sharp_x, kern_sharp_y = Laplace_sharpening.shape 

#Pad both matrices: 
#Take the size of the matrix, subtract size of kernel, and divide by 2:
pad_edge_x = (x_size - kern_edge_x)/2
pad_edge_y = (y_size - kern_edge_y)/2
pad_sharp_x = (x_size - kern_sharp_x)/2
pad_sharp_x = (y_size - kern_sharp_y)/2

#for an uneven image, i.e., result is not a round number, add 1 to one side and reduby by 1 on other. 
Laplace_edge = np.pad (Laplace_edge_detection (pad_edge_x, pad_edge_y)
Laplace_sharp = np.pad (Laplace_sharpening (pad_sharp_x, pad_sharp_y)

#To use with the image we must convolve by transforming into frequency space and multiplying:
ft_img = np.fft.fft2 (np.fft.fftshift (img))
ft_Laplace_edge = np.fft.fft2 (Laplace_edge)
ft_Laplace_sharp = np.fft.fft2 (Laplace_sharp)
ft_result_edge = ft_img * ft_Laplace_edge #Gives edge detection in image.
ft_result_sharp = ft_img * ft_Laplace_sharp #Gives edge sharpening in image.

#Transform back to image space:
result_edge = np.fft.ifft2 (ft_result_edge))
result_sharp = np.fft.ifft2 (ft_result_sharp))

#Display against original image:
edge_fig, (axis1, axis2) = plt.subplots(1,2)
axis1.imshow(original_img,cmap='gray')
axis1.set_title("Original Image")
axis1.axis('off')
axis2.imshow(result_edge,cmap='gray')
axis2.set_title("Edge Detection")
axis2.axis('off')
plt.show()

sharp_fig, (axis1, axis2) = plt.subplots(1,2)
axis1.imshow(img,cmap='gray')
axis1.set_title("Original Image")
axis1.axis('off')
axis2.imshow(result_sharp,cmap='gray')
axis2.set_title("Sharpened Image")
axis2.axis('off')
plt.show()



