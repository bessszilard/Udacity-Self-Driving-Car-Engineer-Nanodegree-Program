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
			
		class Lane {
			public int dist;
			public double v;
			public laneId_enum id;
			
			public Lane() {
				dist = 0;
				id = 0;
				v = 0;
			}
			
			public Lane(laneId_enum id_) {
				dist = 0;
				id = id_;
				v = 0;
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
			
			// distance fine, -> KL
			if (DIST_BUF < lanes[cur_lane].dist || PROP_VEL <= lanes[cur_lane].v )
				return (int)lanes[cur_lane].id;
			if (0 < cur_lane ) {
				// go to lane 
				if(DIST_BUF < lanes[cur_lane - 1].dist)
					return (int)lanes[cur_lane].id - 1;
			}
			else {
				// go to lane 
				if(DIST_BUF < lanes[cur_lane + 1].dist)
					return (int)lanes[cur_lane].id + 1;
			}
			return (int)lanes[cur_lane].id;
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
	}
}
