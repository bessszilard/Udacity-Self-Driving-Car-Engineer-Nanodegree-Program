# Camera calibration
#importing some useful packages
import glob
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import cv2

from cameraCalibration import get_undistorted_image
from combiningThresholds import abs_sobel_thresh, abs_sobel_thresh, mag_thresh, dir_threshold

sobelMin = 0
sobelMax = 255

def on_sobel_min_trackbar(val):

    magnitude = mag_thresh(image, sobel_kernel=ksize, mag_thresh=(20, 200))
    cv2.imshow(sobel_window_name, magnitude )

def on_sobel_max_trackbar(val):
    gradx = abs_sobel_thresh(image, orient='x', sobel_kernel=ksize, thresh=(val, 255))
    cv2.imshow(sobel_window_name, gradx )  

# calculated already with cameraCalibration.py
cameraMx = np.array([[1.15660712e+03, 0.00000000e+00, 6.68960302e+02],
                     [0.00000000e+00, 1.15164235e+03, 3.88057002e+02],
                     [0.00000000e+00, 0.00000000e+00, 1.00000000e+00]])
distCoeffs = np.array([(-0.23185386, -0.11832054, -0.00116561,  0.00023902,  0.15356159)])


image = mpimg.imread('test_images/test1.jpg')
dst = get_undistorted_image(image, cameraMx, distCoeffs)

ksize = 3 # Choose a larger odd number to smooth gradient measurements
# gradx = abs_sobel_thresh(image, orient='x', sobel_kernel=ksize, thresh=(30, 255))
# grady = abs_sobel_thresh(image, orient='y', sobel_kernel=ksize, thresh=(30, 255))
# mag_binary = mag_thresh(image, sobel_kernel=ksize, mag_thresh=(20, 200))
# dir_binary = dir_threshold(image, sobel_kernel=ksize, thresh=( np.radians(45), np.pi/2))

sobel_window_name = "Sobel mag"

cv2.namedWindow(sobel_window_name)

trackbarMinName = "Min tresh"
trackbarMaxNme = "Max tresh"

cv2.createTrackbar(trackbarMinName, sobel_window_name, 0, 255, on_sobel_min_trackbar)
cv2.createTrackbar(trackbarMaxNme, sobel_window_name, 0, 255, on_sobel_max_trackbar)


on_sobel_min_trackbar(0)

# f, (ax) = plt.subplots(2, 3, figsize=(24, 5))
# f.tight_layout()
# ax[0][0].imshow(image)
# ax[0][0].set_title('Original Image', fontsize=10)
# ax[0][1].imshow(gradx, cmap='gray')
# ax[0][1].set_title('Thresholded Gradient X direction', fontsize=10)
# ax[0][2].imshow(grady, cmap='gray')
# ax[0][2].set_title('Thresholded Gradient Y direction', fontsize=10)
# ax[1][0].imshow(mag_binary, cmap='gray')
# ax[1][0].set_title('Threshold magnitude', fontsize=10)
# ax[1][1].imshow(dir_binary, cmap='gray')
# ax[1][1].set_title('Directions of the Gradient', fontsize=10)

# plt.show()
cv2.waitKey(0)