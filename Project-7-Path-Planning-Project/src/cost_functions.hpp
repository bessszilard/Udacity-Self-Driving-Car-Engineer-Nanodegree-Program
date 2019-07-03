#ifndef COST_FUNCTIONS_HPP
#define COST_FUNCTIONS_HPP
#include "json.hpp"

class Lane {
    public: 
        int dist;
        double v;
        int id;
        Lane() {
            dist = 0;
            id = 0;
            v = 0;
        }
        Lane(int id_) {
            dist = 0;
            id = id_;
            const double DEF_LANE_VEL = 10.0f;
            v = DEF_LANE_VEL - (double)id_ * DEF_LANE_VEL / 4;
        }
        Lane(int id_, int dist_s) {
            dist = dist_s;
            id = id_;
            const double DEF_LANE_VEL = 10.0f;
            v = DEF_LANE_VEL - (double)id_ * DEF_LANE_VEL / 4;
        }

       void copy(Lane loc_lane) {
            dist = loc_lane.dist;
            id = loc_lane.id;
            v = loc_lane.v;
        }
};
bool update_lanes(nlohmann::json sensor_fusion, double car_s, int prev_size, int lane, Lane &LeftLane, Lane &MidLane, Lane &RightLane);
int  get_Lane( int cur_lane, Lane leftLane_, Lane midLane_, Lane rigtLane_, double my_vel, double &goal_speed);

#endif /* COST_FUNCTIONS_HPP */

