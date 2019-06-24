#include "PID.h"

/**
 * TODO: Complete the PID class. You may add any additional desired functions.
 */

PID::PID() {}

PID::~PID() {}

void PID::Init(double Kp_, double Ki_, double Kd_) {
  /**
   * TODO: Initialize PID coefficients (and errors, if needed)
   */
  Kp = Kp_;
  Ki = Ki_;
  Kd = Kd_;
}

double PID::GetActuation(double error) {
  /**
   * TODO: Update PID errors based on cte.
   */
  static double error_i = 0;
  static double error_prev = 0;
  double error_d = error_prev - error;
  error_i += error;
  error_prev = error;

  double u_t = Kp * error + Ki * error_i + Kd * error_d;

  // saturation
  if (1.0f < u_t) u_t = 1;
  else if(u_t < -1.0f) u_t = -1;

  return -u_t;
}

double PID::TotalError() {
  /**
   * TODO: Calculate and return the total error
   */
  return 0.0;  // TODO: Add your total error calc here!
}