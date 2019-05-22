## Advanced Lane Finding project

![cover](writeup_images\cover.jpg)

The goals / steps of this project are the following:

* Compute the camera calibration matrix and distortion coefficients given a set of chessboard images.
* Apply a distortion correction to raw images.
* Use color transforms, gradients, etc., to create a thresholded binary image.
* Apply a perspective transform to rectify binary image ("birds-eye view").
* Detect lane pixels and fit to find the lane boundary.
* Determine the curvature of the lane and vehicle position with respect to center.
* Warp the detected lane boundaries back onto the original image.
* Output visual display of the lane boundaries and numerical estimation of lane curvature and vehicle position.

[//]: #	"Image References"
[image1]: ./examples/undistort_output.png	"Undistorted"
[image2]: ./test_images/test1.jpg	"Road Transformed"
[image3]: ./examples/binary_combo_example.jpg	"Binary Example"
[image4]: ./examples/warped_straight_lines.jpg	"Warp Example"
[image5]: ./examples/color_fit_lines.jpg	"Fit Visual"
[image6]: ./examples/example_output.jpg	"Output"
[video1]: ./project_video.mp4	"Video"



| Folder name        | Comment                                |
| ------------------ | -------------------------------------- |
| camera_cal         | Images for the camera calibration      |
| examples           | This folder is given by Udacity        |
| src                | Here is the source code                |
| test_images        | Images, which I used for testing       |
| test_videos_output | Processed videos                       |
| video_images       | Snapshots from the video               |
| writeup_images     | Images that are used for this document |

### Camera Calibration

#### 1. Calculating camera matrix and distortion coefficients to eliminate camera distortion. 

Camera calibration process is located in ```cameraCailbration.py``` file. Calibration parameters which are the **camera matrix** and **distortion coefficients** are determined with ```get_calibration_params()```  function, and generate undistorted image with ```get_undistorted_image()``` function. I read the calibration pictures with glob library. With a for loop I processed all the images. These were process steps:

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

The image process pipeline is in implemented in ```processed_image()``` function, which is located in ```main.py``` source file.

#### 1. Generate undistorted image

To eliminate distortion, I used the  **camera matrix** and **distortion coefficients**, which are calculated with camera calibration.
![Sobel and HLS](writeup_images\distored_undistored_road.jpg)

*Figure 3: Normal and Undistorted road image*

#### 2. Get bird's eye view

Perspective correction method is located in ```geometries.py``` file. I generated bird's eye view with the ``get_perspective()	`` function. In the road image, I selected the four corners with the pyplot's interactive menu. 

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

For the first step, I blurred the undistorted image with a 5x5 kernel. 

For a first attempt, I filtered the image with the combination of Sobel edge detection and HLS color filtering. I used absolute gradient magnitude and gradient direction for Sobel. I combined the 6 test image into one, and than I created a window, where I can manually adjusted the threshold limits. After the limit tuning, I add the two filters output, the results is *Figure 4* . Green color is the output of the Sobel filter and blue is for HLS filter. These functions are located ```adjust_filter_params.py``` file. To reduce noise I used open morphological operator for reduce noise, and close connect remained surface.

![Sobel and HLS birds eye](writeup_images\birds_eye_filtered.jpg)

*Figure 4. Results of Sobel and HLS filtering for the combined test pictures filter*

These methodes only worked on project video. For a more robust solution, I used adaptive color thresholds, which are located in ```combiningThresholds.py```. 

##### 3.1. Yellow lane detection

The yellow lane detection is implemented in ```filter_yellow_lane()``` function.  Firstly, I converted the image into HLS color space, and then I applied and alpha beta correction to be sure, that the channel range ([0, 255]) is fully used, Than I removed the pixels, which has low light and  saturation, and sum the result, with this code:

```
s_ch2[(l_ch2 < l_ch2.mean()) | (s_ch2 < s_ch2.mean())] = 0
l_ch2[(l_ch2 < l_ch2.mean()) | (s_ch2 < s_ch2.mean())] = 0

ch_add = s_ch2 + l_ch2
```

##### 3.2. White lane detection

The white lane detection is implemented in ```filter_white_lane()``` function. I used the R and the G channel to the RGB color space to detect the white color.  To eliminate that dark surface disturb, in this case, I used ```get_mean_bigger_than()``` function to calculate the mean. The function calculates the mean of the numbers, which are bigger than the given limit.

```
white_lane = np.copy(input_image)
r_ch = white_lane[:, :, 0]
r_ch = alpha_beta_auto_correction(r_ch)
threshold = get_mean_bigger_than(r_ch, 75)
r_ch[r_ch * 0.8 < threshold] = 0

g_ch = white_lane[:, :, 1]
g_ch = alpha_beta_auto_correction(g_ch)
threshold = get_mean_bigger_than(g_ch, 75)
g_ch[(g_ch * 0.9 < threshold)] = 0

white_lane[:, :, 0] = r_ch
white_lane[:, :, 1] = g_ch
white_lane[:, :, 2] = 0
```

**Filter result:**

# ![yellow white lanes](writeup_images\yellow_white_lane.jpg)

*Figure 5. Results of yellow and white lane filters. Green is the* ```filter_yellow_lane()``` *results, red is the* ```filter_white_lane()```

#### 4. Identifying lane-line pixels and fit their positions with a polynomial

The polynomial fitting and position handled in ```draw_lanes()``` function, which is located in ```geometries.py ```

file.  Main steps are:

* **Detect pixels which belongs to the two curve**. This step is implemented in ```search_around_poly()``` function. This method is uses the curves which were found in the previous frame. For the hyperparameters I used ```margin = 100``` and ```minpinx = 20```. If the previous curves doesn't exist or the search was unsuccessful, it returns the ```find_lane_pixels()``` function results. The ```find_lane_pixels()``` uses histograms with windows to find pixels, which belongs to the polynomials.
* **Polynomial fitting to found pixels.** 

![yellow white lanes](writeup_images\polynomial_subtitle.jpg)

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
