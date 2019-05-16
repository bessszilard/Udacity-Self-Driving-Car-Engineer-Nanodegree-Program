# Camera calibration
#importing some useful packages
import glob
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import cv2

from cameraCalibration import get_undistorted_image
from combiningThresholds import abs_sobel_thresh, abs_sobel_thresh, mag_thresh, dir_threshold, mag_dir_treshold

# 54       255     -1.4486232791552935     1.3089969389957472
sobelMagMin = 54
sobelMagMax = 255
sobelAngMin = -1.4486232791552935
sobelAngMax = 1.3089969389957472

def on_sobel_mag_min_trackbar(val):
    global sobelMagMin
    sobelMagMin = val
    res = mag_dir_treshold(image, sobel_kernel=ksize, mag_thresh=(sobelMagMin, sobelMagMax),
                                 dir_thresh = (sobelAngMin, sobelAngMax))
    cv2.imshow(sobel_window_name, res )
    print(sobelMagMin, "\t", sobelMagMax, "\t", sobelAngMin, "\t", sobelAngMax)

def on_sobel_mag_max_trackbar(val):
    global sobelMagMax
    sobelMagMax = val
    res = mag_dir_treshold(image, sobel_kernel=ksize, mag_thresh=(sobelMagMin, sobelMagMax),
                                 dir_thresh = (sobelAngMin, sobelAngMax))
    cv2.imshow(sobel_window_name, res )  
    print(sobelMagMin, "\t", sobelMagMax, "\t", sobelAngMin, "\t", sobelAngMax)

def on_sobel_ang_min_trackbar(val):
    global sobelAngMin
    sobelAngMin = np.radians(val - 90)
    res = mag_dir_treshold(image, sobel_kernel=ksize, mag_thresh=(sobelMagMin, sobelMagMax),
                                 dir_thresh=(sobelAngMin, sobelAngMax))
    cv2.imshow(sobel_window_name, res )  
    print(sobelMagMin, "\t", sobelMagMax, "\t", sobelAngMin, "\t", sobelAngMax)

def on_sobel_ang_max_trackbar(val):
    global sobelAngMax
    sobelAngMax = np.radians(val - 90)
    res = mag_dir_treshold(image, sobel_kernel=ksize, mag_thresh=(sobelMagMin, sobelMagMax),
                                 dir_thresh=(sobelAngMin, sobelAngMax))
    cv2.imshow(sobel_window_name, res )  
    print(sobelMagMin, "\t", sobelMagMax, "\t", sobelAngMin, "\t", sobelAngMax)

# calculated already with cameraCalibration.py
cameraMx = np.array([[1.15660712e+03, 0.00000000e+00, 6.68960302e+02],
                     [0.00000000e+00, 1.15164235e+03, 3.88057002e+02],
                     [0.00000000e+00, 0.00000000e+00, 1.00000000e+00]])
distCoeffs = np.array([(-0.23185386, -0.11832054, -0.00116561, 0.00023902, 0.15356159)])

images_file_names = glob.glob('test_images/test*.jpg')

rows = 2
cols = 3


disp_imgRow1 = mpimg.imread(images_file_names[0])

for i in range(1, 3): # len(images_file_names)):
    filename = images_file_names[i]
    img = mpimg.imread(filename)
    img = get_undistorted_image(img, cameraMx, distCoeffs)
    disp_imgRow1 = np.concatenate((disp_imgRow1, img), axis=1)

disp_imgRow2 = mpimg.imread(images_file_names[3])
for i in range(4, len(images_file_names)):
    filename = images_file_names[i]
    img = mpimg.imread(filename)
    img = get_undistorted_image(img, cameraMx, distCoeffs)
    disp_imgRow2 = np.concatenate((disp_imgRow2, img), axis=1)

image = np.concatenate((disp_imgRow1, disp_imgRow2), axis=0)

# plt.imshow(image)
# plt.show()

# image = mpimg.imread('test_images/test2.jpg')
image = cv2.blur = cv2.blur(image, (5,5))
# image = get_undistorted_image(image, cameraMx, distCoeffs)

ksize = 5 # Choose a larger odd number to smooth gradient measurements
# gradx = abs_sobel_thresh(image, orient='x', sobel_kernel=ksize, thresh=(30, 255))
# grady = abs_sobel_thresh(image, orient='y', sobel_kernel=ksize, thresh=(30, 255))
# mag_binary = mag_thresh(image, sobel_kernel=ksize, mag_thresh=(20, 200))
# dir_binary = dir_threshold(image, sobel_kernel=ksize, thresh=( np.radians(45), np.pi/2))

sobel_window_name = "Sobel mag"

cv2.namedWindow(sobel_window_name, cv2.WINDOW_NORMAL)

# desiredWidth = 640
# desiredheight = 480
# cv2.resizewindow(sobel_window_name, desiredWidth,desiredheight)

trackbarMagMinName = "Min mag"
trackbarMagMaxName = "Max mag"
trackbarAngMinName = "Min angle"
trackbarAngMaxName = "Max angle"

cv2.createTrackbar(trackbarMagMinName, sobel_window_name, 0, 255, on_sobel_mag_min_trackbar)
cv2.createTrackbar(trackbarMagMaxName, sobel_window_name, 0, 255, on_sobel_mag_max_trackbar)

cv2.createTrackbar(trackbarAngMinName, sobel_window_name, 0, 180, on_sobel_ang_min_trackbar)
cv2.createTrackbar(trackbarAngMaxName, sobel_window_name, 0, 180, on_sobel_ang_max_trackbar)

cv2.setTrackbarPos(trackbarMagMinName, sobel_window_name, sobelMagMin )
cv2.setTrackbarPos(trackbarMagMaxName, sobel_window_name, sobelMagMax )
cv2.setTrackbarPos(trackbarAngMinName, sobel_window_name, int(sobelAngMin * 180 / np.pi + 90) )
cv2.setTrackbarPos(trackbarAngMaxName, sobel_window_name, int(sobelAngMax * 180 / np.pi + 90) )

# on_sobel_mag_min_trackbar(0)
# on_sobel_mag_max_trackbar(255)

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