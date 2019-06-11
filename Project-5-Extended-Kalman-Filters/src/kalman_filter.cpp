#include "kalman_filter.h"
#include "math.h"

using Eigen::MatrixXd;
using Eigen::VectorXd;

/* 
 * Please note that the Eigen library does not initialize 
 *   VectorXd or MatrixXd objects with zeros upon creation.
 */

KalmanFilter::KalmanFilter() {}

KalmanFilter::~KalmanFilter() {}

void KalmanFilter::Init(VectorXd &x_in, MatrixXd &P_in, MatrixXd &F_in,
                        MatrixXd &H_in, MatrixXd &R_in, MatrixXd &Q_in) {
  x_ = x_in;
  P_ = P_in;
  F_ = F_in;
  H_ = H_in;
  R_ = R_in;
  Q_ = Q_in;
}

void KalmanFilter::Predict() {
  /**
   * TODO: predict the state
   */
  x_ = F_ * x_;
  MatrixXd Ft = F_.transpose();
  P_ = F_ * P_ * Ft + Q_;
}

void KalmanFilter::Update(const VectorXd &z) {
  /**
   * TODO: update the state by using Kalman Filter equations
   */
  VectorXd z_pred = H_ * x_;
  VectorXd y = z - z_pred;
  MatrixXd Ht = H_.transpose();
  MatrixXd S = H_ * P_ * Ht + R_;  // 2x4 * 4x4 * 4x2 + 2x2
  MatrixXd Si = S.inverse();
  MatrixXd PHt = P_ * Ht;
  MatrixXd K = PHt * Si;

  // //new estimate
  x_ = x_ + (K * y);
  long x_size = x_.size();
  MatrixXd I = MatrixXd::Identity(x_size, x_size);
  P_ = (I - K * H_) * P_;
}

MatrixXd h_fun(Eigen::VectorXd x_prime) {
  Eigen::VectorXd z_pred = Eigen::VectorXd(3);
  float px = x_prime[0];
  float py = x_prime[1];
  float vx = x_prime[2];
  float vy = x_prime[3];

  float const1 = sqrt(pow(px, 2) + pow(py, 2));

  z_pred(0) = const1;
  z_pred(1) = atan2(px, py);
  z_pred(2) = (px * vx + py * vy) / (const1);

  return z_pred;
}

void KalmanFilter::UpdateEKF(const VectorXd &z)
{
  /**
   * TODO: update the state by using Extended Kalman Filter equations
   */
  // float ro     = z[0];
  // float theta  = z[1];
  // float ro_dot = z[2];

  // y is in radial coordinates
  VectorXd z_pred = h_fun(x_);
  // VectorXd y = z - z_pred;
  // MatrixXd Ht = H_.transpose();
  // MatrixXd S = H_ * P_ * Ht + R_; // 2x4 * 4x4 * 4x2 + 2x2
  // MatrixXd Si = S.inverse();
  // MatrixXd PHt = P_ * Ht;
  // MatrixXd K = PHt * Si;

  // // //new estimate
  // x_ = x_ + (K * y);
  // long x_size = x_.size();
  // MatrixXd I = MatrixXd::Identity(x_size, x_size);
  // P_ = (I - K * H_) * P_;
}
