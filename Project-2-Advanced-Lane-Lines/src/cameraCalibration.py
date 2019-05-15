# Camera calibration
#importing some useful packages
import glob
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import cv2

# %matplotlib inline

#reading in an image
# image = mpimg.imread('calibration1.jpg')
# image = cv2.imread('camera_cal/calibration1.jpg', cv2.IMREAD_COLOR)

#printing out some stats and plotting
# print('This image is:', type(image), 'with dimensions:', image.shape)
# cv2.imshow("Display window", image)  # if you wanted to show a single color channel image called 'gray', for example, call as plt.imshow(gray, cmap='gray')

def get_undistorted_image(img, mtx, distCoeffs):
    """
    Based on camera matrix and distortion coefficients 
    returns an undistored picture of the input image
    """
    return cv2.undistort(img, mtx, distCoeffs, None, mtx)

def get_calibration_params(images_file_names, nx, ny):
    """
    Calculates camera matrix and distortion coefficients
    """
    objpoints = [] # 3D points in real world space
    imgpoints = [] # 2D points in image plane

    objp = np.zeros((ny*nx,3), np.float32)
    objp[:,:2] = np.mgrid[0:nx, 0:ny].T.reshape(-1, 2)

    for filename in images_file_names:
        img = mpimg.imread(filename)
        # Convert to grayscale
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Find the chessboard corners
        ret, corners = cv2.findChessboardCorners(gray, (nx, ny), None)
        
        # If found, draw corners
        if ret == True:
            # Draw and display the corners
            imgpoints.append(corners)
            objpoints.append(objp)
            img2 = np.copy(img)
            imgCor = cv2.drawChessboardCorners(img2, (nx, ny), corners, ret)

            # f, (ax1, ax2) = plt.subplots(1, 2, figsize=(20, 10))
            # ax1.imshow(img)
            # ax1.set_title("Normal image")
            # ax2.imshow(imgCor)
            # ax2.set_title("Found corners")
            # plt.show()
        # else:
        #     print(filename[len('camera_cal/calibration'):], end = " ")
    img = mpimg.imread(images_file_names[10])
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, mtx, distCoeffs, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, 
                                         gray.shape[::-1], None, None)

    return mtx, distCoeffs

single_img = mpimg.imread('camera_cal/calibration1.jpg')
images = glob.glob('camera_cal/calibration*.jpg')
nx = 9
ny = 6

mtx, distCoeffs = get_calibration_params(images, nx, ny)
dst = get_undistorted_image(single_img, mtx, distCoeffs)

f, (ax1, ax2) = plt.subplots(1, 2, figsize=(20, 10))

ax1.imshow(single_img)
ax1.set_title("Normal image")
ax2.imshow(dst)
ax2.set_title("Undistorted image")

plt.show()




# cv2.waitKey(0)
