namespace RatchetingInCsharp_10_3_15_2
{
    partial class Form1
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            System.Windows.Forms.DataVisualization.Charting.ChartArea chartArea1 = new System.Windows.Forms.DataVisualization.Charting.ChartArea();
            System.Windows.Forms.DataVisualization.Charting.Legend legend1 = new System.Windows.Forms.DataVisualization.Charting.Legend();
            System.Windows.Forms.DataVisualization.Charting.Series series1 = new System.Windows.Forms.DataVisualization.Charting.Series();
            this.label1 = new System.Windows.Forms.Label();
            this.txtInputNumberCycles = new System.Windows.Forms.TextBox();
            this.btnRunSimulation = new System.Windows.Forms.Button();
            this.chtDisplacement = new System.Windows.Forms.DataVisualization.Charting.Chart();
            this.pbarProgress = new System.Windows.Forms.ProgressBar();
            this.txtXSteps = new System.Windows.Forms.TextBox();
            this.label3 = new System.Windows.Forms.Label();
            this.label4 = new System.Windows.Forms.Label();
            this.txtPointsPerCycle = new System.Windows.Forms.TextBox();
            this.label5 = new System.Windows.Forms.Label();
            this.txtH0Factor = new System.Windows.Forms.TextBox();
            this.label6 = new System.Windows.Forms.Label();
            this.txtSimulationWidth = new System.Windows.Forms.TextBox();
            this.txtSFactor = new System.Windows.Forms.TextBox();
            this.label7 = new System.Windows.Forms.Label();
            this.label8 = new System.Windows.Forms.Label();
            this.label9 = new System.Windows.Forms.Label();
            this.label10 = new System.Windows.Forms.Label();
            this.label11 = new System.Windows.Forms.Label();
            this.label12 = new System.Windows.Forms.Label();
            this.label13 = new System.Windows.Forms.Label();
            this.label14 = new System.Windows.Forms.Label();
            this.txtAlphaS = new System.Windows.Forms.TextBox();
            this.label15 = new System.Windows.Forms.Label();
            this.txtAlphaM = new System.Windows.Forms.TextBox();
            this.label16 = new System.Windows.Forms.Label();
            this.txtTempHot = new System.Windows.Forms.TextBox();
            this.label17 = new System.Windows.Forms.Label();
            this.txtTempCold = new System.Windows.Forms.TextBox();
            this.label18 = new System.Windows.Forms.Label();
            this.txtEf = new System.Windows.Forms.TextBox();
            this.label19 = new System.Windows.Forms.Label();
            this.txtNuF = new System.Windows.Forms.TextBox();
            this.label20 = new System.Windows.Forms.Label();
            this.txtEm = new System.Windows.Forms.TextBox();
            this.label21 = new System.Windows.Forms.Label();
            this.txtNuM = new System.Windows.Forms.TextBox();
            this.label22 = new System.Windows.Forms.Label();
            this.txtYield = new System.Windows.Forms.TextBox();
            this.rbnSaveOutput = new System.Windows.Forms.RadioButton();
            this.label2 = new System.Windows.Forms.Label();
            this.txtSigmaFactor = new System.Windows.Forms.TextBox();
            this.label23 = new System.Windows.Forms.Label();
            this.txtA0 = new System.Windows.Forms.TextBox();
            this.txth = new System.Windows.Forms.TextBox();
            this.label24 = new System.Windows.Forms.Label();
            ((System.ComponentModel.ISupportInitialize)(this.chtDisplacement)).BeginInit();
            this.SuspendLayout();
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(12, 7);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(149, 13);
            this.label1.TabIndex = 0;
            this.label1.Text = "Number of Cycles (default = 1)";
            // 
            // txtInputNumberCycles
            // 
            this.txtInputNumberCycles.Location = new System.Drawing.Point(15, 23);
            this.txtInputNumberCycles.Name = "txtInputNumberCycles";
            this.txtInputNumberCycles.Size = new System.Drawing.Size(100, 20);
            this.txtInputNumberCycles.TabIndex = 1;
            this.txtInputNumberCycles.Text = "1";
            // 
            // btnRunSimulation
            // 
            this.btnRunSimulation.Location = new System.Drawing.Point(591, 23);
            this.btnRunSimulation.Name = "btnRunSimulation";
            this.btnRunSimulation.Size = new System.Drawing.Size(118, 23);
            this.btnRunSimulation.TabIndex = 2;
            this.btnRunSimulation.Text = "Run Simulation";
            this.btnRunSimulation.UseVisualStyleBackColor = true;
            this.btnRunSimulation.Click += new System.EventHandler(this.btnRunSimulation_Click);
            // 
            // chtDisplacement
            // 
            chartArea1.Name = "ChartArea1";
            this.chtDisplacement.ChartAreas.Add(chartArea1);
            legend1.Name = "Legend1";
            this.chtDisplacement.Legends.Add(legend1);
            this.chtDisplacement.Location = new System.Drawing.Point(12, 65);
            this.chtDisplacement.Name = "chtDisplacement";
            series1.ChartArea = "ChartArea1";
            series1.ChartType = System.Windows.Forms.DataVisualization.Charting.SeriesChartType.Line;
            series1.Legend = "Legend1";
            series1.Name = "Displacement (um)";
            this.chtDisplacement.Series.Add(series1);
            this.chtDisplacement.Size = new System.Drawing.Size(694, 422);
            this.chtDisplacement.TabIndex = 3;
            this.chtDisplacement.Text = "chart1";
            // 
            // pbarProgress
            // 
            this.pbarProgress.Location = new System.Drawing.Point(12, 512);
            this.pbarProgress.Name = "pbarProgress";
            this.pbarProgress.Size = new System.Drawing.Size(694, 23);
            this.pbarProgress.TabIndex = 4;
            // 
            // txtXSteps
            // 
            this.txtXSteps.Location = new System.Drawing.Point(23, 589);
            this.txtXSteps.Name = "txtXSteps";
            this.txtXSteps.Size = new System.Drawing.Size(51, 20);
            this.txtXSteps.TabIndex = 6;
            this.txtXSteps.Text = "201";
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.Location = new System.Drawing.Point(20, 573);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(94, 13);
            this.label3.TabIndex = 7;
            this.label3.Text = "Number of x Steps";
            // 
            // label4
            // 
            this.label4.AutoSize = true;
            this.label4.Location = new System.Drawing.Point(746, 187);
            this.label4.Name = "label4";
            this.label4.Size = new System.Drawing.Size(84, 13);
            this.label4.TabIndex = 8;
            this.label4.Text = "Points Per Cycle";
            // 
            // txtPointsPerCycle
            // 
            this.txtPointsPerCycle.Location = new System.Drawing.Point(748, 218);
            this.txtPointsPerCycle.Name = "txtPointsPerCycle";
            this.txtPointsPerCycle.Size = new System.Drawing.Size(92, 20);
            this.txtPointsPerCycle.TabIndex = 9;
            this.txtPointsPerCycle.Text = "10000";
            // 
            // label5
            // 
            this.label5.AutoSize = true;
            this.label5.Location = new System.Drawing.Point(303, 573);
            this.label5.Name = "label5";
            this.label5.Size = new System.Drawing.Size(65, 13);
            this.label5.TabIndex = 10;
            this.label5.Text = "Factor H0/h";
            // 
            // txtH0Factor
            // 
            this.txtH0Factor.Location = new System.Drawing.Point(305, 589);
            this.txtH0Factor.Name = "txtH0Factor";
            this.txtH0Factor.Size = new System.Drawing.Size(63, 20);
            this.txtH0Factor.TabIndex = 11;
            this.txtH0Factor.Text = "10.";
            // 
            // label6
            // 
            this.label6.AutoSize = true;
            this.label6.Location = new System.Drawing.Point(152, 573);
            this.label6.Name = "label6";
            this.label6.Size = new System.Drawing.Size(109, 13);
            this.label6.TabIndex = 12;
            this.label6.Text = "Simulation Width (um)";
            // 
            // txtSimulationWidth
            // 
            this.txtSimulationWidth.Location = new System.Drawing.Point(155, 589);
            this.txtSimulationWidth.Name = "txtSimulationWidth";
            this.txtSimulationWidth.Size = new System.Drawing.Size(80, 20);
            this.txtSimulationWidth.TabIndex = 13;
            this.txtSimulationWidth.Text = "200";
            // 
            // txtSFactor
            // 
            this.txtSFactor.Location = new System.Drawing.Point(197, 23);
            this.txtSFactor.Name = "txtSFactor";
            this.txtSFactor.Size = new System.Drawing.Size(56, 20);
            this.txtSFactor.TabIndex = 14;
            this.txtSFactor.Text = "0.";
            // 
            // label7
            // 
            this.label7.AutoSize = true;
            this.label7.Location = new System.Drawing.Point(194, 7);
            this.label7.Name = "label7";
            this.label7.Size = new System.Drawing.Size(86, 13);
            this.label7.TabIndex = 15;
            this.label7.Text = "S factor (0 to 10)";
            // 
            // label8
            // 
            this.label8.AutoSize = true;
            this.label8.Location = new System.Drawing.Point(259, 28);
            this.label8.Name = "label8";
            this.label8.Size = new System.Drawing.Size(266, 13);
            this.label8.TabIndex = 16;
            this.label8.Text = "*Higher value dampens displacement in upper direction";
            // 
            // label9
            // 
            this.label9.AutoSize = true;
            this.label9.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle;
            this.label9.Location = new System.Drawing.Point(24, 545);
            this.label9.Name = "label9";
            this.label9.Size = new System.Drawing.Size(113, 15);
            this.label9.TabIndex = 17;
            this.label9.Text = "Simulation Parameters";
            // 
            // label10
            // 
            this.label10.AutoSize = true;
            this.label10.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle;
            this.label10.Location = new System.Drawing.Point(24, 625);
            this.label10.Name = "label10";
            this.label10.Size = new System.Drawing.Size(96, 15);
            this.label10.TabIndex = 18;
            this.label10.Text = "Material Properties";
            // 
            // label11
            // 
            this.label11.AutoSize = true;
            this.label11.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle;
            this.label11.Location = new System.Drawing.Point(179, 625);
            this.label11.Name = "label11";
            this.label11.Size = new System.Drawing.Size(27, 15);
            this.label11.TabIndex = 19;
            this.label11.Text = "Film";
            // 
            // label12
            // 
            this.label12.AutoSize = true;
            this.label12.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle;
            this.label12.Location = new System.Drawing.Point(355, 625);
            this.label12.Name = "label12";
            this.label12.Size = new System.Drawing.Size(35, 15);
            this.label12.TabIndex = 20;
            this.label12.Text = "Metal";
            // 
            // label13
            // 
            this.label13.AutoSize = true;
            this.label13.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle;
            this.label13.Location = new System.Drawing.Point(533, 625);
            this.label13.Name = "label13";
            this.label13.Size = new System.Drawing.Size(54, 15);
            this.label13.TabIndex = 21;
            this.label13.Text = "Substrate";
            // 
            // label14
            // 
            this.label14.AutoSize = true;
            this.label14.Location = new System.Drawing.Point(530, 646);
            this.label14.Name = "label14";
            this.label14.Size = new System.Drawing.Size(162, 13);
            this.label14.TabIndex = 22;
            this.label14.Text = "Coefficient of Thermal Expansion";
            // 
            // txtAlphaS
            // 
            this.txtAlphaS.Location = new System.Drawing.Point(533, 662);
            this.txtAlphaS.Name = "txtAlphaS";
            this.txtAlphaS.Size = new System.Drawing.Size(100, 20);
            this.txtAlphaS.TabIndex = 23;
            this.txtAlphaS.Text = "0.000014";
            // 
            // label15
            // 
            this.label15.AutoSize = true;
            this.label15.Location = new System.Drawing.Point(352, 742);
            this.label15.Name = "label15";
            this.label15.Size = new System.Drawing.Size(162, 13);
            this.label15.TabIndex = 24;
            this.label15.Text = "Coefficient of Thermal Expansion";
            // 
            // txtAlphaM
            // 
            this.txtAlphaM.Location = new System.Drawing.Point(355, 758);
            this.txtAlphaM.Name = "txtAlphaM";
            this.txtAlphaM.Size = new System.Drawing.Size(100, 20);
            this.txtAlphaM.TabIndex = 25;
            this.txtAlphaM.Text = "0.000024";
            // 
            // label16
            // 
            this.label16.AutoSize = true;
            this.label16.Location = new System.Drawing.Point(656, 573);
            this.label16.Name = "label16";
            this.label16.Size = new System.Drawing.Size(103, 13);
            this.label16.TabIndex = 26;
            this.label16.Text = "Hot Temperature (C)";
            // 
            // txtTempHot
            // 
            this.txtTempHot.Location = new System.Drawing.Point(659, 589);
            this.txtTempHot.Name = "txtTempHot";
            this.txtTempHot.Size = new System.Drawing.Size(100, 20);
            this.txtTempHot.TabIndex = 27;
            this.txtTempHot.Text = "90.";
            // 
            // label17
            // 
            this.label17.AutoSize = true;
            this.label17.Location = new System.Drawing.Point(528, 573);
            this.label17.Name = "label17";
            this.label17.Size = new System.Drawing.Size(107, 13);
            this.label17.TabIndex = 28;
            this.label17.Text = "Cold Temperature (C)";
            // 
            // txtTempCold
            // 
            this.txtTempCold.Location = new System.Drawing.Point(531, 589);
            this.txtTempCold.Name = "txtTempCold";
            this.txtTempCold.Size = new System.Drawing.Size(100, 20);
            this.txtTempCold.TabIndex = 29;
            this.txtTempCold.Text = "-10.";
            // 
            // label18
            // 
            this.label18.AutoSize = true;
            this.label18.Location = new System.Drawing.Point(176, 646);
            this.label18.Name = "label18";
            this.label18.Size = new System.Drawing.Size(119, 13);
            this.label18.TabIndex = 30;
            this.label18.Text = "Young\'s Modulus (MPa)";
            // 
            // txtEf
            // 
            this.txtEf.Location = new System.Drawing.Point(182, 662);
            this.txtEf.Name = "txtEf";
            this.txtEf.Size = new System.Drawing.Size(100, 20);
            this.txtEf.TabIndex = 31;
            this.txtEf.Text = "333000.";
            // 
            // label19
            // 
            this.label19.AutoSize = true;
            this.label19.Location = new System.Drawing.Point(176, 691);
            this.label19.Name = "label19";
            this.label19.Size = new System.Drawing.Size(79, 13);
            this.label19.TabIndex = 32;
            this.label19.Text = "Poisson\'s Ratio";
            // 
            // txtNuF
            // 
            this.txtNuF.Location = new System.Drawing.Point(182, 707);
            this.txtNuF.Name = "txtNuF";
            this.txtNuF.Size = new System.Drawing.Size(100, 20);
            this.txtNuF.TabIndex = 33;
            this.txtNuF.Text = "0.3";
            // 
            // label20
            // 
            this.label20.AutoSize = true;
            this.label20.Location = new System.Drawing.Point(352, 646);
            this.label20.Name = "label20";
            this.label20.Size = new System.Drawing.Size(88, 13);
            this.label20.TabIndex = 34;
            this.label20.Text = "Young\'s Modulus";
            // 
            // txtEm
            // 
            this.txtEm.Location = new System.Drawing.Point(355, 662);
            this.txtEm.Name = "txtEm";
            this.txtEm.Size = new System.Drawing.Size(100, 20);
            this.txtEm.TabIndex = 35;
            this.txtEm.Text = "200000.";
            // 
            // label21
            // 
            this.label21.AutoSize = true;
            this.label21.Location = new System.Drawing.Point(352, 691);
            this.label21.Name = "label21";
            this.label21.Size = new System.Drawing.Size(79, 13);
            this.label21.TabIndex = 36;
            this.label21.Text = "Poisson\'s Ratio";
            // 
            // txtNuM
            // 
            this.txtNuM.Location = new System.Drawing.Point(355, 707);
            this.txtNuM.Name = "txtNuM";
            this.txtNuM.Size = new System.Drawing.Size(100, 20);
            this.txtNuM.TabIndex = 37;
            this.txtNuM.Text = "0.25";
            // 
            // label22
            // 
            this.label22.AutoSize = true;
            this.label22.Location = new System.Drawing.Point(352, 790);
            this.label22.Name = "label22";
            this.label22.Size = new System.Drawing.Size(144, 13);
            this.label22.TabIndex = 38;
            this.label22.Text = "Uniaxial Yield Strength (MPa)";
            // 
            // txtYield
            // 
            this.txtYield.Location = new System.Drawing.Point(359, 809);
            this.txtYield.Name = "txtYield";
            this.txtYield.Size = new System.Drawing.Size(100, 20);
            this.txtYield.TabIndex = 39;
            this.txtYield.Text = "100.";
            // 
            // rbnSaveOutput
            // 
            this.rbnSaveOutput.AutoSize = true;
            this.rbnSaveOutput.Location = new System.Drawing.Point(748, 29);
            this.rbnSaveOutput.Name = "rbnSaveOutput";
            this.rbnSaveOutput.Size = new System.Drawing.Size(85, 17);
            this.rbnSaveOutput.TabIndex = 40;
            this.rbnSaveOutput.Text = "Save Output";
            this.rbnSaveOutput.UseVisualStyleBackColor = true;
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(414, 574);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(75, 13);
            this.label2.TabIndex = 41;
            this.label2.Text = "Factor Sigma0";
            // 
            // txtSigmaFactor
            // 
            this.txtSigmaFactor.BackColor = System.Drawing.SystemColors.Window;
            this.txtSigmaFactor.Location = new System.Drawing.Point(412, 590);
            this.txtSigmaFactor.Name = "txtSigmaFactor";
            this.txtSigmaFactor.ReadOnly = true;
            this.txtSigmaFactor.Size = new System.Drawing.Size(100, 20);
            this.txtSigmaFactor.TabIndex = 42;
            this.txtSigmaFactor.Text = "-0.014";
            // 
            // label23
            // 
            this.label23.AutoSize = true;
            this.label23.Location = new System.Drawing.Point(746, 502);
            this.label23.Name = "label23";
            this.label23.Size = new System.Drawing.Size(20, 13);
            this.label23.TabIndex = 43;
            this.label23.Text = "A0";
            // 
            // txtA0
            // 
            this.txtA0.Location = new System.Drawing.Point(748, 518);
            this.txtA0.Name = "txtA0";
            this.txtA0.Size = new System.Drawing.Size(100, 20);
            this.txtA0.TabIndex = 44;
            this.txtA0.Text = "0.01";
            // 
            // txth
            // 
            this.txth.Location = new System.Drawing.Point(749, 446);
            this.txth.Name = "txth";
            this.txth.Size = new System.Drawing.Size(100, 20);
            this.txth.TabIndex = 45;
            this.txth.Text = "1";
            // 
            // label24
            // 
            this.label24.AutoSize = true;
            this.label24.Location = new System.Drawing.Point(746, 430);
            this.label24.Name = "label24";
            this.label24.Size = new System.Drawing.Size(13, 13);
            this.label24.TabIndex = 46;
            this.label24.Text = "h";
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(903, 874);
            this.Controls.Add(this.label24);
            this.Controls.Add(this.txth);
            this.Controls.Add(this.txtA0);
            this.Controls.Add(this.label23);
            this.Controls.Add(this.txtSigmaFactor);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.rbnSaveOutput);
            this.Controls.Add(this.txtYield);
            this.Controls.Add(this.label22);
            this.Controls.Add(this.txtNuM);
            this.Controls.Add(this.label21);
            this.Controls.Add(this.txtEm);
            this.Controls.Add(this.label20);
            this.Controls.Add(this.txtNuF);
            this.Controls.Add(this.label19);
            this.Controls.Add(this.txtEf);
            this.Controls.Add(this.label18);
            this.Controls.Add(this.txtTempCold);
            this.Controls.Add(this.label17);
            this.Controls.Add(this.txtTempHot);
            this.Controls.Add(this.label16);
            this.Controls.Add(this.txtAlphaM);
            this.Controls.Add(this.label15);
            this.Controls.Add(this.txtAlphaS);
            this.Controls.Add(this.label14);
            this.Controls.Add(this.label13);
            this.Controls.Add(this.label12);
            this.Controls.Add(this.label11);
            this.Controls.Add(this.label10);
            this.Controls.Add(this.label9);
            this.Controls.Add(this.label8);
            this.Controls.Add(this.label7);
            this.Controls.Add(this.txtSFactor);
            this.Controls.Add(this.txtSimulationWidth);
            this.Controls.Add(this.label6);
            this.Controls.Add(this.txtH0Factor);
            this.Controls.Add(this.label5);
            this.Controls.Add(this.txtPointsPerCycle);
            this.Controls.Add(this.label4);
            this.Controls.Add(this.label3);
            this.Controls.Add(this.txtXSteps);
            this.Controls.Add(this.pbarProgress);
            this.Controls.Add(this.chtDisplacement);
            this.Controls.Add(this.btnRunSimulation);
            this.Controls.Add(this.txtInputNumberCycles);
            this.Controls.Add(this.label1);
            this.Name = "Form1";
            this.Text = "Ratcheting Simulator";
            ((System.ComponentModel.ISupportInitialize)(this.chtDisplacement)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.TextBox txtInputNumberCycles;
        private System.Windows.Forms.Button btnRunSimulation;
        private System.Windows.Forms.DataVisualization.Charting.Chart chtDisplacement;
        private System.Windows.Forms.ProgressBar pbarProgress;
        private System.Windows.Forms.TextBox txtXSteps;
        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.Label label4;
        private System.Windows.Forms.TextBox txtPointsPerCycle;
        private System.Windows.Forms.Label label5;
        private System.Windows.Forms.TextBox txtH0Factor;
        private System.Windows.Forms.Label label6;
        private System.Windows.Forms.TextBox txtSimulationWidth;
        private System.Windows.Forms.TextBox txtSFactor;
        private System.Windows.Forms.Label label7;
        private System.Windows.Forms.Label label8;
        private System.Windows.Forms.Label label9;
        private System.Windows.Forms.Label label10;
        private System.Windows.Forms.Label label11;
        private System.Windows.Forms.Label label12;
        private System.Windows.Forms.Label label13;
        private System.Windows.Forms.Label label14;
        private System.Windows.Forms.TextBox txtAlphaS;
        private System.Windows.Forms.Label label15;
        private System.Windows.Forms.TextBox txtAlphaM;
        private System.Windows.Forms.Label label16;
        private System.Windows.Forms.TextBox txtTempHot;
        private System.Windows.Forms.Label label17;
        private System.Windows.Forms.TextBox txtTempCold;
        private System.Windows.Forms.Label label18;
        private System.Windows.Forms.TextBox txtEf;
        private System.Windows.Forms.Label label19;
        private System.Windows.Forms.TextBox txtNuF;
        private System.Windows.Forms.Label label20;
        private System.Windows.Forms.TextBox txtEm;
        private System.Windows.Forms.Label label21;
        private System.Windows.Forms.TextBox txtNuM;
        private System.Windows.Forms.Label label22;
        private System.Windows.Forms.TextBox txtYield;
        private System.Windows.Forms.RadioButton rbnSaveOutput;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.TextBox txtSigmaFactor;
        private System.Windows.Forms.Label label23;
        private System.Windows.Forms.TextBox txtA0;
        private System.Windows.Forms.TextBox txth;
        private System.Windows.Forms.Label label24;
    }
}

