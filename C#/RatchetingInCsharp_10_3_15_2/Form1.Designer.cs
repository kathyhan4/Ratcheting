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
            System.Windows.Forms.DataVisualization.Charting.ChartArea chartArea3 = new System.Windows.Forms.DataVisualization.Charting.ChartArea();
            System.Windows.Forms.DataVisualization.Charting.Legend legend3 = new System.Windows.Forms.DataVisualization.Charting.Legend();
            System.Windows.Forms.DataVisualization.Charting.Series series3 = new System.Windows.Forms.DataVisualization.Charting.Series();
            this.label1 = new System.Windows.Forms.Label();
            this.txtInputNumberCycles = new System.Windows.Forms.TextBox();
            this.btnRunSimulation = new System.Windows.Forms.Button();
            this.chtDisplacement = new System.Windows.Forms.DataVisualization.Charting.Chart();
            this.pbarProgress = new System.Windows.Forms.ProgressBar();
            ((System.ComponentModel.ISupportInitialize)(this.chtDisplacement)).BeginInit();
            this.SuspendLayout();
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(12, 7);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(90, 13);
            this.label1.TabIndex = 0;
            this.label1.Text = "Number of Cycles";
            // 
            // txtInputNumberCycles
            // 
            this.txtInputNumberCycles.Location = new System.Drawing.Point(15, 23);
            this.txtInputNumberCycles.Name = "txtInputNumberCycles";
            this.txtInputNumberCycles.Size = new System.Drawing.Size(100, 20);
            this.txtInputNumberCycles.TabIndex = 1;
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
            chartArea3.Name = "ChartArea1";
            this.chtDisplacement.ChartAreas.Add(chartArea3);
            legend3.Name = "Legend1";
            this.chtDisplacement.Legends.Add(legend3);
            this.chtDisplacement.Location = new System.Drawing.Point(15, 49);
            this.chtDisplacement.Name = "chtDisplacement";
            series3.ChartArea = "ChartArea1";
            series3.ChartType = System.Windows.Forms.DataVisualization.Charting.SeriesChartType.Line;
            series3.Legend = "Legend1";
            series3.Name = "Displacement (um)";
            this.chtDisplacement.Series.Add(series3);
            this.chtDisplacement.Size = new System.Drawing.Size(694, 422);
            this.chtDisplacement.TabIndex = 3;
            this.chtDisplacement.Text = "chart1";
            // 
            // pbarProgress
            // 
            this.pbarProgress.Location = new System.Drawing.Point(15, 477);
            this.pbarProgress.Name = "pbarProgress";
            this.pbarProgress.Size = new System.Drawing.Size(694, 23);
            this.pbarProgress.TabIndex = 4;
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(721, 512);
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
    }
}

