#I used the following libraries, not all are required:
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from math import ceil
import scipy.fftpack
from scipy.fft import fft, ifft
import scipy.io
from scipy.io import loadmat
from scipy import signal

#Load the noise image (I used a .tif file):
img = plt.imread ("noisy_image.tif")

#Transform the image to frequency space so we can find and eliminate the noise:
ft_img = np.fft.fft2 (img)
ft_img_magnitude = np.sqrt (ft_img.real ** 2 + ft_img.imag ** 2)

#Flatten the matrix and plot a histogram to see the noise
x = (np.abs (ft_img_magnitude)).flatten
bins = 255
plt.hist (x,bins)
plt.show()

#Noise occurred around 1000 in my image, so set threshold
threshold = 1000

#Threshold the image in frequency space:
ft_img_magnitude [ft_img_magnitude < threshold] = 1

#Transform back to image space and dispay:
filtered_img = np.fft.ifft2 (ft_img_magnitude)

fig = plt.figure()
fig.suptitle('Filtered Image')
plt.imshow(np.abs(filtered_img), cmap='gray')
plt.axis('off')
plt.show()
