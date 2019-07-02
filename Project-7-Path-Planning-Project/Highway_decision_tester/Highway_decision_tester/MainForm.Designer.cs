/*
 * Created by SharpDevelop.
 * User: szilard
 * Date: 2019-07-02
 * Time: 9:16 AM
 * 
 * To change this template use Tools | Options | Coding | Edit Standard Headers.
 */
namespace Highway_decision_tester
{
	partial class MainForm
	{
		/// <summary>
		/// Designer variable used to keep track of non-visual components.
		/// </summary>
		private System.ComponentModel.IContainer components = null;
		private System.Windows.Forms.RadioButton rb_LeftLane;
		private System.Windows.Forms.GroupBox gb_my_car_pos;
		private System.Windows.Forms.RadioButton rb_RightLane;
		private System.Windows.Forms.RadioButton rb_MidLane;
		private System.Windows.Forms.Label Lb_lane_line;
		private System.Windows.Forms.HScrollBar hsb_LeftLane;
		private System.Windows.Forms.HScrollBar hsb_MidLane;
		private System.Windows.Forms.Label label1;
		private System.Windows.Forms.HScrollBar hsb_RightLane;
		private System.Windows.Forms.Label label2;
		private System.Windows.Forms.Label label3;
		private System.Windows.Forms.TextBox tb_LeftLane_speed;
		private System.Windows.Forms.Label lbl_mph_ll;
		private System.Windows.Forms.Label label4;
		private System.Windows.Forms.TextBox tb_MidLane_speed;
		private System.Windows.Forms.Label label5;
		private System.Windows.Forms.TextBox tb_RightLane_speed;
		private System.Windows.Forms.Label lbl_LeftLane_dist;
		private System.Windows.Forms.Label lbl_MidLane_dist;
		private System.Windows.Forms.Label lbl_RightLane_dist;
		private System.Windows.Forms.GroupBox gp_pred;
		private System.Windows.Forms.Button bt_RightLane_pred;
		private System.Windows.Forms.Button bt_LeftLane_pred;
		private System.Windows.Forms.Button bt_MidLane_pred;
		private System.Windows.Forms.Button bt_get_pred;
		private System.Windows.Forms.Button bt_step;
		private System.Windows.Forms.Label label6;
		private System.Windows.Forms.TextBox tb_my_vel;
		private System.Windows.Forms.Label label7;
		private System.Windows.Forms.RichTextBox rtb_Pred_results;
		private System.Windows.Forms.Button bt_One_step_back;
		
		/// <summary>
		/// Disposes resources used by the form.
		/// </summary>
		/// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
		protected override void Dispose(bool disposing)
		{
			if (disposing) {
				if (components != null) {
					components.Dispose();
				}
			}
			base.Dispose(disposing);
		}
		
		/// <summary>
		/// This method is required for Windows Forms designer support.
		/// Do not change the method contents inside the source code editor. The Forms designer might
		/// not be able to load this method if it was changed manually.
		/// </summary>
		private void InitializeComponent()
		{
			this.rb_LeftLane = new System.Windows.Forms.RadioButton();
			this.gb_my_car_pos = new System.Windows.Forms.GroupBox();
			this.rb_RightLane = new System.Windows.Forms.RadioButton();
			this.rb_MidLane = new System.Windows.Forms.RadioButton();
			this.Lb_lane_line = new System.Windows.Forms.Label();
			this.hsb_LeftLane = new System.Windows.Forms.HScrollBar();
			this.hsb_MidLane = new System.Windows.Forms.HScrollBar();
			this.label1 = new System.Windows.Forms.Label();
			this.hsb_RightLane = new System.Windows.Forms.HScrollBar();
			this.label2 = new System.Windows.Forms.Label();
			this.label3 = new System.Windows.Forms.Label();
			this.tb_LeftLane_speed = new System.Windows.Forms.TextBox();
			this.lbl_mph_ll = new System.Windows.Forms.Label();
			this.label4 = new System.Windows.Forms.Label();
			this.tb_MidLane_speed = new System.Windows.Forms.TextBox();
			this.label5 = new System.Windows.Forms.Label();
			this.tb_RightLane_speed = new System.Windows.Forms.TextBox();
			this.lbl_LeftLane_dist = new System.Windows.Forms.Label();
			this.lbl_MidLane_dist = new System.Windows.Forms.Label();
			this.lbl_RightLane_dist = new System.Windows.Forms.Label();
			this.gp_pred = new System.Windows.Forms.GroupBox();
			this.bt_RightLane_pred = new System.Windows.Forms.Button();
			this.bt_LeftLane_pred = new System.Windows.Forms.Button();
			this.bt_MidLane_pred = new System.Windows.Forms.Button();
			this.bt_get_pred = new System.Windows.Forms.Button();
			this.bt_step = new System.Windows.Forms.Button();
			this.label6 = new System.Windows.Forms.Label();
			this.tb_my_vel = new System.Windows.Forms.TextBox();
			this.label7 = new System.Windows.Forms.Label();
			this.rtb_Pred_results = new System.Windows.Forms.RichTextBox();
			this.bt_One_step_back = new System.Windows.Forms.Button();
			this.gb_my_car_pos.SuspendLayout();
			this.gp_pred.SuspendLayout();
			this.SuspendLayout();
			// 
			// rb_LeftLane
			// 
			this.rb_LeftLane.Location = new System.Drawing.Point(25, 25);
			this.rb_LeftLane.Name = "rb_LeftLane";
			this.rb_LeftLane.Size = new System.Drawing.Size(21, 24);
			this.rb_LeftLane.TabIndex = 3;
			this.rb_LeftLane.UseVisualStyleBackColor = true;
			this.rb_LeftLane.CheckedChanged += new System.EventHandler(this.Rb_LeftLaneCheckedChanged);
			// 
			// gb_my_car_pos
			// 
			this.gb_my_car_pos.Controls.Add(this.rb_RightLane);
			this.gb_my_car_pos.Controls.Add(this.rb_MidLane);
			this.gb_my_car_pos.Controls.Add(this.rb_LeftLane);
			this.gb_my_car_pos.Font = new System.Drawing.Font("Microsoft Sans Serif", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
			this.gb_my_car_pos.Location = new System.Drawing.Point(12, 12);
			this.gb_my_car_pos.Name = "gb_my_car_pos";
			this.gb_my_car_pos.Size = new System.Drawing.Size(74, 186);
			this.gb_my_car_pos.TabIndex = 4;
			this.gb_my_car_pos.TabStop = false;
			this.gb_my_car_pos.Text = "My pos";
			// 
			// rb_RightLane
			// 
			this.rb_RightLane.Location = new System.Drawing.Point(25, 138);
			this.rb_RightLane.Name = "rb_RightLane";
			this.rb_RightLane.Size = new System.Drawing.Size(21, 24);
			this.rb_RightLane.TabIndex = 5;
			this.rb_RightLane.UseVisualStyleBackColor = true;
			this.rb_RightLane.CheckedChanged += new System.EventHandler(this.Rb_RightLaneCheckedChanged);
			// 
			// rb_MidLane
			// 
			this.rb_MidLane.Checked = true;
			this.rb_MidLane.Location = new System.Drawing.Point(25, 81);
			this.rb_MidLane.Name = "rb_MidLane";
			this.rb_MidLane.Size = new System.Drawing.Size(21, 24);
			this.rb_MidLane.TabIndex = 4;
			this.rb_MidLane.TabStop = true;
			this.rb_MidLane.UseVisualStyleBackColor = true;
			this.rb_MidLane.CheckedChanged += new System.EventHandler(this.Rb_MidLaneCheckedChanged);
			// 
			// Lb_lane_line
			// 
			this.Lb_lane_line.Font = new System.Drawing.Font("Microsoft Sans Serif", 40F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
			this.Lb_lane_line.Location = new System.Drawing.Point(209, 40);
			this.Lb_lane_line.Name = "Lb_lane_line";
			this.Lb_lane_line.Size = new System.Drawing.Size(411, 77);
			this.Lb_lane_line.TabIndex = 5;
			this.Lb_lane_line.Text = "- - - - - - - - - - - - ";
			// 
			// hsb_LeftLane
			// 
			this.hsb_LeftLane.Location = new System.Drawing.Point(341, 34);
			this.hsb_LeftLane.Minimum = 1;
			this.hsb_LeftLane.Name = "hsb_LeftLane";
			this.hsb_LeftLane.Size = new System.Drawing.Size(272, 30);
			this.hsb_LeftLane.TabIndex = 6;
			this.hsb_LeftLane.Value = 99;
			this.hsb_LeftLane.Scroll += new System.Windows.Forms.ScrollEventHandler(this.HSB_Left_laneScroll);
			// 
			// hsb_MidLane
			// 
			this.hsb_MidLane.Location = new System.Drawing.Point(341, 87);
			this.hsb_MidLane.Minimum = 1;
			this.hsb_MidLane.Name = "hsb_MidLane";
			this.hsb_MidLane.Size = new System.Drawing.Size(272, 30);
			this.hsb_MidLane.TabIndex = 8;
			this.hsb_MidLane.Value = 99;
			this.hsb_MidLane.Scroll += new System.Windows.Forms.ScrollEventHandler(this.Hsb_mid_laneScroll);
			// 
			// label1
			// 
			this.label1.Font = new System.Drawing.Font("Microsoft Sans Serif", 40F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
			this.label1.Location = new System.Drawing.Point(209, 93);
			this.label1.Name = "label1";
			this.label1.Size = new System.Drawing.Size(411, 77);
			this.label1.TabIndex = 7;
			this.label1.Text = "- - - - - - - - - - - - ";
			// 
			// hsb_RightLane
			// 
			this.hsb_RightLane.Location = new System.Drawing.Point(341, 140);
			this.hsb_RightLane.Minimum = 1;
			this.hsb_RightLane.Name = "hsb_RightLane";
			this.hsb_RightLane.Size = new System.Drawing.Size(272, 30);
			this.hsb_RightLane.TabIndex = 10;
			this.hsb_RightLane.Value = 99;
			this.hsb_RightLane.Scroll += new System.Windows.Forms.ScrollEventHandler(this.Hsb_right_laneScroll);
			// 
			// label2
			// 
			this.label2.Font = new System.Drawing.Font("Microsoft Sans Serif", 40F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
			this.label2.Location = new System.Drawing.Point(209, 145);
			this.label2.Name = "label2";
			this.label2.Size = new System.Drawing.Size(404, 77);
			this.label2.TabIndex = 9;
			this.label2.Text = "- - - - - - - - - - - - ";
			// 
			// label3
			// 
			this.label3.Font = new System.Drawing.Font("Microsoft Sans Serif", 40F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
			this.label3.Location = new System.Drawing.Point(209, 3);
			this.label3.Name = "label3";
			this.label3.Size = new System.Drawing.Size(435, 77);
			this.label3.TabIndex = 11;
			this.label3.Text = "- - - - - - - - - - - - ";
			// 
			// tb_LeftLane_speed
			// 
			this.tb_LeftLane_speed.Font = new System.Drawing.Font("Microsoft Sans Serif", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
			this.tb_LeftLane_speed.Location = new System.Drawing.Point(220, 38);
			this.tb_LeftLane_speed.Name = "tb_LeftLane_speed";
			this.tb_LeftLane_speed.Size = new System.Drawing.Size(62, 26);
			this.tb_LeftLane_speed.TabIndex = 12;
			this.tb_LeftLane_speed.TextChanged += new System.EventHandler(this.Tb_Left_lane_speedTextChanged);
			// 
			// lbl_mph_ll
			// 
			this.lbl_mph_ll.Font = new System.Drawing.Font("Microsoft Sans Serif", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
			this.lbl_mph_ll.Location = new System.Drawing.Point(281, 38);
			this.lbl_mph_ll.Name = "lbl_mph_ll";
			this.lbl_mph_ll.Size = new System.Drawing.Size(57, 23);
			this.lbl_mph_ll.TabIndex = 13;
			this.lbl_mph_ll.Text = "mph";
			// 
			// label4
			// 
			this.label4.Font = new System.Drawing.Font("Microsoft Sans Serif", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
			this.label4.Location = new System.Drawing.Point(281, 100);
			this.label4.Name = "label4";
			this.label4.Size = new System.Drawing.Size(50, 23);
			this.label4.TabIndex = 15;
			this.label4.Text = "mph";
			// 
			// tb_MidLane_speed
			// 
			this.tb_MidLane_speed.Font = new System.Drawing.Font("Microsoft Sans Serif", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
			this.tb_MidLane_speed.Location = new System.Drawing.Point(220, 97);
			this.tb_MidLane_speed.Name = "tb_MidLane_speed";
			this.tb_MidLane_speed.Size = new System.Drawing.Size(62, 26);
			this.tb_MidLane_speed.TabIndex = 14;
			this.tb_MidLane_speed.TextChanged += new System.EventHandler(this.Tb_Mid_lane_speedTextChanged);
			// 
			// label5
			// 
			this.label5.Font = new System.Drawing.Font("Microsoft Sans Serif", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
			this.label5.Location = new System.Drawing.Point(281, 148);
			this.label5.Name = "label5";
			this.label5.Size = new System.Drawing.Size(57, 23);
			this.label5.TabIndex = 17;
			this.label5.Text = "mph";
			// 
			// tb_RightLane_speed
			// 
			this.tb_RightLane_speed.Font = new System.Drawing.Font("Microsoft Sans Serif", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
			this.tb_RightLane_speed.Location = new System.Drawing.Point(220, 145);
			this.tb_RightLane_speed.Name = "tb_RightLane_speed";
			this.tb_RightLane_speed.Size = new System.Drawing.Size(62, 26);
			this.tb_RightLane_speed.TabIndex = 16;
			this.tb_RightLane_speed.TextChanged += new System.EventHandler(this.Tb_Right_lane_speedTextChanged);
			// 
			// lbl_LeftLane_dist
			// 
			this.lbl_LeftLane_dist.Font = new System.Drawing.Font("Microsoft Sans Serif", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
			this.lbl_LeftLane_dist.Location = new System.Drawing.Point(626, 38);
			this.lbl_LeftLane_dist.Name = "lbl_LeftLane_dist";
			this.lbl_LeftLane_dist.Size = new System.Drawing.Size(57, 23);
			this.lbl_LeftLane_dist.TabIndex = 18;
			this.lbl_LeftLane_dist.Text = "00 m";
			// 
			// lbl_MidLane_dist
			// 
			this.lbl_MidLane_dist.Font = new System.Drawing.Font("Microsoft Sans Serif", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
			this.lbl_MidLane_dist.Location = new System.Drawing.Point(626, 87);
			this.lbl_MidLane_dist.Name = "lbl_MidLane_dist";
			this.lbl_MidLane_dist.Size = new System.Drawing.Size(57, 23);
			this.lbl_MidLane_dist.TabIndex = 19;
			this.lbl_MidLane_dist.Text = "00 m";
			// 
			// lbl_RightLane_dist
			// 
			this.lbl_RightLane_dist.Font = new System.Drawing.Font("Microsoft Sans Serif", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
			this.lbl_RightLane_dist.Location = new System.Drawing.Point(626, 145);
			this.lbl_RightLane_dist.Name = "lbl_RightLane_dist";
			this.lbl_RightLane_dist.Size = new System.Drawing.Size(57, 23);
			this.lbl_RightLane_dist.TabIndex = 20;
			this.lbl_RightLane_dist.Text = "00 m";
			// 
			// gp_pred
			// 
			this.gp_pred.Controls.Add(this.bt_RightLane_pred);
			this.gp_pred.Controls.Add(this.bt_LeftLane_pred);
			this.gp_pred.Controls.Add(this.bt_MidLane_pred);
			this.gp_pred.Font = new System.Drawing.Font("Microsoft Sans Serif", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
			this.gp_pred.Location = new System.Drawing.Point(92, 12);
			this.gp_pred.Name = "gp_pred";
			this.gp_pred.Size = new System.Drawing.Size(111, 186);
			this.gp_pred.TabIndex = 6;
			this.gp_pred.TabStop = false;
			this.gp_pred.Text = "pred";
			// 
			// bt_RightLane_pred
			// 
			this.bt_RightLane_pred.Font = new System.Drawing.Font("Microsoft Sans Serif", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
			this.bt_RightLane_pred.Location = new System.Drawing.Point(3, 132);
			this.bt_RightLane_pred.Name = "bt_RightLane_pred";
			this.bt_RightLane_pred.Size = new System.Drawing.Size(102, 30);
			this.bt_RightLane_pred.TabIndex = 23;
			this.bt_RightLane_pred.Text = "Right Lane";
			this.bt_RightLane_pred.UseVisualStyleBackColor = true;
			// 
			// bt_LeftLane_pred
			// 
			this.bt_LeftLane_pred.Font = new System.Drawing.Font("Microsoft Sans Serif", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
			this.bt_LeftLane_pred.Location = new System.Drawing.Point(3, 25);
			this.bt_LeftLane_pred.Name = "bt_LeftLane_pred";
			this.bt_LeftLane_pred.Size = new System.Drawing.Size(102, 30);
			this.bt_LeftLane_pred.TabIndex = 21;
			this.bt_LeftLane_pred.Text = "Left Lane";
			this.bt_LeftLane_pred.UseVisualStyleBackColor = true;
			// 
			// bt_MidLane_pred
			// 
			this.bt_MidLane_pred.Font = new System.Drawing.Font("Microsoft Sans Serif", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
			this.bt_MidLane_pred.Location = new System.Drawing.Point(3, 83);
			this.bt_MidLane_pred.Name = "bt_MidLane_pred";
			this.bt_MidLane_pred.Size = new System.Drawing.Size(102, 30);
			this.bt_MidLane_pred.TabIndex = 22;
			this.bt_MidLane_pred.Text = "Mid Lane";
			this.bt_MidLane_pred.UseVisualStyleBackColor = true;
			// 
			// bt_get_pred
			// 
			this.bt_get_pred.Font = new System.Drawing.Font("Microsoft Sans Serif", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
			this.bt_get_pred.Location = new System.Drawing.Point(686, 12);
			this.bt_get_pred.Name = "bt_get_pred";
			this.bt_get_pred.Size = new System.Drawing.Size(92, 68);
			this.bt_get_pred.TabIndex = 21;
			this.bt_get_pred.Text = "Get Prediction";
			this.bt_get_pred.UseVisualStyleBackColor = true;
			this.bt_get_pred.Click += new System.EventHandler(this.Bt_get_predClick);
			// 
			// bt_step
			// 
			this.bt_step.Font = new System.Drawing.Font("Microsoft Sans Serif", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
			this.bt_step.Location = new System.Drawing.Point(686, 86);
			this.bt_step.Name = "bt_step";
			this.bt_step.Size = new System.Drawing.Size(92, 68);
			this.bt_step.TabIndex = 22;
			this.bt_step.Text = "One Step";
			this.bt_step.UseVisualStyleBackColor = true;
			this.bt_step.Click += new System.EventHandler(this.Bt_stepClick);
			// 
			// label6
			// 
			this.label6.Font = new System.Drawing.Font("Microsoft Sans Serif", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
			this.label6.Location = new System.Drawing.Point(140, 207);
			this.label6.Name = "label6";
			this.label6.Size = new System.Drawing.Size(57, 23);
			this.label6.TabIndex = 24;
			this.label6.Text = "mph";
			// 
			// tb_my_vel
			// 
			this.tb_my_vel.Font = new System.Drawing.Font("Microsoft Sans Serif", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
			this.tb_my_vel.Location = new System.Drawing.Point(75, 204);
			this.tb_my_vel.Name = "tb_my_vel";
			this.tb_my_vel.Size = new System.Drawing.Size(62, 26);
			this.tb_my_vel.TabIndex = 23;
			this.tb_my_vel.TextChanged += new System.EventHandler(this.Tb_my_velTextChanged);
			// 
			// label7
			// 
			this.label7.Font = new System.Drawing.Font("Microsoft Sans Serif", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
			this.label7.Location = new System.Drawing.Point(12, 207);
			this.label7.Name = "label7";
			this.label7.Size = new System.Drawing.Size(57, 23);
			this.label7.TabIndex = 25;
			this.label7.Text = "My vel";
			// 
			// rtb_Pred_results
			// 
			this.rtb_Pred_results.Font = new System.Drawing.Font("Microsoft Sans Serif", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
			this.rtb_Pred_results.Location = new System.Drawing.Point(13, 234);
			this.rtb_Pred_results.Name = "rtb_Pred_results";
			this.rtb_Pred_results.Size = new System.Drawing.Size(765, 283);
			this.rtb_Pred_results.TabIndex = 26;
			this.rtb_Pred_results.Text = "";
			// 
			// bt_One_step_back
			// 
			this.bt_One_step_back.Font = new System.Drawing.Font("Microsoft Sans Serif", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
			this.bt_One_step_back.Location = new System.Drawing.Point(686, 160);
			this.bt_One_step_back.Name = "bt_One_step_back";
			this.bt_One_step_back.Size = new System.Drawing.Size(92, 68);
			this.bt_One_step_back.TabIndex = 27;
			this.bt_One_step_back.Text = "One Step Back";
			this.bt_One_step_back.UseVisualStyleBackColor = true;
			this.bt_One_step_back.Click += new System.EventHandler(this.Bt_One_step_backClick);
			// 
			// MainForm
			// 
			this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
			this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
			this.BackColor = System.Drawing.SystemColors.ActiveCaption;
			this.ClientSize = new System.Drawing.Size(790, 529);
			this.Controls.Add(this.bt_One_step_back);
			this.Controls.Add(this.rtb_Pred_results);
			this.Controls.Add(this.label7);
			this.Controls.Add(this.label6);
			this.Controls.Add(this.tb_my_vel);
			this.Controls.Add(this.bt_step);
			this.Controls.Add(this.bt_get_pred);
			this.Controls.Add(this.gp_pred);
			this.Controls.Add(this.lbl_RightLane_dist);
			this.Controls.Add(this.lbl_MidLane_dist);
			this.Controls.Add(this.lbl_LeftLane_dist);
			this.Controls.Add(this.label5);
			this.Controls.Add(this.tb_RightLane_speed);
			this.Controls.Add(this.label4);
			this.Controls.Add(this.tb_MidLane_speed);
			this.Controls.Add(this.lbl_mph_ll);
			this.Controls.Add(this.tb_LeftLane_speed);
			this.Controls.Add(this.hsb_RightLane);
			this.Controls.Add(this.label2);
			this.Controls.Add(this.hsb_MidLane);
			this.Controls.Add(this.label1);
			this.Controls.Add(this.hsb_LeftLane);
			this.Controls.Add(this.Lb_lane_line);
			this.Controls.Add(this.gb_my_car_pos);
			this.Controls.Add(this.label3);
			this.Name = "MainForm";
			this.Text = "Highway_decision_tester";
			this.gb_my_car_pos.ResumeLayout(false);
			this.gp_pred.ResumeLayout(false);
			this.ResumeLayout(false);
			this.PerformLayout();

		}
	}
}
