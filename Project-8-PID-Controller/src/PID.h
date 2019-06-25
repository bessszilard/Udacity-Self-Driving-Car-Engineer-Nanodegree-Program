#ifndef PID_H
#define PID_H

class PID {
 public:
  /**
   * Constructor
   */
  PID();

  /**
   * Destructor.
   */
  virtual ~PID();

  /**
   * Initialize PID.
   * @param (Kp_, Ki_, Kd_) The initial PID coefficients
   */
  void Init(double Kp_, double Ki_, double Kd_, double act[]);

  /**
   * Update the PID error variables given cross track error.
   * @param cte The current cross track error
   */
  double GetActuation(double error);

  /**
   * Calculate the total PID error.
   * @output The total PID error
   */
  double TotalError();

  double Limit_actuator(double u_t);

private:
  /**
   * PID Errors
   */
  double p_error;
  double i_error;
  double d_error;

  /**
   * PID Coefficients
   */ 
  double Kp;
  double Ki;
  double Kd;
  double actuator[2];
};

#endif  // PID_H