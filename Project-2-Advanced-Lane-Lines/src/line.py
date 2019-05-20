import numpy as np
# import geometries find_lane_pixels

# Define a class to receive the characteristics of each line detection
class Line():
    def __init__(self, fifo_max_len):
        # was the line detected in the last iteration?
        self.detected = False  
        # x values of the last n fits of the line
        self.recent_xfitted = [] 
        #average x values of the fitted line over the last n iterations
        self.bestx = None     
        #polynomial coefficients averaged over the last n iterations
        self.best_fit = None  
        #polynomial coefficients for the most recent fit
        self.current_fit = [np.array([False])]  
        #radius of curvature of the line in some units
        self.radius_of_curvature = None 
        #distance in meters of vehicle center from the line
        self.line_base_pos = None 
        #difference in fit coefficients between last and new fits
        self.diffs = [] # np.array([0,0,0], dtype='float') 
        #x values for detected line pixels
        self.coef_fifo = [] # np.zeros((3,1))  
        self.fifo_max_len = fifo_max_len  

    def append_x(self, poly_x, poly_y): # leftx, lefty, rightx, righty):
        self.current_fit = poly_x  
        # self.ally = poly_y
        # Fit a second order polynomial to each using `np.polyfit`
        
        if len(self.coef_fifo) > 0:
            lsq_error = np.sum( (self.recent_xfitted - self.current_fit) ** 2 )
            if lsq_error < np.sum( self.recent_xfitted ** 2 ) * 6:
                # valid result
                if len(poly_x) > 3:
                    current_fit = np.array([np.polyfit(poly_y, poly_x, 2)])
                    if len(current_fit) > 0:
                        if len(self.coef_fifo) > self.fifo_max_len:
                            np.delete(self.coef_fifo, 0, 0)
                        self.coef_fifo = np.concatenate((self.coef_fifo, current_fit), axis=0)
                        avg_coefs = self.coef_fifo.mean(0)
                        self.recent_xfitted  = avg_coefs[0]*poly_y**2 + avg_coefs[1]*poly_y + avg_coefs[2]
            else:
                print("lsq error is too big: ", lsq_error / np.sum( self.recent_xfitted ** 2 ))
        #fifo is empty
        else:
            current_fit = np.array(np.polyfit(poly_y, poly_x, 2))
            self.coef_fifo = np.array( [current_fit] )
            # self.coef_fifo.append([current_fit])
            self.recent_xfitted  = current_fit[0]*poly_y**2 + current_fit[1]*poly_y + current_fit[2]
            
        return self.recent_xfitted

    def clear_fifo(self):
        self.coef_fifo = []


    def get_coefs(self):
        return  self.coef_fifo.mean(0)
    # def get_fitted_x():
    #     return self.recently_fitted_x, self.poly_y
