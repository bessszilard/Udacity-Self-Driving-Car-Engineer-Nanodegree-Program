import numpy as np

class Line():
    '''
    This class stands for to filter fitted values of the image.
    The class uses average filtering, to reduce noise in fitted values.
    '''
    def __init__(self, fifo_max_len=5):
        # x values of the last n fits of the line
        self.recent_xfitted = [] 
        #polynomial coefficients for the most recent fit
        self.current_fit = []  
        #distance in meters of vehicle center from the line
        self.coef_fifo = []
        #maximal FIFO length for average filtering
        self.fifo_max_len = fifo_max_len
        #maximal least square error - determined empirically
        self.max_lsq_error = 3000000

    def append(self, poly_x, poly_y):
        '''
        Append a new fit, and return a filtered value.
        If the new fit differs too much, it will not be taking in account.
        '''
        self.current_fit = poly_x
        # self.ally = poly_y
        # Fit a second order polynomial to each using `np.polyfit`
        if len(self.coef_fifo) > 0:
            lsq_error = np.sum((self.recent_xfitted - poly_x) ** 2)
            if lsq_error < self.max_lsq_error:
                # valid result
                if len(poly_x) > 3:
                    self.current_fit = np.array([np.polyfit(poly_y, poly_x, 2)])
                    # print(int(lsq_error))
                    if len(self.current_fit) > 0:
                        if len(self.coef_fifo) >= self.fifo_max_len:
                            self.coef_fifo = np.delete(self.coef_fifo, (0), axis=0)
                            # np.delete(self.coef_fifo, 0)
                        self.coef_fifo = np.concatenate((self.coef_fifo, self.current_fit), axis=0)
                        avg_coefs = self.coef_fifo.mean(0)
                        self.recent_xfitted = avg_coefs[0] * poly_y ** 2 + avg_coefs[1] * poly_y + avg_coefs[2]
            else:
                print("lsq error is too big: ", lsq_error) # / np.sum( self.recent_xfitted ** 2 ))
        #fifo is empty
        else:
            current_fit = np.array(np.polyfit(poly_y, poly_x, 2))
            self.coef_fifo = np.array([current_fit])
            self.recent_xfitted = current_fit[0] * poly_y ** 2 + current_fit[1] * poly_y + current_fit[2]
        return self.recent_xfitted

    def clear_fifo(self):
        '''
        Clears coefficient FIFO memory.
        '''
        self.coef_fifo = []

    def get_coefs(self):
        '''
        Returns the current coefficient. If coefficient vector is empty, we return 0.
        '''
        if len(self.coef_fifo) == 0:
            return [0]
        return  self.coef_fifo.mean(0)

    def get_recent_xfitted(self):
        '''
        Returns the current x coordinates of the fitted polynomial.
        '''
        return self.recent_xfitted