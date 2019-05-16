# gemoetries.py
import numpy as np
import cv2

def get_birds_eye_img(input_image):
    image = np.copy(input_image)
    image_size = (image.shape[0], image.shape[1])

    topLeft    = ( 585 , 453)
    topRight   = ( 697,  453)
    bottomLeft = (  270, 668)
    bottomRight= ( 1060, 668) 

    src = np.float32([[topLeft],[topRight],[bottomLeft],[bottomRight]])

    topLeft = (0, 0)
    topRgiht = (image_size, 0)
    bottomLeft = (0, image_size[1])
    bottomRight =(image_size[0], image_size[1])
    dst = np.float32([[topLeft],[topRight],[bottomLeft],[bottomRight]])

    M = cv2.getPerspectiveTransform(src, dst)
    warped = cv2.warpPerspective(image, M, image_size, flags=cv2.INTER_LINEAR)
    return warped