#include <iostream>
#include <iomanip>
#include "PID.h"

using std::cout;
using std::endl;
/**
 * TODO: Complete the PID class. You may add any additional desired functions.
 */

PID::PID() {}

PID::~PID() {}

void PID::Init(double Kp_, double Ki_, double Kd_, double act[]) {
  /**
   * TODO: Initialize PID coefficients (and errors, if needed)
   */
  Kp = Kp_;
  Ki = Ki_;
  Kd = Kd_;
  actuator[0] = act[0];
  actuator[1] = act[1];
}

double PID::Limit_actuator(double u_t) {
  if (u_t < actuator[0])
    u_t = -actuator[0];
  if (actuator[1] < u_t)
    u_t = actuator[1];
  return u_t;
}

double PID::GetActuation(double error) {
  /**
   * TODO: Update PID errors based on cte.
   */
  static double error_i = 0;
  static double error_prev = 0;
  double error_d = error - error_prev;
  error_i += error;
  error_prev = error;
  
  double u_t = Kp * error + Ki * error_i + Kd * error_d;

  std::cout << std::fixed << std::setprecision(5);
  cout << "P: "<< Kp * error / u_t << "\tD: " << Kd * error_d / u_t << "\t";

  u_t = Limit_actuator(u_t);
  return u_t;
}

double PID::TotalError() {
  /**
   * TODO: Calculate and return the total error
   */
  return 0.0;  // TODO: Add your total error calc here!
}