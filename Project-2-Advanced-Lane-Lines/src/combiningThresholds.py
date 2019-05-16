# source: Udacity, Lesson 8, Gradient and Color Spaces
# import pickle
import numpy as np
import cv2
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def abs_sobel_thresh(img, orient='x', sobel_kernel=3, thresh=(0, 255)):
    # Calculate directional gradient
    # Apply threshold
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

    if orient == 'x':
        sobel = cv2.Sobel( gray, cv2.CV_64F, 1, 0, ksize = sobel_kernel )
    elif orient == 'y':
        sobel = cv2.Sobel( gray, cv2.CV_64F, 0, 1, ksize = sobel_kernel )

    abs_sobel = np.absolute(sobel)
    scaled_sobel = np.uint8( abs_sobel * 255 / np.max(abs_sobel) )

    grad_binary = np.zeros_like(img)
    grad_binary [ ( thresh[0] <= scaled_sobel ) & ( scaled_sobel <= thresh[1]) ] = 255
    
    return grad_binary

def mag_thresh(image, sobel_kernel=3, mag_thresh=(0, 255)):
    # Calculate gradient magnitude
    # Apply threshold
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize = sobel_kernel)
    sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize = sobel_kernel)
    
    abs_sobelxy = np.sqrt( np.square(sobelx) + np.square(sobely) )
    # sobelyAbs = np.absolute(sobely)
    
    sobelxyScaled = np.uint8( 255 * abs_sobelxy / np.max(abs_sobelxy) )
    # sobelyScaled = np.uint8( 255 * sobelyAbs / np.max(sobelyAbs) )
    
    mag_binary = np.zeros_like(sobelxyScaled)
    mag_binary[ ( mag_thresh[0] < sobelxyScaled ) & (sobelxyScaled < mag_thresh[1])] = 255
        
    # binary_output = np.copy(img) # Remove this line
    return mag_binary

def dir_threshold(image, sobel_kernel=3, thresh=(0, np.pi/2)):
    # Calculate gradient direction
    # Apply threshold
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize = sobel_kernel)
    sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize = sobel_kernel)
    
    abs_sobelxy = np.sqrt( np.square(sobelx) + np.square(sobely) )
    
    # gradientAngle = np.arctan2(sobelx / sobely)
    graddir = np.arctan2(np.absolute(sobely), np.absolute(sobelx))
    
    dir_binary = np.zeros_like(abs_sobelxy)
    dir_binary[ (thresh[0] < graddir) & ( graddir < thresh[1] ) ] = 1
    return dir_binary

def sobel_mag_dir_treshold(image, sobel_kernel=3, mag_thresh=(0, 255), dir_thresh=(0, np.pi/2)):
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize = sobel_kernel)
    sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize = sobel_kernel)
    
    abs_sobelxy = np.sqrt( np.square(sobelx) + np.square(sobely) )
    sobelxyScaled = np.uint8( 255 * abs_sobelxy / np.max(abs_sobelxy) )

    abs_sobelxy = np.sqrt( np.square(sobelx) + np.square(sobely) )
    graddir = np.arctan2(np.absolute(sobely), np.absolute(sobelx))
    
    res_binary = np.zeros_like(sobelxyScaled)
    res_binary[ ((mag_thresh[0] < sobelxyScaled) & (sobelxyScaled < mag_thresh[1]) & (dir_thresh[0] < graddir) & ( graddir < dir_thresh[1] )) ] = 255
    return res_binary

def hls_convert_and_filter(rgb_image, h, l, s):
    local_image = cv2.cvtColor(rgb_image, cv2.COLOR_RGB2HLS)
    low_th = np.array([h[0], l[0], s[0]])
    high_th = np.array([h[1], l[1], s[1]])
    res = cv2.inRange(local_image, low_th, high_th)
    return res

def region_of_interest(img, vertices):
    """
    Applies an image mask.
    
    Only keeps the region of the image defined by the polygon
    formed from `vertices`. The rest of the image is set to black.
    `vertices` should be a numpy array of integer points.
    """
    #defining a blank mask to start with
    mask = np.zeros_like(img)   
    
    #defining a 3 channel or 1 channel color to fill the mask with depending on the input image
    if len(img.shape) > 2:
        channel_count = img.shape[2]  # i.e. 3 or 4 depending on your image
        ignore_mask_color = (255,) * channel_count
    else:
        ignore_mask_color = 255
        
    #filling pixels inside the polygon defined by "vertices" with the fill color    
    cv2.fillPoly(mask, vertices, ignore_mask_color)
    
    #returning the image only where mask pixels are nonzero
    masked_image = cv2.bitwise_and(img, mask)
    return masked_image
    
def draw_region_of_interest(input_image, top_length, bottom_length, vert_offset):
    image = np.copy(input_image)
    img_cols = image.shape[1]
    img_rows = image.shape[0]

    roiTop = img_rows / 1.6
    roiBottom = img_rows - 50
    roiTopLen = top_length 
    roiBottomLen = bottom_length
    vertices = np.array([[(img_cols / 2 - roiBottomLen / 2 + vert_offset , roiBottom),      # left_bot
                        (img_cols / 2 - roiTopLen / 2      + vert_offset , roiTop),  # left_top
                        (img_cols / 2 + roiTopLen / 2      + vert_offset , roiTop),  # right_top
                        (img_cols / 2 + roiBottomLen / 2   + vert_offset , roiBottom)]], dtype=np.int32)
    
    return cv2.polylines(image, vertices,  True, (255,0,0), 5)