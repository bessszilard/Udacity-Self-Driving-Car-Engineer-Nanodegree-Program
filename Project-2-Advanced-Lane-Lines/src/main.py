# Main process
#importing some useful packages
import glob
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import cv2

from cameraCalibration   import get_undistorted_image
from combiningThresholds import sobel_mag_dir_treshold, hls_convert_and_filter, draw_region_of_interest
from adjust_filter_params import adjuct_filter_parameters, filter_and_show

# calculated already with cameraCalibration.py
cameraMx = np.array([[1.15660712e+03, 0.00000000e+00, 6.68960302e+02],
                     [0.00000000e+00, 1.15164235e+03, 3.88057002e+02],
                     [0.00000000e+00, 0.00000000e+00, 1.00000000e+00]])
distCoeffs = np.array([(-0.23185386, -0.11832054, -0.00116561,  0.00023902,  0.15356159)])

# Sobel thresholds
# 54       255     -1.4486232791552935     1.3089969389957472
sobelMag = np.array([54, 255])
sobelAngMin = np.array([-1.4486232791552935, 1.3089969389957472])

# HLS thresholds
h_ch = [  3,  31] 
l_ch = [  0, 255]
s_ch = [110, 255]

images_file_names = glob.glob('test_images/test*.jpg')

rows = 2
cols = 3

single_image = mpimg.imread('test_images/straight_lines1.jpg')

roiTopLen = 150
rioBottomLen = 910
roiOffset = 20

img = mpimg.imread(images_file_names[0])
img = get_undistorted_image(img, cameraMx, distCoeffs)
disp_imgRow1 = draw_region_of_interest(img, roiTopLen, rioBottomLen, roiOffset)

for i in range(1, 3): # len(images_file_names)):
    filename = images_file_names[i]
    img = mpimg.imread(filename)
    img = get_undistorted_image(img, cameraMx, distCoeffs)
    img = draw_region_of_interest(img, roiTopLen, rioBottomLen, roiOffset)
    disp_imgRow1 = np.concatenate((disp_imgRow1, img), axis=1)

img = mpimg.imread(images_file_names[3])
img = get_undistorted_image(img, cameraMx, distCoeffs)
disp_imgRow2 = draw_region_of_interest(img, roiTopLen, rioBottomLen, roiOffset)
for i in range(4, len(images_file_names)):
    filename = images_file_names[i]
    img = mpimg.imread(filename)
    img = get_undistorted_image(img, cameraMx, distCoeffs)
    img = draw_region_of_interest(img, roiTopLen, rioBottomLen, roiOffset)
    disp_imgRow2 = np.concatenate((disp_imgRow2, img), axis=1)

image = np.concatenate((disp_imgRow1, disp_imgRow2), axis=0)
# image = cv2.blur(image, (5,5))
ksize = 5 # Choose a larger odd number to smooth gradient measurements

# image = np.copy(single_image)

sobelRes = sobel_mag_dir_treshold(image, sobel_kernel=ksize, mag_thresh=sobelMag, dir_thresh=sobelAngMin)
hlsRes = hls_convert_and_filter(image, h_ch, l_ch, s_ch)

combinedPiture = np.zeros_like(image)
combinedPiture[:,:,0] = hlsRes
combinedPiture[:,:,1] = sobelRes
combinedPiture[:,:,2] = 0

# adjuct_filter_parameters(image)

# img = cv2.addWeighted(single_image, alpha, roi, 1 - alpha, 0, img)

# filter_and_show(single_image, h_ch, l_ch, s_ch, sobelMag, sobelAngMin )
plt.imshow(image)
# plt.imshow(hlsRes)

plt.show()
