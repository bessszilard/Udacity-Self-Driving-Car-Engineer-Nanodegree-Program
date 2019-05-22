# gemoetries.py
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import cv2
from line import Line

left_lane = Line(5)
right_lane = Line(5)

def clear_lane_fifos():
    left_lane.clear_fifo()
    right_lane.clear_fifo()

def get_perspective(input_image, perspective = 'b'):
    '''
    Transform input image in to bird's eye view. Pixels calculated with plt.show 
    interactive window coordinates.
    Perspective
        'b' - Bird's eye view
        'n' - normal view
 
    '''
    image = np.copy(input_image)
    # image_size = (image.shape[0], image.shape[1])
    image_size = (image.shape[1], image.shape[0])
    top_left = (585, 453)
    top_right = (697, 453)
    bottom_left = (270, 668)
    bottom_right = (1060, 668) 

    src = np.float32([[top_left], [top_right], [bottom_left], [bottom_right]])
    vert_padding = 150

    top_left = (vert_padding, 0)
    top_right = (image_size[0] - vert_padding, 0)
    bottom_left = (vert_padding, image_size[1])
    bottom_right = (image_size[0] - vert_padding, image_size[1])
    dst = np.float32([[top_left], [top_right], [bottom_left], [bottom_right]])
    
    # bird's eye view
    if perspective == 'b':
        M = cv2.getPerspectiveTransform(src, dst)
    elif perspective == 'n':
        M = cv2.getPerspectiveTransform(dst, src)
    else:
        raise TypeError(" 'b' or 'n' values are valid perspectives") 

    warped = cv2.warpPerspective(image, M, image_size, flags=cv2.INTER_LINEAR)
    return warped

def find_lane_pixels(binary_warped):
    '''
    Returns the left and the right second degree polynomial. 
    '''
    # Take a histogram of the bottom half of the image
    histogram = np.sum(binary_warped[binary_warped.shape[0]//2:,:], axis=0)
    # Create an output image to draw on and visualize the result
    out_img = np.dstack((binary_warped, binary_warped, binary_warped))
    # Find the peak of the left and right halves of the histogram
    # These will be the starting point for the left and right lines
    midpoint = np.int(histogram.shape[0]//2)
    leftx_base = np.argmax(histogram[:midpoint])
    rightx_base = np.argmax(histogram[midpoint:]) + midpoint

    # HYPERPARAMETERS
    # Choose the number of sliding windows
    nwindows = 9
    # Set the width of the windows +/- margin
    margin = 200
    # Set minimum number of pixels found to recenter window
    minpix = 50

    # Set height of windows - based on nwindows above and image shape
    window_height = np.int(binary_warped.shape[0]//nwindows)
    # Identify the x and y positions of all nonzero pixels in the image
    nonzero = binary_warped.nonzero()
    nonzeroy = np.array(nonzero[0])
    nonzerox = np.array(nonzero[1])
    # Current positions to be updated later for each window in nwindows
    leftx_current = leftx_base
    rightx_current = rightx_base

    # Create empty lists to receive left and right lane pixel indices
    left_lane_inds = []
    right_lane_inds = []

    # Step through the windows one by one
    for window in range(nwindows):
        # Identify window boundaries in x and y (and right and left)
        win_y_low = binary_warped.shape[0] - (window+1)*window_height
        win_y_high = binary_warped.shape[0] - window*window_height
        
        win_xleft_low =  leftx_current   - int(margin / 2 )  # Update this
        win_xleft_high = leftx_current   + int(margin / 2 )  # Update this
        win_xright_low = rightx_current  - int(margin / 2 )  # Update this
        win_xright_high = rightx_current + int(margin / 2 )  # Update this
        
        # Draw the windows on the visualization image
        cv2.rectangle(out_img,(win_xleft_low,win_y_low),
        (win_xleft_high,win_y_high),(0,255,0), 2) 
        cv2.rectangle(out_img,(win_xright_low,win_y_low),
        (win_xright_high,win_y_high),(0,255,0), 2) 
        
        good_left_inds =  ((win_xleft_low <= nonzerox) & (nonzerox < win_xleft_high) & 
                           (win_y_low <= nonzeroy)     & (nonzeroy < win_y_high)).nonzero()[0]
        good_right_inds = ((win_xright_low <= nonzerox) & (nonzerox < win_xright_high) & 
                            (win_y_low <= nonzeroy)     & (nonzeroy < win_y_high)).nonzero()[0] 
        
        # Append these indices to the lists
        left_lane_inds.append(good_left_inds)
        right_lane_inds.append(good_right_inds)
        
        if len(good_left_inds) > minpix:
            leftx_current = np.int(np.mean(nonzerox[good_left_inds]))
        if len(good_right_inds) > minpix:
            rightx_current = np.int(np.mean(nonzerox[good_right_inds]))
        # leftx_current = np.argmax(histogram)

    # Concatenate the arrays of indices (previously was a list of lists of pixels)
    try:
        left_lane_inds = np.concatenate(left_lane_inds)
        right_lane_inds = np.concatenate(right_lane_inds)
    except ValueError:
        # Avoids an error if the above is not implemented fully
        pass

    # Extract left and right line pixel positions
    leftx = nonzerox[left_lane_inds]
    lefty = nonzeroy[left_lane_inds] 
    rightx = nonzerox[right_lane_inds]
    righty = nonzeroy[right_lane_inds]

    return leftx, lefty, rightx, righty, out_img
    
def fit_poly(img_shape, leftx, lefty, rightx, righty):
    '''
    Fits the found polynomial to the picture dimensions.
    '''
    left_fit = np.polyfit(lefty, leftx, 2)
    right_fit = np.polyfit(righty, rightx, 2)
    # Generate x and y values for plotting
    ploty = np.linspace(0, img_shape[0]-1, img_shape[0])
    ### Calc both polynomials using ploty, left_fit and right_fit ###
    left_fitx = left_fit[0] * ploty ** 2 + left_fit[1] * ploty + left_fit[2]
    right_fitx = right_fit[0] * ploty ** 2 + left_fit[1] * ploty + right_fit[2]
    
    return left_fitx, right_fitx, ploty

def search_around_poly(binary_warped, left_fit, right_fit):
    '''
    Tries to determine next polynomial's pixels based on previous frame result.
    '''
    # HYPERPARAMETER
    # Choose the width of the margin around the previous polynomial to search
    margin = 100
    minpix = 20

    # if the polynomials are empty
    if len(left_fit) < 3 or len(right_fit) < 3:
        return find_lane_pixels(binary_warped)

    # Grab activated pixels
    nonzero = binary_warped.nonzero()
    nonzeroy = np.array(nonzero[0])
    nonzerox = np.array(nonzero[1])
    
    ### Sets the area of search based on activated x-values ###
    ### within the +/- margin of our polynomial function ###
    left_lane_inds = ((left_fit[0] * nonzeroy ** 2 + left_fit[1] * nonzeroy + left_fit[2]
                    - margin <= nonzerox) & (nonzerox <
                    left_fit[0] * nonzeroy ** 2 + left_fit[1] * nonzeroy + left_fit[2]
                    + margin))
    right_lane_inds = ((right_fit[0] * nonzeroy ** 2 + right_fit[1] * nonzeroy + right_fit[2]
                    - margin <= nonzerox) & (nonzerox <
                    right_fit[0] * nonzeroy ** 2 + right_fit[1] * nonzeroy + right_fit[2]
                    + margin))
    
    # Again, extract left and right line pixel positions
    leftx = nonzerox[left_lane_inds]
    lefty = nonzeroy[left_lane_inds] 
    rightx = nonzerox[right_lane_inds]
    righty = nonzeroy[right_lane_inds]

    if len(leftx) < minpix or len(rightx) < minpix:
        return find_lane_pixels(binary_warped)
    out_img = np.dstack((binary_warped, binary_warped, binary_warped)) * 255

    return leftx, lefty, rightx, righty, out_img

def get_poly_pixels_form_coefs(leftx, lefty, rightx, righty, binary_warped, out_img):
    '''
    Fits the found polynomial to the picture if the polynomial is found.
    After fitting, it plots in the picture.
    '''
    # Generate x and y values for plotting
    ploty = np.linspace(0, binary_warped.shape[0]-1, binary_warped.shape[0] )
    left_fit = right_fit = left_fitx = right_fitx = [0]

    if len(leftx) > 0:
        # Fit a second order polynomial to each using `np.polyfit`
        left_fit = np.polyfit(lefty, leftx, 2)
        
        try:
            left_fitx = left_fit[0]*ploty**2 + left_fit[1]*ploty + left_fit[2]
        except TypeError:
            # Avoids an error if `left` and `right_fit` are still none or incorrect
            print('The function failed to fit a line!')
            left_fitx = 1*ploty**2 + 1*ploty
        out_img[lefty, leftx] = [255, 0, 0]
        left_line = np.array([np.transpose(np.vstack([left_fitx, ploty]))])
        cv2.polylines(out_img, np.int32([left_line]), False, (255, 255, 0), 10 )

    if len(rightx) > 0:
        # Fit a second order polynomial to each using `np.polyfit`
        right_fit = np.polyfit(righty, rightx, 2)
        try:
            right_fitx = right_fit[0]*ploty**2 + right_fit[1]*ploty + right_fit[2]
        except TypeError:
            # Avoids an error if `left` and `right_fit` are still none or incorrect
            print('The function failed to fit a line!')
            right_fitx = 1*ploty**2 + 1*ploty
        out_img[righty, rightx] = [0, 0, 255]
        right_line = np.array([np.transpose(np.vstack([right_fitx, ploty]))])
        cv2.polylines(out_img, np.int32([right_line]), False, (255, 0, 255), 10 )
    ## Visualization ##
    return left_fitx, right_fitx, ploty, out_img

def get_radious_from_poly(a, b, y):
    '''
    Returns the radius of the approximated circle.
    '''
    return (1 + (2 * a * y + b) ** 2) ** (3 / 2) / (2 * a)

def measure_curvature_real(__left_lane, __right_lane, ploty):
    '''
    Calculates the curvature of polynomial functions in meters.
    '''
    # Define conversions in x and y from pixels space to meters
    # ym_per_pix = 30 / 720 # meters per pixel in y dimension
    xm_per_pix = 3.7 / 709 # meters per pixel in x dimension

    # # Define y-value where we want radius of curvature
    # # We'll choose the maximum y-value, corresponding to the bottom of the image
    y_eval = np.max(ploty)

    # left_coefs =  np.polyfit(ploty * ym_per_pix, __left_lane.get_recent_xfitted() * xm_per_pix, 2)
    # right_coefs =  np.polyfit(ploty * ym_per_pix, __right_lane.get_recent_xfitted() * xm_per_pix, 2)
    # # left_coefs = np.multiply(__left_lane.get_coefs(), [  1, 1, 1])
    # # right_coefs = np.multiply(__right_lane.get_coefs(), [1, 1, 1])

    left_curverad = __left_lane.get_radius_in_meter() # get_radious_from_poly(left_coefs[0], left_coefs[1], y_eval)
    right_curverad = __right_lane.get_radius_in_meter() # get_radious_from_poly(right_coefs[0], right_coefs[1], y_eval)
    bottom_left_x = __left_lane.get_recent_xfitted()[int(y_eval)]
    bottom_right_x = __right_lane.get_recent_xfitted()[int(y_eval)]

    center = (bottom_left_x + bottom_right_x) / 2

    offset = (1280//2 - center) / 2 * xm_per_pix * 100
    return left_curverad, right_curverad, offset

def draw_poly_pixels_blank_img(left_fitx, right_fitx, ploty, input_image):
    '''
    Creates an input_image sized blank image, and draws a the results of the polynomials.  
    '''
    out_img = np.zeros((input_image.shape[0], input_image.shape[1], 3), dtype=np.uint8)
    left_line = np.array([np.transpose(np.vstack([left_fitx, ploty]))])
    right_line = np.array([np.transpose(np.vstack([right_fitx, ploty]))])

    right_line_flipped = np.array([np.flipud(np.transpose(np.vstack([right_fitx, ploty])))])
    fil_poly_line_pts = np.hstack((left_line, right_line_flipped))

    cv2.fillPoly(out_img, np.int_([fil_poly_line_pts]), (0, 255, 0))
    cv2.polylines(out_img, np.int32([left_line]), False, (255, 0, 0), 20 )
    cv2.polylines(out_img, np.int32([right_line]), False, (255, 128, 0), 20 )
    return out_img

def write_radius_and_offset(__left_lane, __right_lane, ploty, out_img):
    '''
    Calculates and writes the culviture's radious on the given image
    '''
    left_curverad, right_curverad, offset = measure_curvature_real(__left_lane, __right_lane, ploty)
    curve = (np.abs(left_curverad) + np.abs(right_curverad)) / 2
    image_text = "curve %5.1f m | offset %4.1f cm" % (curve, offset)
    cv2.putText(out_img, image_text, (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 0), 5, cv2.LINE_AA)
    return out_img

def draw_lanes(binary_warped, input_image):
    '''
    Handles the main drawing process.
    '''
    # Find our lane pixels first
    leftx, lefty, rightx, righty, out_img = find_lane_pixels(binary_warped)
    leftx, lefty, rightx, righty, out_img = search_around_poly(binary_warped, left_lane.get_coefs(), right_lane.get_coefs())

    left_fitx, right_fitx, ploty, out_img = get_poly_pixels_form_coefs(leftx, lefty, rightx, righty, binary_warped, out_img)
    left_fitx = left_lane.append(left_fitx, ploty)
    right_fitx = right_lane.append(right_fitx, ploty)

    left_line = np.array([np.transpose(np.vstack([left_fitx, ploty]))])
    cv2.polylines(out_img, np.int32([left_line]), False, (255, 127, 127), 2 )

    right_line = np.array([np.transpose(np.vstack([right_fitx, ploty]))])
    cv2.polylines(out_img, np.int32([right_line]), False, (127, 255, 127), 2 )

    video_frame = draw_poly_pixels_blank_img(left_fitx, right_fitx, ploty, input_image)
    video_frame = get_perspective(video_frame, 'n')
    write_radius_and_offset(left_lane, right_lane, ploty, video_frame)
    return video_frame, out_img
