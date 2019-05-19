# Main process
#importing some useful packages
import glob
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import cv2

from moviepy.editor import VideoFileClip
from cameraCalibration   import get_undistorted_image
from combiningThresholds import sobel_mag_dir_treshold, hls_convert_and_filter, draw_region_of_interest
from adjust_filter_params import adjuct_filter_parameters, filter_and_show
from gemoetries import get_birds_eye_img, fit_polynomial, get_car_perspective, get_path_img, draw_lanes

# calculated already with cameraCalibration.py
cameraMx = np.array([[1.15660712e+03, 0.00000000e+00, 6.68960302e+02],
                     [0.00000000e+00, 1.15164235e+03, 3.88057002e+02],
                     [0.00000000e+00, 0.00000000e+00, 1.00000000e+00]])
distCoeffs = np.array([(-0.23185386, -0.11832054, -0.00116561,  0.00023902,  0.15356159)])

# Sobel thresholds
# 54       255     -1.4486232791552935     1.3089969389957472
# sobelMag = np.array([54, 255])
# sobelAngMin = np.array([-1.4486232791552935, 1.3089969389957472])

sobelMag = np.array([19, 255])
sobelAngMin = np.array([-1.4486232791552935, 1.3089969389957472])
# [21 105]


# HLS thresholds
h_ch = [  3,  31] 
l_ch = [  0, 255]
s_ch = [110, 255]

images_file_names = glob.glob('test_images/test*.jpg')
# images_file_names = glob.glob('video_images/vlcsnap-0000*.jpg')

rows = 2
cols = 3
ksize = 5 # Choose a larger odd number to smooth gradient measurements

# single_image = mpimg.imread('test_images/straight_lines1.jpg')
# single_image = mpimg.imread('video_images/vlcsnap-00001.jpg')

def alphaBetaAuto_correction(img):
    inputRange = np.amax(img) - np.amin(img)
    wantedrange = 255.0
    alpha = wantedrange / inputRange
    beta = - alpha * np.amin(img)
    return (img * alpha + beta).astype("uint8")


def addImages (image1, image2):
    image_out = image1 + image2
    image_out [ 255 < image_out ] = 255
    return image_out

def process_image(input_image):
    image = np.copy(input_image)
    image = get_undistorted_image(image, cameraMx, distCoeffs)
    # image = draw_region_of_interest(image)
    image = get_birds_eye_img(image)
    image = cv2.blur(image, (5,5))
    sobelRes = sobel_mag_dir_treshold(image, sobel_kernel=ksize, mag_thresh=sobelMag, dir_thresh=sobelAngMin)
    hlsRes = hls_convert_and_filter(image, h_ch, l_ch, s_ch)

    openingker = np.ones((6,6),np.uint8)
    closingker = np.ones((10,10),np.uint8)
    sobelRes = cv2.morphologyEx(sobelRes, cv2.MORPH_OPEN, openingker)
    sobelRes = cv2.morphologyEx(sobelRes, cv2.MORPH_CLOSE, closingker)

    binary_warped = sobelRes + hlsRes
    # # # combinedPiture = np.zeros_like(image)
    # # # combinedPiture[:,:,0] = hlsRes
    # # # combinedPiture[:,:,1] = sobelRes
    # # # combinedPiture[:,:,2] = 0
    # # # # image = combinedPiture

    # binary_warped = np.copy(fit_polynomial(binary_warped))
    # binary_warped = np.copy(get_path_img(binary_warped))
    image = draw_lanes(binary_warped, input_image)
    image = get_car_perspective(image, input_image)

    # hls = cv2.cvtColor(image, cv2.COLOR_RGB2HLS)
    # l_ch2 = hls[:, :, 1 ]
    # s_ch2 = hls[:, :, 2 ]
    # l_ch2 = alphaBetaAuto_correction(l_ch2)
    # s_ch2 = alphaBetaAuto_correction(s_ch2)

    # l_ch2_avg = l_ch2.mean()
    # yellowLane = np.copy(image)
    # yellowLane[ (l_ch2 < l_ch2.mean()) | ( s_ch2 < s_ch2.mean()),: ] = 0
    # yellowLane[ (l_ch2 * 0.8 < l_ch2.mean()) | (s_ch2 * 3.5 < s_ch2.mean()), : ] = 0
    # yellowLane [ l_ch2 == 0, : ] = 0

    # image[ (l_ch2 < l_ch2[ int(l_ch2.shape[0] / 2), :].mean()) | ( s_ch2 * 2 < s_ch2[ int(l_ch2.shape[0] / 2), :].mean()),: ] = 0

    # image[ (l_ch2  < l_ch2.mean() + 80) ] = 0
    # lightSobel = sobel_mag_dir_treshold(l_ch2, sobel_kernel=ksize, mag_thresh=sobelMag, dir_thresh=sobelAngMin)
    # lightSobel[(l_ch2  < l_ch2.mean()) | (s_ch2 * 3 < s_ch2.mean())] = 0

    # whiteLane = np.copy(image)
    # print( l_ch2.mean() )
    # whiteLane[ lightSobel == 0, : ] = 0

    # image = yellowLane #addImages(l_ch2, s_ch2) # np.uint8( l_ch2 + s_ch2 )#  yellowLane ) # + whiteLane )

    # l_ch2[ ( l_ch2 < l_ch2.mean()) ] = 0
    
    # image = l_ch2
    image = cv2.addWeighted(input_image, 1, image, 1, 0)

    # combinedPiture = binary_warped
    # image = combinedPiture

    # reziedImg = cv2.resize(input_image,(image.shape[0],input_image.shape[1]))
    # image = np.concatenate((input_image, image), axis=0)
    # resizedImg = cv2.resize(combinedPiture,(image.shape[1], input_image.shape[0]))
    # image = np.concatenate((combinedPiture, reziedImg), axis=1)

    return image

# roiTopLen = 150
# rioBottomLen = 910
# roiOffset = 20

roiTopLen = 130
rioBottomLen = 800
roiOffset = 7

img = mpimg.imread(images_file_names[0])
disp_imgRow1 = process_image(img)

# mutiple image
# --------------------------------------------------------------------
for i in range(1, 3): # len(images_file_names)):
    filename = images_file_names[i]
    img = mpimg.imread(filename)
    img = process_image(img)
    disp_imgRow1 = np.concatenate((disp_imgRow1, img), axis=1)

img = mpimg.imread(images_file_names[3])
disp_imgRow2 = process_image(img)
for i in range(4, len(images_file_names)):
    filename = images_file_names[i]
    img = mpimg.imread(filename)
    img = process_image(img)
    disp_imgRow2 = np.concatenate((disp_imgRow2, img), axis=1)

image = np.concatenate((disp_imgRow1, disp_imgRow2), axis=0)
# --------------------------------------------------------------------

# # image = cv2.blur(image, (5,5))

# # image = np.copy(single_image)

# sobelRes = sobel_mag_dir_treshold(image, sobel_kernel=ksize, mag_thresh=sobelMag, dir_thresh=sobelAngMin)
# hlsRes = hls_convert_and_filter(image, h_ch, l_ch, s_ch)

# combinedPiture = np.zeros_like(image)
# combinedPiture[:,:,0] = hlsRes
# combinedPiture[:,:,1] = sobelRes
# combinedPiture[:,:,2] = 0

# plt.imshow(image)
# plt.show()
# image = process_image(single_image)
plt.imshow(image)
plt.show()
 
# adjuct_filter_parameters(image)

# f, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 20))
# ax1.set_title("Normal image")
# ax1.imshow(single_image)
# ax2.set_title("Bird's eye view")
# ax2.imshow(image)
# plt.show()

# videoName = 'project_video.mp4'
# # videoName = 'challenge_video.mp4'
# # videoName = 'harder_challenge_video.mp4'
# white_output = 'test_videos_output/' + videoName
# clip1 = VideoFileClip(videoName)
# white_clip = clip1.fl_image(process_image) #NOTE: this function expects color images!!
# white_clip.write_videofile(white_output, audio=False)
