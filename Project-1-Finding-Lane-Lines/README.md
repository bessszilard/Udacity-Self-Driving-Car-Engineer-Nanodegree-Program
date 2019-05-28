# 1. Pipeline description

My pipeline consisted of 8 steps. 
* Step 1: Resize image into 960 x 540.
* Step 2: Convert the colored image to grayscale.
* Step 3: Smooth with Gaussian Blur
* Step 4: Detect edges with Canny edge detection operator
* Step 5: Select Region Of Interest (ROI)
* Step 6: Find lines with Hough transform
* Step 7: Determine the left and right lane from detected the lines
* Step 8: Filter lane parameters with an average filter using FIFO memory

# 2. Potential shortcomings with this pipeline
Shortcomings are:
1. Based on average filtering, the algorithm can't follow the rapid changes of line.
2. If the light conditions are not proper, edges could not be detected.

In the last video (challenge.mp4) at light conditions changes, for some frames, the lines could not be detected with Canny + Hough transform operations. Because the lane lines didn't change a lot frame by frame, I used, in that case, the on previous frames lane results (average filtering).

# Results
* [solidWhiteRight.mp4](https://www.youtube.com/watch?v=mT-Rp0BcflU)
* [solidYellowLeft.mp4](https://www.youtube.com/watch?v=0IJy2IMVXew)
* [challange.mp4](https://www.youtube.com/watch?v=A3a8BxA1ETs)
