# Camera calibration
#importing some useful packages
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import cv2
# %matplotlib inline

#reading in an image
# image = mpimg.imread('calibration1.jpg')
# image = cv2.imread('camera_cal/calibration1.jpg', cv2.IMREAD_COLOR)
img = mpimg.imread('camera_cal/calibration1.jpg')

#printing out some stats and plotting
# print('This image is:', type(image), 'with dimensions:', image.shape)
# cv2.imshow("Display window", image)  # if you wanted to show a single color channel image called 'gray', for example, call as plt.imshow(gray, cmap='gray')

gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
# plt.imshow(gray, cmap='gray')

nx = 9
ny = 5

objpoints = [] # 3D points in real world space
imgpoints = [] # 2D points in image plane

objp = np.zeros((ny*nx,3), np.float32)
objp[:,:2] = np.mgrid[0:nx, 0:ny].T.reshape(-1, 2)

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Find the chessboard corners
ret, corners = cv2.findChessboardCorners(gray, (nx, ny), None)

# If found, draw corners
if ret == True:
    # Draw and display the corners
    imgpoints.append(corners)
    objpoints.append(objp)
    
    cv2.drawChessboardCorners(img, (nx, ny), corners, ret)
    
ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, gray.shape[::-1], None, None)
dst = cv2.undistort(img, mtx, dist, None, mtx)

f, (ax1, ax2) = plt.subplots(1, 2, figsize=(20,10))

ax1.imshow(img)
ax1.set_title("Normal image")
ax2.imshow(dst)
ax2.set_title("Disorted image")


plt.show()




cv2.waitKey(0)
