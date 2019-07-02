/*
 * Created by SharpDevelop.
 * User: szilard
 * Date: 2019-07-02
 * Time: 9:16 AM
 * 
 * To change this template use Tools | Options | Coding | Edit Standard Headers.
 */
using System;
using System.Collections.Generic;
using System.Drawing;
using System.Windows.Forms;

namespace Highway_decision_tester
{
	/// <summary>
	/// Description of MainForm.
	/// </summary>
	
	
	public partial class MainForm : Form
	{	
		enum actions_enum { KL, LCL, RCL };
		enum laneId_enum { LEFT_LANE, MID_LANE, RIGHT_LANE };
		const double DEF_MY_VEL = 20.0f;

		class Lane {
			public int dist;
			public double v;
			public laneId_enum id;
			private const double DEF_LANE_VEL = 10.0f;
			
			public Lane() {
				dist = 0;
				id = 0;
				v = 0;
			}
			
			public Lane(laneId_enum id_) {
				dist = 0;
				id = id_;
				v = DEF_LANE_VEL - (double)id_ * DEF_LANE_VEL / 4;
			}
		}
		
		Lane LeftLane_veh = new Lane(laneId_enum.LEFT_LANE);
		Lane MidLane_veh = new Lane(laneId_enum.MID_LANE);
		Lane RightLane_veh = new Lane(laneId_enum.RIGHT_LANE);		
		
		Color def_but_bg_color;
		
		public MainForm()
		{
			//
			// The InitializeComponent() call is required for Windows Forms designer support.
			//
			InitializeComponent();
			
			LeftLane_veh.dist = hsb_LeftLane.Value;
			lbl_LeftLane_dist.Text = LeftLane_veh.dist.ToString() + "m";
			tb_LeftLane_speed.Text = LeftLane_veh.v.ToString();
			
			MidLane_veh.dist = hsb_MidLane.Value;
			lbl_MidLane_dist.Text = MidLane_veh.dist.ToString() + "m";
			tb_MidLane_speed.Text = MidLane_veh.v.ToString();
			
			RightLane_veh.dist = hsb_RightLane.Value;
			lbl_RightLane_dist.Text = RightLane_veh.dist.ToString() + "m";
			tb_RightLane_speed.Text = RightLane_veh.v.ToString();
			def_but_bg_color = bt_LeftLane_pred.BackColor;
			
			my_vel = DEF_MY_VEL;
			tb_my_vel.Text = my_vel.ToString();
		}
		
		laneId_enum get_current_pos() {
			laneId_enum current_lane = laneId_enum.RIGHT_LANE;
			if (rb_LeftLane.Checked)		current_lane = laneId_enum.LEFT_LANE;
			else if (rb_MidLane.Checked)	current_lane = laneId_enum.MID_LANE;
			
			return current_lane;
		}
		
		void set_current_pos(laneId_enum id) {
			rb_LeftLane.Checked = false;
			rb_MidLane.Checked = false;
			rb_RightLane.Checked = false;
			
			switch(id) {
				case laneId_enum.LEFT_LANE: 
					rb_LeftLane.Checked = true;
					break;
				case laneId_enum.MID_LANE: 
					rb_MidLane.Checked = true;
					break;
				case laneId_enum.RIGHT_LANE: 
					rb_RightLane.Checked = true;
					break;
				
			}
		}
		
		const int DIST_BUF = 30;
		const double PROP_VEL = 49.5;
		double my_vel = 0.0f;
		int get_Lane( int cur_lane, Lane leftLane_, Lane midLane_, Lane rigtLane_) {
			Lane[] lanes = new Lane[3];
			lanes[0] = leftLane_;
			lanes[1] = midLane_;
			lanes[2] = rigtLane_;
			int result = 0;
			
			double[] lane_speeds = {20.0, 10.0, 5.0};
//			// distance fine, -> KL
			if (DIST_BUF < lanes[cur_lane].dist || PROP_VEL <= lanes[cur_lane].v )
				result = (int)lanes[cur_lane].id;
			else if (0 < cur_lane ) {
				// go to lane 
				if(DIST_BUF < lanes[cur_lane - 1].dist)
					result = (int)lanes[cur_lane].id - 1;
			}
			else {
				// go to lane 
				if(DIST_BUF < lanes[cur_lane + 1].dist)
					result = (int)lanes[cur_lane].id + 1;
			}
			
//			rtb_Pred_results.Clear();
			double[] weight = { Convert.ToDouble(tb_cost_w1.Text), Convert.ToDouble(tb_cost_w2.Text), Convert.ToDouble(tb_cost_w3.Text)};
			rtb_Pred_results.Text = "";
			int intended_lane = cur_lane;
			for (int goal_lane = 0; goal_lane < 3; ++goal_lane) {
				for (int final_lane = 0; final_lane < 3; ++final_lane) {
					// invalid scenari
					if ((final_lane == goal_lane && (final_lane != goal_lane) || (intended_lane == final_lane && goal_lane != intended_lane))) {
						continue;
					}
					double cost1 = goal_distance_cost(goal_lane, intended_lane, final_lane, lanes[cur_lane].dist);
					double cost2 = inefficiency_cost(my_vel, intended_lane, goal_lane, lane_speeds);
					double cost3 = car_distance_cost(lanes[final_lane].dist);
					double cost_sum = weight[0] * cost1 + weight[1] * cost2 + weight[2]* cost3;
					rtb_Pred_results.AppendText(cur_lane.ToString() + " -> " + goal_lane + " -> " + final_lane + "\t");
					rtb_Pred_results.AppendText(cost1.ToString("0.00000") + " \t" + cost2.ToString("0.00000") + "\t" + cost3.ToString("0.00000") + "\t");
					rtb_Pred_results.AppendText(cost_sum.ToString("0.00000") + "\n");
				}
			}
			
			return result;
		}
		double car_distance_cost(int goal_lane_dist) {
			return 30.0f / goal_lane_dist;
		}
		
		double goal_distance_cost(int goal_lane, int intended_lane, int final_lane, double distance_to_goal) {
		  // The cost increases with both the distance of intended lane from the goal
		  //   and the distance of the final lane from the goal. The cost of being out 
		  //   of the goal lane also becomes larger as the vehicle approaches the goal.
		    
		  double cost = 1 - Math.Exp(-Math.Abs(2.0f * goal_lane - intended_lane - final_lane) / distance_to_goal);
		  return cost;
		}
		
//		double inefficiency_cost(int target_speed, int intended_lane, int final_lane, const std::vector<int> &lane_speeds) {
		double inefficiency_cost(double target_speed, int intended_lane, int final_lane, double[] lane_speeds) {
		  // Cost becomes higher for trajectories with intended lane and final lane 
		  //   that have traffic slower than target_speed.
		  double speed_intended = lane_speeds[intended_lane];
		  double speed_final = lane_speeds[final_lane];
		  double cost = (2.0 * target_speed - speed_intended - speed_final) / (2.0 *  target_speed);
		  return cost;
		}
		
		void displayLane(){
			int current_lane = (int)get_current_pos();
			laneId_enum id_ = (laneId_enum)get_Lane( current_lane, LeftLane_veh, MidLane_veh, RightLane_veh);
			switch(id_) {
				case laneId_enum.LEFT_LANE:
					bt_LeftLane_pred.BackColor = Color.Lime;
					bt_MidLane_pred.BackColor = def_but_bg_color;
					bt_RightLane_pred.BackColor = def_but_bg_color;
					break;
				case laneId_enum.MID_LANE:
					bt_LeftLane_pred.BackColor = def_but_bg_color;
					bt_MidLane_pred.BackColor = Color.Lime;
					bt_RightLane_pred.BackColor = def_but_bg_color;
					break;
				case laneId_enum.RIGHT_LANE:
					bt_LeftLane_pred.BackColor = def_but_bg_color;
					bt_MidLane_pred.BackColor = def_but_bg_color;
					bt_RightLane_pred.BackColor = Color.Lime;;
					break;
			}
		}
		
		void HSB_Left_laneScroll(object sender, ScrollEventArgs e)
		{
			LeftLane_veh.dist = hsb_LeftLane.Value;
			lbl_LeftLane_dist.Text = LeftLane_veh.dist.ToString() + "m";
			displayLane();
		}
		void Hsb_mid_laneScroll(object sender, ScrollEventArgs e)
		{
			MidLane_veh.dist = hsb_MidLane.Value;
			lbl_MidLane_dist.Text = MidLane_veh.dist.ToString() + "m";
			displayLane();
		}
		void Hsb_right_laneScroll(object sender, ScrollEventArgs e)
		{
			RightLane_veh.dist = hsb_RightLane.Value;
			lbl_RightLane_dist.Text = RightLane_veh.dist.ToString() + "m";
			displayLane();
		}
		void Tb_Left_lane_speedTextChanged(object sender, EventArgs e)
		{
			try {
				LeftLane_veh.v = Convert.ToDouble(tb_LeftLane_speed.Text);
			}
			catch {
				tb_LeftLane_speed.Text = "0";
			}
			displayLane();
		}
		void Tb_Mid_lane_speedTextChanged(object sender, EventArgs e)
		{
			try {
				MidLane_veh.v = Convert.ToDouble(tb_MidLane_speed.Text);
			}
			catch {
				tb_MidLane_speed.Text = "0";
			}
			displayLane();
		}
		void Tb_Right_lane_speedTextChanged(object sender, EventArgs e)
		{
			try {
				RightLane_veh.v = Convert.ToDouble(tb_RightLane_speed.Text);
			}
			catch {
				tb_RightLane_speed.Text = "0";
			}
			displayLane();
		}
		void Bt_get_predClick(object sender, EventArgs e)
		{
			displayLane();
		}
		void Rb_LeftLaneCheckedChanged(object sender, EventArgs e)
		{
			displayLane();
		}
		void Rb_MidLaneCheckedChanged(object sender, EventArgs e)
		{
			displayLane();
		}
		void Rb_RightLaneCheckedChanged(object sender, EventArgs e)
		{
			displayLane();
		}
		
		void update_dist(ref HScrollBar sb, ref Label lbl, ref Lane lane_, double my_vel){
			int nextLeftLaneValue = (int)(lane_.dist - my_vel - lane_.v);
			if (nextLeftLaneValue < 0 )
				nextLeftLaneValue += sb.Maximum;
			if (sb.Maximum < nextLeftLaneValue)
				nextLeftLaneValue -= sb.Maximum;
			lane_.dist = nextLeftLaneValue;
			sb.Value = nextLeftLaneValue;
			hsb_LeftLane.Update();
			lbl.Text = lane_.dist.ToString() + "m";
		}
		
		void Bt_stepClick(object sender, EventArgs e)
		{
			update_dist(ref hsb_LeftLane, ref lbl_LeftLane_dist, ref LeftLane_veh, my_vel);
			update_dist(ref hsb_MidLane, ref lbl_MidLane_dist, ref MidLane_veh, my_vel);
			update_dist(ref hsb_RightLane, ref lbl_RightLane_dist, ref RightLane_veh, my_vel);
			
			set_current_pos((laneId_enum) get_Lane( (int)get_current_pos(), LeftLane_veh, MidLane_veh, RightLane_veh));
		}
		void Tb_my_velTextChanged(object sender, EventArgs e)
		{
			try {
				my_vel = Convert.ToDouble(tb_my_vel.Text);
			}
			catch {
				tb_my_vel.Text = "0";
			}
			displayLane();	
		}
		void Bt_One_step_backClick(object sender, EventArgs e)
		{
			update_dist(ref hsb_LeftLane, ref lbl_LeftLane_dist, ref LeftLane_veh, -my_vel);
			update_dist(ref hsb_MidLane, ref lbl_MidLane_dist, ref MidLane_veh, -my_vel);
			update_dist(ref hsb_RightLane, ref lbl_RightLane_dist, ref RightLane_veh, -my_vel);
			
			set_current_pos((laneId_enum) get_Lane( (int)get_current_pos(), LeftLane_veh, MidLane_veh, RightLane_veh));
		}
		void Tb_cost_w1TextChanged(object sender, EventArgs e)
		{
			displayLane();
		}
		void Tb_cost_w2TextChanged(object sender, EventArgs e)
		{
			displayLane();
		}
		void Tb_cost_w3TextChanged(object sender, EventArgs e)
		{
			displayLane();
		}
	}
}
