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
		private System.Windows.Forms.Button button3;
		private System.Windows.Forms.Button button1;
		private System.Windows.Forms.Button button2;
		
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
			this.button1 = new System.Windows.Forms.Button();
			this.button2 = new System.Windows.Forms.Button();
			this.button3 = new System.Windows.Forms.Button();
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
			this.hsb_LeftLane.Name = "hsb_LeftLane";
			this.hsb_LeftLane.Size = new System.Drawing.Size(272, 30);
			this.hsb_LeftLane.TabIndex = 6;
			this.hsb_LeftLane.Value = 99;
			this.hsb_LeftLane.Scroll += new System.Windows.Forms.ScrollEventHandler(this.HSB_Left_laneScroll);
			// 
			// hsb_MidLane
			// 
			this.hsb_MidLane.Location = new System.Drawing.Point(341, 87);
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
			this.gp_pred.Controls.Add(this.button3);
			this.gp_pred.Controls.Add(this.button1);
			this.gp_pred.Controls.Add(this.button2);
			this.gp_pred.Font = new System.Drawing.Font("Microsoft Sans Serif", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
			this.gp_pred.Location = new System.Drawing.Point(92, 12);
			this.gp_pred.Name = "gp_pred";
			this.gp_pred.Size = new System.Drawing.Size(111, 186);
			this.gp_pred.TabIndex = 6;
			this.gp_pred.TabStop = false;
			this.gp_pred.Text = "pred";
			// 
			// button1
			// 
			this.button1.Font = new System.Drawing.Font("Microsoft Sans Serif", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
			this.button1.Location = new System.Drawing.Point(3, 25);
			this.button1.Name = "button1";
			this.button1.Size = new System.Drawing.Size(102, 30);
			this.button1.TabIndex = 21;
			this.button1.Text = "Left Lane";
			this.button1.UseVisualStyleBackColor = true;
			// 
			// button2
			// 
			this.button2.Font = new System.Drawing.Font("Microsoft Sans Serif", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
			this.button2.Location = new System.Drawing.Point(3, 83);
			this.button2.Name = "button2";
			this.button2.Size = new System.Drawing.Size(102, 30);
			this.button2.TabIndex = 22;
			this.button2.Text = "Mid Lane";
			this.button2.UseVisualStyleBackColor = true;
			// 
			// button3
			// 
			this.button3.Font = new System.Drawing.Font("Microsoft Sans Serif", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
			this.button3.Location = new System.Drawing.Point(3, 132);
			this.button3.Name = "button3";
			this.button3.Size = new System.Drawing.Size(102, 30);
			this.button3.TabIndex = 23;
			this.button3.Text = "Right Lane";
			this.button3.UseVisualStyleBackColor = true;
			// 
			// MainForm
			// 
			this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
			this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
			this.BackColor = System.Drawing.SystemColors.ActiveCaption;
			this.ClientSize = new System.Drawing.Size(841, 231);
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
