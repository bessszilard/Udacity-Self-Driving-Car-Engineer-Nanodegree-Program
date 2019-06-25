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

/**
 * Returns the calculated throttle based on speed and steer value.
 * Goal is to accelerate on straight path, and slow down while the vehicle is steering.
 * @param speed the current speed in the simulator. Range: [0 ... 99]
 * @param steer_value is the PID output value
 * return throttle value
 */
double get_throttle(double speed, double steer_value) {
  // minimal speed
  if (speed < 30) {
    // std::cout << "acc" << std::endl;
    return 1.0;
  }
  else if (fabs(steer_value) < 0.2) {
    // std::cout << "maintain speed" << std::endl;
    return 0.6;
  }
  else if (fabs(steer_value) < 0.5) {
    // std::cout << "maintain speed" << std::endl;
    return - 0.3;
  }
  else if (0.5 < fabs(steer_value)) {
    // std::cout << "slow down" << std::endl;
    return - 0.9;
  }
  return 0.5;
}

    int
    main()
{
  uWS::Hub h;

  PID pid;
  PID pid_speed;
  /**
   * TODO: Initialize the pid variable.
   */
  // double Kp = 0.075f;
  // double Kd = 0.15f;
  // double Ki = 0.0f;
  double Kp = 0.2f;
  double Kd = 3.0f;
  double Ki = 0.0000325f;
  double steering_limits[2] = {-1.0f, 1.0f};
  pid.Init(Kp, Ki, Kd, steering_limits);

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
          double steer_value = pid.GetActuation(-cte);
          // static int counter = 0;

          // DEBUG
          std::cout << std::fixed << std::setprecision(5);
          std::cout << cte
          // std::cout << "CTE: " << cte // << "\tSteering Value: " << steer_value
                  << std::endl;//  << "\tref angle: " << ref_angle << "\tAngle: " << angle << std::endl;

          json msgJson;
          msgJson["steering_angle"] = steer_value;
          // double max_speed = 50;
          // if (max_speed <= speed )
          //   msgJson["throttle"] = 0.0;
          // else 
          //   // msgJson["throttle"] = 0.2;
          //   msgJson["throttle"] = 1.2;
          msgJson["throttle"] = get_throttle(speed, steer_value);

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