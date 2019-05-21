# Main process
#importing some useful packages
import glob
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import cv2

from moviepy.editor import VideoFileClip
from cameraCalibration   import get_undistorted_image
from combiningThresholds import filter_white_lane, filter_yellow_lane
# from adjust_filter_params import adjuct_filter_parameters
from geometries import get_perspective, draw_lanes, clear_lane_fifos

# images_file_names = glob.glob('test_images/test*.jpg')
images_file_names = glob.glob('video_images/vlcsnap-0000*.jpg')

# single_image = mpimg.imread('test_images/straight_lines1.jpg')
single_image = mpimg.imread('video_images/vlcsnap-00001.jpg')

def alphaBetaAuto_correction(img):
    inputRange = np.amax(img) - np.amin(img)
    wantedrange = 255.0
    alpha = wantedrange / inputRange
    beta = - alpha * np.amin(img)
    return (img * alpha + beta).astype("uint8")

frameCounter = 0

def process_image(input_image):
    global frameCounter

    image = np.copy(input_image)
    image = get_undistorted_image(image)
    # image = draw_region_of_interest(image)
    image = cv2.blur(image, (5,5))
    image = get_perspective(image, 'b')

    white_line_binary = filter_white_lane(image)
    yellow_line_binary = filter_yellow_lane(input_image)
    binary_warped = np.uint8( white_line_binary + yellow_line_binary )

    image, road = draw_lanes(binary_warped, input_image) 
    image = cv2.addWeighted(input_image, 1, image, 1, 0)

    image = np.concatenate((image, road), axis=1)
    frameCounter += 1

    # if frameCounter >= 120:
    #     plt.imshow(image)
    #     plt.show()

    return image

# # mutiple image
# # --------------------------------------------------------------------
# img = mpimg.imread(images_file_names[0])
# disp_imgRow1 = process_image(img)
# for i in range(1, 3): # len(images_file_names)):
#     filename = images_file_names[i]
#     img = mpimg.imread(filename)
#     img = process_image(img)
#     disp_imgRow1 = np.concatenate((disp_imgRow1, img), axis=1)

# img = mpimg.imread(images_file_names[3])
# disp_imgRow2 = process_image(img)
# for i in range(4, len(images_file_names)):
#     filename = images_file_names[i]
#     img = mpimg.imread(filename)
#     img = process_image(img)
#     disp_imgRow2 = np.concatenate((disp_imgRow2, img), axis=1)

# image = np.concatenate((disp_imgRow1, disp_imgRow2), axis=0)
# # --------------------------------------------------------------------


image = process_image(single_image)
plt.imshow(image)
plt.show()
# # single_image = draw_region_of_interest(single_image, top_left, top_right, bottom_left, bottom_right)

# # offset = 150
# # top_left = (offset, 0)
# # top_right = (1280-offset , 0)
# # bottom_left = (offset, 721)
# # bottom_right = (1280-offset, 721) 
# # image = draw_region_of_interest(image, top_left, top_right, bottom_left, bottom_right)

# plt.imshow(image)
# plt.show()
 
# adjuct_filter_parameters(image)

# f, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 20))
# ax1.set_title("Normal image")
# ax1.imshow(single_image)
# ax2.set_title("Bird's eye view")
# ax2.imshow(image)
# plt.show()
frameCounter = 0
clear_lane_fifos()

# videoName = 'project_video.mp4'
videoName = 'challenge_video.mp4'
# videoName = 'harder_challenge_video.mp4'
white_output = 'test_videos_output/' + videoName
clip1 = VideoFileClip(videoName)
white_clip = clip1.fl_image(process_image) #NOTE: this function expects color images!!
white_clip.write_videofile(white_output, audio=False)
