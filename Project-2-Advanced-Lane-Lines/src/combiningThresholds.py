# source: Udacity, Lesson 8, Gradient and Color Spaces
# import pickle
import numpy as np
import cv2
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from geometries import get_perspective

def get_mean_bigger_than(matrix, limit):
    '''
    Returns the mean of the matrix elements which are bigger than the limit.
    '''
    return matrix.sum()/(limit < matrix).sum().astype(float)

def alphaBetaAuto_correction(input_image):
    '''
    Increases rescales the matrix elements to [0 255] range.
    '''
    inputRange = np.amax(input_image) - np.amin(input_image)
    wantedrange = 255.0
    alpha = wantedrange / inputRange
    beta = - alpha * np.amin(input_image)
    return (input_image * alpha + beta).astype("uint8")

def filter_white_lane(input_image):
    '''
    Filters out the white lane and returns a binary image.
    Filters the red and the green channels. Threshold is adaptive.
    get_mean_bigger_than function is used to eliminate in mean the black surfaces
    '''
    white_lane = np.copy(input_image)
    r_ch = white_lane[:, :, 0]
    r_ch = alphaBetaAuto_correction(r_ch)

    threshold = get_mean_bigger_than(r_ch, 75)
    r_ch[ r_ch * 0.8 < threshold ] = 0

    g_ch = white_lane[:, :, 1]
    g_ch = alphaBetaAuto_correction(g_ch)
    threshold =  get_mean_bigger_than(g_ch, 75)
    g_ch[ (g_ch * 0.9 < threshold) ] = 0

    white_lane[:, :, 0] = r_ch
    white_lane[:, :, 1] = g_ch
    white_lane[:, :, 2] = 0

    white_lane[white_lane > 0] = 255

    return r_ch + g_ch

def filter_yellow_lane(input_image):
    '''
    Filters out the yellow lane and returns a binary image.
    Filters the light and the saturation channels, Threshold is adaptive.
    '''
    yellow_lane = np.copy(input_image)
    hls = cv2.cvtColor(yellow_lane, cv2.COLOR_RGB2HLS)
    l_ch2 = hls[:, :, 1 ]
    s_ch2 = hls[:, :, 2 ]
    l_ch2 = alphaBetaAuto_correction(l_ch2)
    s_ch2 = alphaBetaAuto_correction(s_ch2)   
    s_ch2[ (l_ch2 < l_ch2.mean()) | ( s_ch2 < s_ch2.mean()) ] = 0
    l_ch2[ (l_ch2 < l_ch2.mean()) | ( s_ch2 < s_ch2.mean()) ] = 0

    channelAdd = s_ch2 + l_ch2
    yellowBirdsEye = get_perspective(channelAdd, 'b')

    yellowBirdsEye[yellowBirdsEye > 0] = 255
    return yellowBirdsEye

def draw_region_of_interest(input_image, top_left, top_right, bottom_left, bottom_right):
    '''
    Draws region of interest based on input arguments.
    '''
    image = np.copy(input_image)
    vertices = np.array([[bottom_left,  # left_bot
                          top_left,     # right_top
                          top_right,    # left_top
                          bottom_right]], dtype=np.int32)
    return cv2.polylines(image, vertices, True, (255, 0, 0), 5)