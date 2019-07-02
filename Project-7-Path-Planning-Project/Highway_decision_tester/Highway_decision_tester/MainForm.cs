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
			public int v;
			public laneId_enum id;
			
			public Lane(laneId_enum id_) {
				dist = 0;
				id = id_;
				v = 0;
			}
		}
		
		Lane LeftLane_veh = new Lane(laneId_enum.LEFT_LANE);
		Lane MidLane_veh = new Lane(laneId_enum.MID_LANE);
		Lane RightLane_veh = new Lane(laneId_enum.RIGHT_LANE);		
		public MainForm()
		{
			//
			// The InitializeComponent() call is required for Windows Forms designer support.
			//
			InitializeComponent();
			
			//
			// TODO: Add constructor code after the InitializeComponent() call.
			//
			LeftLane_veh.dist = hsb_LeftLane.Value;
			lbl_LeftLane_dist.Text = LeftLane_veh.dist.ToString() + "m";
			tb_LeftLane_speed.Text = LeftLane_veh.v.ToString();
			
			MidLane_veh.dist = hsb_MidLane.Value;
			lbl_MidLane_dist.Text = MidLane_veh.dist.ToString() + "m";
			tb_MidLane_speed.Text = MidLane_veh.v.ToString();
			
			RightLane_veh.dist = hsb_RightLane.Value;
			lbl_RightLane_dist.Text = RightLane_veh.dist.ToString() + "m";
			tb_RightLane_speed.Text = RightLane_veh.v.ToString();

		}
		

		
		int get_Lane( int current_lane, Lane leftLane_, Lane midLane_, Lane rigtLane_) {
			
			
			
			return 0;
		}
		
		void displayLane(int id){
			
			
		}
		
		void HSB_Left_laneScroll(object sender, ScrollEventArgs e)
		{
			LeftLane_veh.dist = hsb_LeftLane.Value;
			lbl_LeftLane_dist.Text = LeftLane_veh.dist.ToString() + "m";
		}
		void Hsb_mid_laneScroll(object sender, ScrollEventArgs e)
		{
			MidLane_veh.dist = hsb_MidLane.Value;
			lbl_MidLane_dist.Text = MidLane_veh.dist.ToString() + "m";
		}
		void Hsb_right_laneScroll(object sender, ScrollEventArgs e)
		{
			RightLane_veh.dist = hsb_RightLane.Value;
			lbl_RightLane_dist.Text = RightLane_veh.dist.ToString() + "m";
		}
		void Tb_Left_lane_speedTextChanged(object sender, EventArgs e)
		{
			try {
				LeftLane_veh.v = Convert.ToInt32(tb_LeftLane_speed.Text);
			}
			catch {
				tb_LeftLane_speed.Text = "0";
			}
		}
		void Tb_Mid_lane_speedTextChanged(object sender, EventArgs e)
		{
			try {
				MidLane_veh.v = Convert.ToInt32(tb_MidLane_speed.Text);
			}
			catch {
				tb_MidLane_speed.Text = "0";
			}

		}
		void Tb_Right_lane_speedTextChanged(object sender, EventArgs e)
		{
			try {
				RightLane_veh.v = Convert.ToInt32(tb_RightLane_speed.Text);
			}
			catch {
				tb_RightLane_speed.Text = "0";
			}
		}
	}
}
