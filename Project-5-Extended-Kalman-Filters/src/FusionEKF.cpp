#include "FusionEKF.h"
#include <iostream>
#include "Eigen/Dense"
#include "tools.h"

using Eigen::MatrixXd;
using Eigen::VectorXd;
using std::cout;
using std::endl;
using std::vector;

/**
 * Constructor.
 */
FusionEKF::FusionEKF() {
  is_initialized_ = false;

  previous_timestamp_ = 0;

  // initializing matrices
  R_laser_ = MatrixXd(2, 2);
  R_radar_ = MatrixXd(3, 3);
  H_laser_ = MatrixXd(2, 4);
  Hj_ = MatrixXd(3, 4);

  //measurement covariance matrix - laser
  R_laser_ << 0.0225, 0,
              0, 0.0225;

  //measurement covariance matrix - radar
  R_radar_ << 0.09, 0, 0,
              0, 0.0009, 0,
              0, 0, 0.09;

  // measurement matrix
  H_laser_ << 1, 0, 0, 0,
              0, 1, 0, 0;


  // allopcate memory
  VectorXd x_in = VectorXd(4);
  MatrixXd P_in = MatrixXd(4, 4);
  MatrixXd F_in = MatrixXd(4, 4);
  MatrixXd Q_in = MatrixXd(4, 4);

  F_in << 1, 0, 1, 0,
      0, 1, 0, 1,
      0, 0, 1, 0,
      0, 0, 0, 1;

  ekf_.Init(x_in, P_in, F_in, H_laser_, R_laser_, Q_in);
}

/**
 * Destructor.
 */
FusionEKF::~FusionEKF() {}

void FusionEKF::ProcessMeasurement(const MeasurementPackage &measurement_pack) {
  /**
   * Initialization
   */

  // states x = [p_x, p_y, v_x, v_y]

  if (!is_initialized_) {
    /**
     * Initializing the state ekf_.x_ with the first measurement.
     * Creating the covariance matrix.
     * At radar converint from polar to cartesian coordinates.
     */
    
    // first measurement
    cout << "EKF: " << endl;
    ekf_.x_ = VectorXd(4);
    ekf_.x_ << 1, 1, 1, 0;

    if (measurement_pack.sensor_type_ == MeasurementPackage::RADAR) {
      // Converting radar from polar to cartesian coordinates 
      //  and initializing the state.
      float ro     = measurement_pack.raw_measurements_[0];
      float theta  = measurement_pack.raw_measurements_[1];
      ekf_.x_[0] = ro * cos(theta); // px
      ekf_.x_[1] = ro * sin(theta); // py
    }
    else if (measurement_pack.sensor_type_ == MeasurementPackage::LASER) {
      // Initializing the state.
      ekf_.x_[0] = measurement_pack.raw_measurements_[0];
      ekf_.x_[1] = measurement_pack.raw_measurements_[1];
    }

    float p_def = 5;
    ekf_.P_ << p_def, 0, 0, 0,
               0, p_def, 0, 0,
               0, 0, p_def, 0,
               0, 0, 0, p_def;

    previous_timestamp_ = measurement_pack.timestamp_;
    // done initializing, no need to predict or update
    
    is_initialized_ = true;
    return;
  }

  /**
   * Prediction
   */

  /**
   * Updating the state transition matrix F according to the new elapsed time.
   * Time is measured in seconds.
   * Updating the process noise covariance matrix.
   * Use noise_ax = 9 and noise_ay = 9 for your Q matrix.
   */
  float dt = (measurement_pack.timestamp_ - previous_timestamp_) / 1000000.0;
  previous_timestamp_ = measurement_pack.timestamp_;

  float dt_2 = dt * dt;
  float dt_3 = dt_2 * dt;
  float dt_4 = dt_3 * dt;

  static float noise_ax = 9;
  static float noise_ay = 9;

  ekf_.F_(0, 2) = dt;
  ekf_.F_(1, 3) = dt;

  ekf_.Q_ << dt_4 / 4 * noise_ax, 	0, 					        	dt_3 / 2 * noise_ax, 	0,
             0, 					       	  dt_4 / 4 * noise_ay, 	0, 					        	dt_3 / 2 * noise_ay,
             dt_3 / 2 * noise_ax, 	0, 					        	dt_2 * noise_ax, 	  	0,
             0, 					        	dt_3 / 2 * noise_ay, 	0, 					        	dt_2 * noise_ay;
  ekf_.Predict();

  /**
   * Update
   */

  /**
   * - Using the sensor type to perform the update step.
   * - Updating the state and covariance matrices.
   */

  if (measurement_pack.sensor_type_ == MeasurementPackage::RADAR) {
    // Radar updates
    Hj_ = tools.CalculateJacobian(ekf_.x_);
    ekf_.R_ = R_radar_;
    ekf_.H_ = Hj_;

    ekf_.UpdateEKF(measurement_pack.raw_measurements_);
  } else {
    // Laser updates
    ekf_.R_ = R_laser_;
    ekf_.H_ = H_laser_;
    ekf_.Update(measurement_pack.raw_measurements_);

  }

  // print the output
  cout << "x_ = " << ekf_.x_ << endl;
  cout << "P_ = " << ekf_.P_ << endl;
}
