#In this program, we will take a distorted and noisy image and demonstrate image processing techniques.

#I used these libraries, not all are required. 
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from math import ceil
import scipy.fftpack
from scipy.fft import fft, ifft
import scipy.io
from scipy.io import loadmat
from scipy import signal

#Read the image (.tif file).
img = plt.imread ('img_name.tif') 

#Display the image 
original_fig = plt.figure()
original_fig.suptitle ("Original Image")
plt.imshow (img, cmap = 'gray')   #cmap = 'gray' produces a gray scale image.
plt.axis('off')
plt.show()

#For noise, a Gaussian blur can be used to blur and smooth out the image.
#Method is as follows:
#1. Find the size of the original image as convolution of matrices must be of the same size.
x_size, y_size = img.shape

#2. Create a meshgrid of the same size as out original image. This will form our Gaussian kernel. 
x, y = np.meshgrid (np.linspace (0, x_size, x_size), np.linspace (0, y_size, y_size))

#3. Calculate the Gaussian components and form the kernel:
d = np.sqrt (x**2, y**2)
sigma, mu = 3, 0  #Set based on desired results.
Gauss_kernel = np.exp (-((d-mu)**2 / (2.0 * sigma**2)))

#To smooth the original image, we must convolve the image and kernel.
#We must transform both and mulitply (this is a convolution).
ft_Gauss = np.fft.fft2 (np.fft.fftshift (Gauss_kernel)) #Shift the high frequencies to the centre.
ft_img = np.fft.fft2 (np.fft.fftshift (img)) 
ft_result = ft_img * ft_Gauss

#To see the newimage we must return the result back to image space.
result = np.abs (np.fft.ifft2 (ft_result)) #Can only handle the absolute frequencies.

#Display both original and result:
smooth_fig, (ax1, ax2) = plt.subplots(1,2)
ax1.imshow(img,cmap='gray')
ax1.set_title("Original Image")
ax1.axis('off')
ax2.imshow(result,cmap='gray')
ax2.set_title("Smooth Image")
ax2.axis('off')
plt.show()

