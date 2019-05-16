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
    sobelxyScaled = np.uint8( 255 * abs_sobelxy / np.max(abs_sobelxy) )
    
    mag_binary = np.zeros_like(sobelxyScaled)
    mag_binary[ ( mag_thresh[0] < sobelxyScaled ) & (sobelxyScaled < mag_thresh[1])] = 255
    return mag_binary

def dir_threshold(image, sobel_kernel=3, thresh=(0, np.pi/2)):
    # Calculate gradient direction
    # Apply threshold
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize = sobel_kernel)
    sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize = sobel_kernel)
    
    abs_sobelxy = np.sqrt( np.square(sobelx) + np.square(sobely) )
    graddir = np.arctan2(np.absolute(sobely), np.absolute(sobelx))
    
    dir_binary = np.zeros_like(abs_sobelxy)
    dir_binary[ (thresh[0] < graddir) & ( graddir < thresh[1] ) ] = 255
    return dir_binary

def mag_dir_treshold(image, sobel_kernel=3, mag_thresh=(0, 255), dir_thresh=(0, np.pi/2)):
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


# # image = mpimg.imread('test_images/signs_vehicles_xygrad.png')
# image = mpimg.imread('test_images/test1.jpg')
# # Choose a Sobel kernel size
# ksize = 3 # Choose a larger odd number to smooth gradient measurements
# # Apply each of the thresholding functions
# gradx = abs_sobel_thresh(image, orient='x', sobel_kernel=ksize, thresh=(20, 100))
# grady = abs_sobel_thresh(image, orient='y', sobel_kernel=ksize, thresh=(20, 100))
# mag_binary = mag_thresh(image, sobel_kernel=ksize, mag_thresh=(20, 100))
# dir_binary = dir_threshold(image, sobel_kernel=ksize, thresh=( np.radians(45), np.pi/2))

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

# plt.subplots_adjust(left=0., right=1, top=0.9, bottom=0.)

# plt.show()

# cv2.waitKey(0)