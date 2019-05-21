# Camera calibration
#importing some useful packages
import glob
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import cv2

# calculated already with cameraCalibration.py
cameraMx = np.array([[1.15660712e+03, 0.00000000e+00, 6.68960302e+02],
                     [0.00000000e+00, 1.15164235e+03, 3.88057002e+02],
                     [0.00000000e+00, 0.00000000e+00, 1.00000000e+00]])
distCoeffs = np.array([(-0.23185386, -0.11832054, -0.00116561,  0.00023902,  0.15356159)])

def get_undistorted_image(img):
    """
    Based on camera matrix and distortion coefficients 
    returns an undistored picture of the input image.
    """
    return cv2.undistort(img, cameraMx, distCoeffs, None, cameraMx)

def get_calibration_params(images_file_names, nx, ny):
    """
    Calculates camera matrix and distortion coefficients.
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


def calibrate():
    single_img = mpimg.imread('camera_cal/calibration1.jpg')
    images = glob.glob('camera_cal/calibration*.jpg')
    nx = 9
    ny = 6

    mtx, distCoeffs = get_calibration_params(images, nx, ny)
    dst = get_undistorted_image(single_img, mtx, distCoeffs)

    # print(mtx, "\n", distCoeffs)

    f, (ax1, ax2) = plt.subplots(1, 2, figsize=(20, 10))

    ax1.imshow(single_img)
    ax1.set_title("Normal image")
    ax2.imshow(dst)
    ax2.set_title("Undistorted image")

    plt.show()

# cv2.waitKey(0)
