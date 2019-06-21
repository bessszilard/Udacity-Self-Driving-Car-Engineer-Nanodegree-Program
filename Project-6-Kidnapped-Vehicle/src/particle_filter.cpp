/**
 * particle_filter.cpp
 *
 * Created on: Dec 12, 2016
 * Author: Tiffany Huang
 */

#include "particle_filter.h"

#include <math.h>
#include <algorithm>
#include <iostream>
#include <iterator>
#include <numeric>
#include <random>
#include <string>
#include <vector>

#include "helper_functions.h"

using std::normal_distribution;
using std::string;
using std::vector;
using std::cout;
using std::endl;


void ParticleFilter::init(double x, double y, double theta, double std[]) {
  /**
   * TODO: Set the number of particles. Initialize all particles to 
   *   first position (based on estimates of x, y, theta and their uncertainties
   *   from GPS) and all weights to 1. 
   * TODO: Add random Gaussian noise to each particle.
   * NOTE: Consult particle_filter.h for more information about this method 
   *   (and others in this file).
   */
  num_particles = 100;  // TODO: Set the number of particles
  std::default_random_engine gen;

  double std_x = std[0];
  double std_y = std[1];
  double std_theta = std[2];

  // This line creates a normal (Gaussian) distribution for x
  normal_distribution<double> dist_x(x, std_x);

  // TODO: Create normal distributions for y and theta
  normal_distribution<double> dist_y(y, std_y);
  normal_distribution<double> dist_theta(theta, std_theta);

  particles.resize(num_particles); // allocating memory for N particles

  cout << "Particles number" << particles.size() << endl;
  for (size_t i = 0; i < particles.size(); ++i) {
    // TODO: Sample from these normal distributions like this:
    //   sample_x = dist_x(gen);
    //   where "gen" is the random engine initialized earlier.
    particles[i].x = dist_x(gen);    
    particles[i].y = dist_y(gen);
    particles[i].theta = dist_theta(gen);

    // weights
    particles[i].weight = 1;
  }
  is_initialized = true;
}
/**
 * Returns the prediction of the given variable based on Lesson 8 formulas
 */
inline double get_prediction(Particle particle, double v, double thetaD, double dt, char operation) {
  switch(operation) {
    case 'x': return particle.x + v / thetaD * (sin(particle.theta + thetaD * dt) - sin(particle.theta));
    case 'y': return particle.y + v / thetaD * (cos(particle.theta) - cos(particle.theta + thetaD * dt));
    case 't': return particle.theta + thetaD * dt;
    default:  return 0;  // unkonown command
  }
}

void ParticleFilter::prediction(double delta_t, double std_pos[], double velocity, double yaw_rate) {
  /**
   * TODO: Add measurements to each particle and add random Gaussian noise.
   * NOTE: When adding noise you may find std::normal_distribution 
   *   and std::default_random_engine useful.
   *  http://en.cppreference.com/w/cpp/numeric/random/normal_distribution
   *  http://www.cplusplus.com/reference/random/default_random_engine/
   */

  std::default_random_engine gen;

  double std_x = std_pos[0];
  double std_y = std_pos[1];
  double std_theta = std_pos[2];

  for (size_t i = 0; i < particles.size(); ++i) {
    double x_f     = get_prediction(particles[i], velocity, yaw_rate, delta_t, 'x');
    double y_f     = get_prediction(particles[i], velocity, yaw_rate, delta_t, 'y');
    double theta_f = get_prediction(particles[i], velocity, yaw_rate, delta_t, 't');

    normal_distribution<double> dist_x(x_f, std_x);
    normal_distribution<double> dist_y(y_f, std_y);
    normal_distribution<double> dist_theta(theta_f, std_theta);

    particles[i].x = dist_x(gen);
    particles[i].y = dist_y(gen);
    particles[i].theta = dist_theta(gen);
  }
}

/**
 *  @param predicted - predictive measurements between a particle and all of the map landmarks in sensor range 
 *  @param observations- actual measurments from the LIDAR 
 */
void ParticleFilter::dataAssociation(vector<LandmarkObs> predicted, 
                                     vector<LandmarkObs> &observations) {
  /**
   * TODO: Find the predicted measurement that is closest to each 
   *   observed measurement and assign the observed measurement to this 
   *   particular landmark.
   * NOTE: this method will NOT be called by the grading code. But you will 
   *   probably find it useful to implement this method and use it as a helper 
   *   during the updateWeights phase.
   */
  cout << "dataAssociation " << predicted.size() << " ";
  cout << observations.size() << endl;
  if (0 < predicted.size()) {
    for (size_t i = 0; i < observations.size(); ++i)
    {
      size_t min_obs_idx = 0;
      double min_obs = dist(predicted[0].x, predicted[0].y, observations[i].x, observations[i].y);
      for (size_t j = 1; j < predicted.size(); ++j)
      {
        double dist_temp = dist(predicted[j].x, predicted[j].y, observations[i].x, observations[i].y);
        if (min_obs > dist_temp)
        {
          min_obs = dist_temp;
          min_obs_idx = j;
        }
      }
      observations[i].x = predicted[min_obs_idx].x;
      observations[i].y = predicted[min_obs_idx].y;
      observations[i].id = predicted[min_obs_idx].id;
    }
  }
}

vector<LandmarkObs> get_in_range_landmarks(double sensor_range, Particle particle, Map map_landmarks) {
  vector<LandmarkObs> predicted;
  for (size_t i = 0; i < map_landmarks.landmark_list.size(); ++i) {
    // whithin range
    if (sensor_range >= dist(particle.x, particle.y, map_landmarks.landmark_list[i].x_f, map_landmarks.landmark_list[i].y_f)) {
      // add object to 
      LandmarkObs in_range_landmark = {
        map_landmarks.landmark_list[i].id_i,
        map_landmarks.landmark_list[i].x_f,
        map_landmarks.landmark_list[i].y_f
      };
        predicted.push_back(in_range_landmark);
      }
    }
  return predicted;
}

void transform_to_map(Particle particle_pos, vector<LandmarkObs> &observations) {

  for(size_t i = 0; i < observations.size(); ++i) {
    double x_p = particle_pos.x;
    double y_p = particle_pos.y;
    double theta = particle_pos.theta;
    double x_c = observations[i].x;  // car observation
    double y_c = observations[i].y;  // car observation

    observations[i].x = x_p + cos(theta) * x_c - sin(theta) * y_c;
    observations[i].y = y_p + sin(theta) * x_c + cos(theta) * y_c;
  }
}

// double get_RMSE(vector<LandmarkObs> particle_obs, vector<LandmarkObs> sensor_obs){
//   double error[3];
//   error = getError(particle_obs.x, particle_obs.y, particle_obs.th)
// }
  
    /**
 * @param sensor_range - range of the sensor
 * @param std_landmark - landmark measurements uncertainities
 * @param observations - vector of landmark measurements
 */
void ParticleFilter::updateWeights(double sensor_range, double std_landmark[],
                                       const vector<LandmarkObs> &observations,
                                       const Map &map_landmarks) {
  /**
   * TODO: Update the weights of each particle using a mult-variate Gaussian 
   *   distribution. You can read more about this distribution here: 
   *   https://en.wikipedia.org/wiki/Multivariate_normal_distribution
   * NOTE: The observations are given in the VEHICLE'S coordinate system. 
   *   Your particles are located according to the MAP'S coordinate system. 
   *   You will need to transform between the two systems. Keep in mind that
   *   this transformation requires both rotation AND translation (but no scaling).
   *   The following is a good resource for the theory:
   *   https://www.willamette.edu/~gorr/classes/GeneralGraphics/Transforms/transforms2d.htm
   *   and the following is a good resource for the actual equation to implement
   *   (look at equation 3.33) http://planning.cs.uiuc.edu/node99.html
   */

  // Step 1. Predict measurements to all landmarks within sensor range for each particle
  for (size_t i = 0; i < particles.size(); ++i)  {
    vector<LandmarkObs> temp_obs(observations); // deep copy
    vector<LandmarkObs> temp_obs_landmark; // deep copy
    transform_to_map(particles[i], temp_obs);
    
    // // Step 2. With predicted landmark measurements we can call the dataAssociation() function
    // // to associate the sensor measurments to map landmarks
    temp_obs_landmark = temp_obs;
    vector<LandmarkObs> predicted = get_in_range_landmarks(sensor_range, particles[i], map_landmarks);
    dataAssociation(predicted, temp_obs_landmark);

    // Step 3. Calculate the new weights of the particles


    // double error = getError()
    // if ( i == 5 )
    //   cout << predicted.size() << " " << observations.size() << endl;
  }
        // vector<LandmarkObs> predicted


        // Step 4. Normalize the weights

        // for(size_t i = 0; i < observations.size(); ++i) {
        //   cout << observations[i].id << " " << observations[i].x << " " << observations[i].y << "\t";
        // }
        // cout << endl;

    //     for (size_t i = 0; i < map_landmarks.landmark_list.size(); ++i)
    // {
    //   cout << map_landmarks.landmark_list[i].id_i << " " << map_landmarks.landmark_list[i].x_f << " " << map_landmarks.landmark_list[i].y_f << "\t";
    // }
    // cout << endl;

    // double prob = 1.0;
    // for (int i = 0; i < observations.size(); ++i)
    // {
    //   double dist =

    // }
    // cout << map_landmarks.landmark_list.size() << " " << observations.size() << endl;

}

void ParticleFilter::resample() {
  /**
   * TODO: Resample particles with replacement with probability proportional 
   *   to their weight. 
   * NOTE: You may find std::discrete_distribution helpful here.
   *   http://en.cppreference.com/w/cpp/numeric/random/discrete_distribution
   */

  // 

}

void ParticleFilter::SetAssociations(Particle& particle, 
                                     const vector<int>& associations, 
                                     const vector<double>& sense_x, 
                                     const vector<double>& sense_y) {
  // particle: the particle to which assign each listed association, 
  //   and association's (x,y) world coordinates mapping
  // associations: The landmark id that goes along with each listed association
  // sense_x: the associations x mapping already converted to world coordinates
  // sense_y: the associations y mapping already converted to world coordinates
  particle.associations= associations;
  particle.sense_x = sense_x;
  particle.sense_y = sense_y;
}

string ParticleFilter::getAssociations(Particle best) {
  vector<int> v = best.associations;
  std::stringstream ss;
  copy(v.begin(), v.end(), std::ostream_iterator<int>(ss, " "));
  string s = ss.str();
  s = s.substr(0, s.length()-1);  // get rid of the trailing space
  return s;
}

string ParticleFilter::getSenseCoord(Particle best, string coord) {
  vector<double> v;

  if (coord == "X") {
    v = best.sense_x;
  } else {
    v = best.sense_y;
  }

  std::stringstream ss;
  copy(v.begin(), v.end(), std::ostream_iterator<float>(ss, " "));
  string s = ss.str();
  s = s.substr(0, s.length()-1);  // get rid of the trailing space
  return s;
}