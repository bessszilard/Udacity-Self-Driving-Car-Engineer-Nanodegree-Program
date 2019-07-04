#include "cost_functions.hpp"
#include <math.h>
#include <iostream>
#include <limits.h>
#include <iomanip>      // std::setprecision

using std::cout;
using std::endl;

static double car_distance_cost(Lane mid_lane, int intended_lane, int goal_lane_dist, int final_lane_dist);
static double goal_distance_cost(int goal_lane, int intended_lane, int final_lane, double distance_to_goal);
static double inefficiency_cost(double target_speed, int intended_lane, int final_lane, double lane_speeds[]);
static void update_single_lane(nlohmann::json sensor_fusion, int i, Lane &loc_lane, int lane, float d, double car_s, bool &too_close, int prev_size);

void update_single_lane(nlohmann::json sensor_fusion, int i, Lane &loc_lane, int lane, float d, double car_s, bool &too_close, int prev_size) {
     if (d < (2 + 4 * loc_lane.id + 2) && d > (2 + 4 * loc_lane.id - 2)) { // car is in left lane 
        double vx = sensor_fusion[i][3];
        double vy = sensor_fusion[i][4];
        double check_speed = sqrt(vx * vx + vy * vy);
        double check_car_s = sensor_fusion[i][5];

        check_car_s += ((double) prev_size * 0.02 * check_speed);
        // we look for the nearest car which is ahead of us and or aside of us
        if ((check_car_s - car_s) < loc_lane.dist && car_s < check_car_s + 10) {
        loc_lane.dist = check_car_s - car_s;
        loc_lane.v    = check_speed;
        }
        if (lane == loc_lane.id && (check_car_s > car_s) && ((check_car_s - car_s) < 30)) {
            too_close = true;
        }
    }
}

bool update_lanes(nlohmann::json sensor_fusion, double car_s, int prev_size, int lane, Lane &LeftLane, Lane &MidLane, Lane &RightLane) {
    bool too_close = false;
    for (size_t i = 0; i < sensor_fusion.size(); ++i) {
        float d = sensor_fusion[i][6];
        update_single_lane(sensor_fusion, i, LeftLane,  lane, d, car_s, too_close, prev_size);
        update_single_lane(sensor_fusion, i, MidLane,   lane, d, car_s, too_close, prev_size);
        update_single_lane(sensor_fusion, i, RightLane, lane, d, car_s, too_close, prev_size);
    }
    return too_close;
}
/**
 * Returns the prefered lane
 */
int get_Lane( int cur_lane, Lane leftLane_, Lane midLane_, Lane rigtLane_, double my_vel, double &goal_speed) {
    Lane lanes[3];
    lanes[0].copy(leftLane_);
    lanes[1].copy(midLane_);
    lanes[2].copy(rigtLane_);
    int result = 0;
    
    cout <<  std::fixed << std::setprecision(5);

    double lane_speeds[] = {20.0, 10.0, 5.0};
    double weight[] = { 1.0f, 1.0, 10.0 };
    // rtb_Pred_results.Text = "";
    int intended_lane = cur_lane;
    double min_cost = 999;
    double min_cost_speed = 0.0f;
    double costs_print[3] = {0, 0, 0};
    int next_lane = 0;
    for (int goal_lane = 0; goal_lane < 3; ++goal_lane) {
        for (int final_lane = 0; final_lane < 3; ++final_lane) {
            // invalid scenari
            if ((final_lane == goal_lane && (final_lane != goal_lane)           || 
                (intended_lane == final_lane && goal_lane != intended_lane))    ||
                abs(intended_lane - goal_lane) == 2 || abs(final_lane - goal_lane) == 2)  {
                continue;
            }
            double cost1 = goal_distance_cost(goal_lane, intended_lane, final_lane, lanes[cur_lane].dist);
            double cost2 = inefficiency_cost(my_vel, intended_lane, goal_lane, lane_speeds);
            double cost3 = car_distance_cost(midLane_, intended_lane, lanes[goal_lane].dist, lanes[final_lane].dist);
            double cost_sum = weight[0] * cost1 + weight[1] * cost2 + weight[2]* cost3;
            
            if (cost_sum < min_cost) {
                min_cost = cost_sum;
                next_lane = goal_lane;
                min_cost_speed = lanes[cur_lane].v;
                costs_print[0] = cost1;
                costs_print[1] = cost2;
                costs_print[2] = cost3;
            }
            cout << cur_lane << " -> " << goal_lane << " -> " << final_lane << "\t" << cost_sum  << endl;
            // cout << " \t" << cost1 << "\t" << cost2 << "\t" << cost3;
            // cout << "\t\t" << lanes[goal_lane].dist << "\t" << lanes[final_lane].dist;
            // cout << endl;
        }
    }
    // rtb_Pred_results.AppendText("\n" + cur_lane.ToString() + " -> " + next_lane + "\n");
    cout << cur_lane << " -> " << next_lane << "\t\t" << min_cost << endl;
    // cout << "\t\t" << costs_print[0] << "\t" << costs_print[1] << "\t" << costs_print[2]  << endl;
    cout << "------------------------" << endl;
    
    if (min_cost < weight[2]) {  // if it too risky, we will stay in the lane
        goal_speed = 49.5;       // max speed
        return next_lane;
    }
    else {
        if (cur_lane != next_lane)
            cout << "STAY IN THE LINE\n";
        goal_speed = min_cost_speed;    // lane speed
        return cur_lane;
    }
}

/**
 * The cost helps to choose that lane, which car is furthest away.
 */
double car_distance_cost(Lane mid_lane, int intended_lane, int goal_lane_dist, int final_lane_dist) {
    double cost_goal  = (double)(goal_lane_dist)  + 10;
    double cost_final = (double)(final_lane_dist) + 10;
    
    if (300 < cost_goal)
        cost_goal = 300;
    if (300 < cost_final)
        cost_final = 300;

    if (goal_lane_dist < 30)        // smaller than alloved distance return with max error
        return 1;

    return 1 - exp( - 1.0 / (fabs(cost_goal * 3 + cost_final)));
}

/**
 * The cost helps to choose the fastest lane
 */
double goal_distance_cost(int goal_lane, int intended_lane, int final_lane, double distance_to_goal) {
    // The cost increases with both the distance of intended lane from the goal
    //   and the distance of the final lane from the goal. The cost of being out 
    //   of the goal lane also becomes larger as the vehicle approaches the goal.
    
    double cost = 1 - exp(-abs(2.0f * goal_lane - intended_lane - final_lane) / distance_to_goal);
    return cost;
}

//		double inefficiency_cost(int target_speed, int intended_lane, int final_lane, const std::vector<int> &lane_speeds) {
double inefficiency_cost(double target_speed, int intended_lane, int final_lane, double lane_speeds[]) {
    // Cost becomes higher for trajectories with intended lane and final lane 
    //   that have traffic slower than target_speed.
    double speed_intended = lane_speeds[intended_lane];
    double speed_final = lane_speeds[final_lane];
    double cost = abs((2.0 * target_speed - speed_intended - speed_final) / (2.0 *  target_speed));
    if (10.0f < fabs(cost))
        cost = 10.0f;
    return cost;
}
