#include <math.h>
#include <uWS/uWS.h>
#include <iostream>
#include <string>
#include "json.hpp"
#include "PID.h"
#include "math.h"

// for convenience
using nlohmann::json;
using std::string;

// For converting back and forth between radians and degrees.
constexpr double pi() { return M_PI; }
double deg2rad(double x) { return x * pi() / 180; }
double rad2deg(double x) { return x * 180 / pi(); }

// Checks if the SocketIO event has JSON data.
// If there is data the JSON object in string format will be returned,
// else the empty string "" will be returned.
string hasData(string s) {
  auto found_null = s.find("null");
  auto b1 = s.find_first_of("[");
  auto b2 = s.find_last_of("]");
  if (found_null != string::npos) {
    return "";
  }
  else if (b1 != string::npos && b2 != string::npos) {
    return s.substr(b1, b2 - b1 + 1);
  }
  return "";
}

double angle_trajectory_gen(double cte, double limit[2]) {
  double norm = 60.0f;//3.5f;
  double angle = -sin(cte / norm * M_PI_2l ) * limit[1]; // this is an angle
  if (angle < limit[0])
    angle = -limit[0];
  if (limit[1] < angle)
    angle = limit[1];
  return angle;
}

int main() {
  uWS::Hub h;

  PID pid;
  PID pid_speed;
  /**
   * TODO: Initialize the pid variable.
   */
  // double Kp = 0.075f;
  // double Kd = 0.15f;
  // double Ki = 0.0f;
  double Kp = 0.1f;
  double Kd = 3.0f;
  double Ki = 0.0000325f;
  double steering_limits[2] = {-1.0f, 1.0f};
  pid.Init(Kp, Ki, Kd, steering_limits);

  double Kp_speed = 0.075f;
  double Kd_speed = 0.0f;
  double Ki_speed = 0.0f;
  double throttle_limits[2] = {-1.0f, 1.0f};
  pid_speed.Init(Kp_speed, Ki_speed, Kd_speed, throttle_limits);


  h.onMessage([&pid](uWS::WebSocket<uWS::SERVER> ws, char *data, size_t length, 
                     uWS::OpCode opCode) {
    // "42" at the start of the message means there's a websocket message event.
    // The 4 signifies a websocket message
    // The 2 signifies a websocket event
    if (length && length > 2 && data[0] == '4' && data[1] == '2') {
      auto s = hasData(string(data).substr(0, length));

      if (s != "") {
        auto j = json::parse(s);

        string event = j[0].get<string>();

        if (event == "telemetry") {
          // j[1] is the data JSON object
          double cte = std::stod(j[1]["cte"].get<string>());
          double speed = std::stod(j[1]["speed"].get<string>());
          double angle = std::stod(j[1]["steering_angle"].get<string>());

          double angle_limits[2] = {-10.0f, 10.0f};
          double ref_angle = angle_trajectory_gen(cte, angle_limits);
          double steer_value = pid.GetActuation(-cte); // ref_angle - angle);
          /**
           * TODO: Calculate steering value here, remember the steering value is
           *   [-1, 1].
           * NOTE: Feel free to play around with the throttle and speed.
           *   Maybe use another PID controller to control the speed!
           */

          // DEBUG
          std::cout << std::fixed << std::setprecision(5);
          std::cout << "CTE: " << cte << "\tSteering Value: " << steer_value
                  << std::endl;//  << "\tref angle: " << ref_angle << "\tAngle: " << angle << std::endl;

          json msgJson;
          msgJson["steering_angle"] = steer_value;
          double max_speed = 30;
          if (max_speed <= speed )
            msgJson["throttle"] = 0.0;
          else 
            // msgJson["throttle"] = 0.2;
            msgJson["throttle"] = 1.2;

          auto msg = "42[\"steer\"," + msgJson.dump() + "]";
          // std::cout << msg << std::endl;
          ws.send(msg.data(), msg.length(), uWS::OpCode::TEXT);
        }  // end "telemetry" if
      } else {
        // Manual driving
        string msg = "42[\"manual\",{}]";
        ws.send(msg.data(), msg.length(), uWS::OpCode::TEXT);
      }
    }  // end websocket message if
  }); // end h.onMessage

  h.onConnection([&h](uWS::WebSocket<uWS::SERVER> ws, uWS::HttpRequest req) {
    std::cout << "Connected!!!" << std::endl;
  });

  h.onDisconnection([&h](uWS::WebSocket<uWS::SERVER> ws, int code, 
                         char *message, size_t length) {
    ws.close();
    std::cout << "Disconnected" << std::endl;
  });

  int port = 4567;
  if (h.listen(port)) {
    std::cout << "Listening to port " << port << std::endl;
  } else {
    std::cerr << "Failed to listen to port" << std::endl;
    return -1;
  }
  
  h.run();
}