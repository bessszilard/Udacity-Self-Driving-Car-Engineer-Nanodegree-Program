# Camera calibration
#importing some useful packages
import glob
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import cv2

from cameraCalibration import get_undistorted_image
from combiningThresholds import abs_sobel_thresh, abs_sobel_thresh, mag_thresh, dir_threshold, mag_dir_treshold

h_ch = [  3,  31] 
l_ch = [  0, 255]
s_ch = [110, 255]
# h_ch = [0, 180]
# l_ch = [0, 255]
# s_ch  = [0, 255]

def filter_and_show(image, h, l, s):
    low_th = np.array([h[0], l[0], s[0]])
    high_th = np.array([h[1], l[1], s[1]])
    res = cv2.inRange(image, low_th, high_th)
    cv2.imshow(hls_window_name, res )

def hls_h_min_ch_trackbar(val):
    global h_ch
    h_ch[0] = val
    filter_and_show(image, h_ch, l_ch, s_ch)

def hls_h_max_ch_trackbar(val):
    global h_ch
    h_ch[1] = val
    filter_and_show(image, h_ch, l_ch, s_ch)

def hls_l_min_ch_trackbar(val):
    global l_ch
    l_ch[0] = val
    filter_and_show(image, h_ch, l_ch, s_ch)

def hls_l_max_ch_trackbar(val):
    global l_ch
    l_ch[1] = val
    filter_and_show(image, h_ch, l_ch, s_ch)

def hls_s_min_ch_trackbar(val):
    global s_ch
    s_ch[0] = val
    filter_and_show(image, h_ch, l_ch, s_ch)

def hls_s_max_ch_trackbar(val):
    global s_ch
    s_ch[1] = val
    filter_and_show(image, h_ch, l_ch, s_ch)


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

image = cv2.cvtColor(image, cv2.COLOR_RGB2HLS)
# plt.imshow(image)
# plt.show()

# image = mpimg.imread('test_images/test2.jpg')
image = cv2.blur = cv2.blur(image, (5,5))

hls_window_name = "HLS filter"
cv2.namedWindow(hls_window_name, cv2.WINDOW_NORMAL)
trackbarHMinName = "H min"
trackbarHMaxName = "H max"
trackbarLMinName = "L min"
trackbarLMaxName = "L max"
trackbarsMinName = "S min"
trackbarsMaxName = "S max"

cv2.createTrackbar(trackbarHMinName, hls_window_name, 0, 180, hls_h_min_ch_trackbar)
cv2.createTrackbar(trackbarHMaxName, hls_window_name, 0, 180, hls_h_max_ch_trackbar)

cv2.createTrackbar(trackbarLMinName, hls_window_name, 0, 255, hls_l_min_ch_trackbar)
cv2.createTrackbar(trackbarLMaxName, hls_window_name, 0, 255, hls_l_max_ch_trackbar)

cv2.createTrackbar(trackbarsMinName, hls_window_name, 0, 255, hls_s_min_ch_trackbar)
cv2.createTrackbar(trackbarsMaxName, hls_window_name, 0, 255, hls_s_max_ch_trackbar)

cv2.setTrackbarPos(trackbarHMinName, hls_window_name, h_ch[0] )
cv2.setTrackbarPos(trackbarHMaxName, hls_window_name, h_ch[1] )
cv2.setTrackbarPos(trackbarLMinName, hls_window_name, l_ch[0] )
cv2.setTrackbarPos(trackbarLMaxName, hls_window_name, l_ch[1] )
cv2.setTrackbarPos(trackbarsMinName, hls_window_name, s_ch[0] )
cv2.setTrackbarPos(trackbarsMaxName, hls_window_name, s_ch[1] )


cv2.waitKey(0)