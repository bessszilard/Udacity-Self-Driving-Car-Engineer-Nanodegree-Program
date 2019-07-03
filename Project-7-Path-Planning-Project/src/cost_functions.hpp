#ifndef COST_FUNCTIONS_HPP
#define COST_FUNCTIONS_HPP

#include <math.h>

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

       void copy(Lane loc_lane) {
            dist = loc_lane.dist;
            id = loc_lane.id;
            v = loc_lane.v;
        }
    // private:

};

Lane LeftLane_veh = Lane(0);
Lane MidLane_veh = Lane(1);
Lane RightLane_veh = Lane(2);	

int get_Lane( int cur_lane, Lane leftLane_, Lane midLane_, Lane rigtLane_);
double car_distance_cost(Lane mid_lane, int intended_lane, int goal_lane_dist, int final_lane_dist);
double goal_distance_cost(int goal_lane, int intended_lane, int final_lane, double distance_to_goal);
double inefficiency_cost(double target_speed, int intended_lane, int final_lane, double lane_speeds[]);

		
int get_Lane( int cur_lane, Lane leftLane_, Lane midLane_, Lane rigtLane_, double my_vel) {
    Lane lanes[3];
    lanes[0].copy(leftLane_);
    lanes[1].copy(midLane_);
    lanes[2].copy(rigtLane_);
    int result = 0;
    
    double lane_speeds[] = {20.0, 10.0, 5.0};
//			// distance fine, -> KL
    // if (DIST_BUF < lanes[cur_lane].dist || PROP_VEL <= lanes[cur_lane].v )
    //     result = (int)lanes[cur_lane].id;
    // else if (0 < cur_lane ) {
    //     // go to lane 
    //     if(DIST_BUF < lanes[cur_lane - 1].dist)
    //         result = (int)lanes[cur_lane].id - 1;
    // }
    // else {
    //     // go to lane 
    //     if(DIST_BUF < lanes[cur_lane + 1].dist)
    //         result = (int)lanes[cur_lane].id + 1;
    // }
    
//			rtb_Pred_results.Clear();
    double weight[] = { 1.0f, 1.0, 1.0 };
    // rtb_Pred_results.Text = "";
    int intended_lane = cur_lane;
    double min_cost = 999;
    int next_lane = 0;
    for (int goal_lane = 0; goal_lane < 3; ++goal_lane) {
        for (int final_lane = 0; final_lane < 3; ++final_lane) {
            // invalid scenari
            if ((final_lane == goal_lane && (final_lane != goal_lane) || (intended_lane == final_lane && goal_lane != intended_lane))) {
                continue;
            }
            double cost1 = goal_distance_cost(goal_lane, intended_lane, final_lane, lanes[cur_lane].dist);
            double cost2 = inefficiency_cost(my_vel, intended_lane, goal_lane, lane_speeds);
            double cost3 = car_distance_cost(midLane_, intended_lane, lanes[goal_lane].dist, lanes[final_lane].dist);
            double cost_sum = weight[0] * cost1 + weight[1] * cost2 + weight[2]* cost3;
            
            if (cost_sum < min_cost) {
                min_cost = cost_sum;
                next_lane = goal_lane;
            }
            // rtb_Pred_results.AppendText(cur_lane.ToString() + " -> " + goal_lane + " -> " + final_lane + "\t");
            // rtb_Pred_results.AppendText(cost1.ToString("0.00000") + " \t" + cost2.ToString("0.00000") + "\t" + cost3.ToString("0.00000") + "\t");
            // rtb_Pred_results.AppendText(cost_sum.ToString("0.00000") + "\n");
        }
    }
    // rtb_Pred_results.AppendText("\n" + cur_lane.ToString() + " -> " + next_lane + "\n");
    result = next_lane;
    return result;
}

		double car_distance_cost(Lane mid_lane, int intended_lane, int goal_lane_dist, int final_lane_dist) {
			double cost_goal;
			double cost_final;
			
			if (abs(intended_lane - goal_lane_dist) <= 1)
				cost_goal = 30.0f / goal_lane_dist;
			else
				cost_goal = 30.0f / goal_lane_dist + 30.0f / mid_lane.dist;
			
			if (abs(intended_lane - final_lane_dist) <= 1)
				cost_final = 30.0f / final_lane_dist;
			else
				cost_final = 30.0f / final_lane_dist + 30.0f / mid_lane.dist;
			return cost_goal + cost_final;
		}
		
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
		  double cost = (2.0 * target_speed - speed_intended - speed_final) / (2.0 *  target_speed);
		  return cost;
		}


#endif /* COST_FUNCTIONS_HPP */

