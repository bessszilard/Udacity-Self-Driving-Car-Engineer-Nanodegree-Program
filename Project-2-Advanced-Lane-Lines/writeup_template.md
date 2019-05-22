## Advanced Lane Finding project

The goals / steps of this project are the following:

* Compute the camera calibration matrix and distortion coefficients given a set of chessboard images.
* Apply a distortion correction to raw images.
* Use color transforms, gradients, etc., to create a thresholded binary image.
* Apply a perspective transform to rectify binary image ("birds-eye view").
* Detect lane pixels and fit to find the lane boundary.
* Determine the curvature of the lane and vehicle position with respect to center.
* Warp the detected lane boundaries back onto the original image.
* Output visual display of the lane boundaries and numerical estimation of lane curvature and vehicle position.

### Camera Calibration

#### 1. Calculating camera matrix and distortion coefficients to eliminate camera distortion. 

Camera calibration process is located in ```src/cameraCailbration.py``` file. Calibration parameters which are the **camera matrix** and **distortion coefficients** are determined with ```get_calibration_params()```  function, and generate undistorted image with ```get_undistorted_image()``` function. I read the calibration pictures with glob library. With a for loop I processed all the images. These were process steps:

1. Convert current image to grayscale
2. Find corners with ```findChessboardCorners()``` function
3. If corners were found, I appended the corners and image points to my list

This is the results.

![distored_undistored](writeup_images\distored_undistored.jpg)

*Figure 1. Chessboard corner finding results*

After the object and image points were determined, I calculated **camera matrix** and **distortion coefficients** with ```calibrateCamera()``` function, and generate the undistorted the image.

Final results:

![calibraiton results](writeup_images\calib_results.jpg)

*Figure 2. Normal and undistorted image*

### Pipeline (single images)

The image process pipeline is in 

#### 1. Generate undistorted image

To eliminate distortion, I used the  **camera matrix** and **distortion coefficients**, which are calculated with camera calibration.
![Sobel and HLS](writeup_images\distored_undistored_road.jpg)

*Figure 3: Normal and Undistorted road image*

#### 2. Get bird's eye view

Perspective correction method is located in ```src/geometries.py``` file. I generated bird's eye view with the ``get_perspective()	`` function. In the road image, I selected the four corners with the pyplot's interactive menu. 

```python
top_left = (585, 453)
top_right = (697, 453)
bottom_left = (270, 668)
bottom_right = (1060, 668) 
```

On the bird's eye view, I used 150 pixel padding on the horizontal axis. 

```python
top_left = (vert_padding, 0)
top_right = (image_size[0] - vert_padding, 0)
bottom_left = (vert_padding, image_size[1])
bottom_right = (image_size[0] - vert_padding, image_size[1])
dst = np.float32([[top_left], [top_right], [bottom_left], [bottom_right]])
```

This resulted in the following source and destination points:

|  Source   | Destination |
| :-------: | :---------: |
| 585, 453  |   150, 0    |
| 697, 453  |   570, 0    |
| 270, 668  |  150, 1280  |
| 1060, 668 |  570, 1280  |

![Bird's eye veiew](writeup_images\birds_eye2.jpg)

#### 3. Image filtering

For a first step, I blurred the image with a 5x5 kernel. Secondly, for filtering I used the combination of Sobel edge detection and HLS color filtering. I used absolute gradient magnitude and gradient direction for Sobel. I combined the 6 test image into one, and than I created a window, where I can manually adjusted the threshold limits. After the limit tuning, I add the two filters output, the results is *Figure 4* . Green color is the output of the Sobel filter and blue is for HLS filter. These functions are located ```combiningThresholds.py``` file. To reduce noise I used open morphological operator for reduce noise, and close connect remained surface.

![Sobel and HLS birds eye](writeup_images\birds_eye_filtered.jpg)

*Figure 4. Results of Sobel and HLS filtering for the combined test pictures filter*

#### 3. Describe how (and identify where in your code) you performed a perspective transform and provide an example of a transformed image.

The code for my perspective transform includes a function called `warper()`, which appears in lines 1 through 8 in the file `example.py` (output_images/examples/example.py) (or, for example, in the 3rd code cell of the IPython notebook).  The `warper()` function takes as inputs an image (`img`), as well as source (`src`) and destination (`dst`) points.  I chose the hardcode the source and destination points in the following manner:

```python
src = np.float32(
    [[(img_size[0] / 2) - 55, img_size[1] / 2 + 100],
    [((img_size[0] / 6) - 10), img_size[1]],
    [(img_size[0] * 5 / 6) + 60, img_size[1]],
    [(img_size[0] / 2 + 55), img_size[1] / 2 + 100]])
dst = np.float32(
    [[(img_size[0] / 4), 0],
    [(img_size[0] / 4), img_size[1]],
    [(img_size[0] * 3 / 4), img_size[1]],
    [(img_size[0] * 3 / 4), 0]])
```

This resulted in the following source and destination points:

| Source        | Destination   |
|:-------------:|:-------------:|
| 585, 460      | 320, 0        |
| 203, 720      | 320, 720      |
| 1127, 720     | 960, 720      |
| 695, 460      | 960, 0        |

I verified that my perspective transform was working as expected by drawing the `src` and `dst` points onto a test image and its warped counterpart to verify that the lines appear parallel in the warped image.

![alt text][image4]



#### 4. Describe how (and identify where in your code) you identified lane-line pixels and fit their positions with a polynomial?

Then I did some other stuff and fit my lane lines with a 2nd order polynomial kinda like this:

![alt text][image5]

#### 5. Describe how (and identify where in your code) you calculated the radius of curvature of the lane and the position of the vehicle with respect to center.

I did this in lines # through # in my code in `my_other_file.py`

#### 6. Provide an example image of your result plotted back down onto the road such that the lane area is identified clearly.

I implemented this step in lines # through # in my code in `yet_another_file.py` in the function `map_lane()`.  Here is an example of my result on a test image:

![alt text][image6]

---

### Pipeline (video)

#### 1. Provide a link to your final video output.  Your pipeline should perform reasonably well on the entire project video (wobbly lines are ok but no catastrophic failures that would cause the car to drive off the road!).

Here's a [link to my video result](./project_video.mp4)

---

### Discussion

#### 1. Briefly discuss any problems / issues you faced in your implementation of this project.  Where will your pipeline likely fail?  What could you do to make it more robust?

Here I'll talk about the approach I took, what techniques I used, what worked and why, where the pipeline might fail and how I might improve it if I were going to pursue this project further.  
