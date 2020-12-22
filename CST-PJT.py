#In this file we will demonstrate the Central Projection Theorem or Projection Slice Theorem.
#I used the following libraries:
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

#Load the image (I used a .tif file):
img = plt.imread ("img_name.tif")

#Sum the image array (in x-axis):
sum_img = np.sum (img, axis=0)

#Transform the image
ft_img = np.fft.fft2 (np.fft.fftshift (img))

#Find the central line
len_x = int (len (ft_img[:0,0])/2)

#Sum about the central lin
sum_ft_img = ft_img[len_x]

#Inverse Fourier transform the summed projection
ift_sum_img = np.fft.ifft (sum_ft_img)

#Calculate the magnitude
mag_img = np.sqrt (ift_sum_img.real ** 2 + ift_sum_img.imag ** 2)

#Display both projections, should be the same:
fig, (a1, a2) = plt.subplots(1,2)
a1.plot (sum_img)
a1.set_title("Central Line")
a2.plot ( np.fft.ifftshift( np.squeeze( mag_img)))
a2.set_title("Projection")
plt.show()
