using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace RatchetingInCsharp_10_3_15_2
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void btnRunSimulation_Click(object sender, EventArgs e)
        {
            double h = 1; // film thickness in microns- this needs to be 1 and everything else is scaled to this

            // Simulation Constants
            int NumberCycles = 1;
            bool result = Int32.TryParse(txtInputNumberCycles.Text, out NumberCycles);
            if (result == false)
            {
                MessageBox.Show("Input must be an integer.");
                return;
            }    
            int xSteps = 201;
            int PointsPerCycle = 10000; // number of timepoints per cycle, higher number is slower, but should have more stable results
            double H0 = 10 * h; // initial thickness of metal in units of h
            double SimulationWidth = 200 * h; //will simulate a 200 um wide 
            double Sfactor = 0; // sets level of S (0, 0.1, 1, or 10) 
            
            // Material Properties Constants
            double Ef = 333000; // Young's modulus of elastic film in MPa
            double nu_f = 0.3; // Poisson's ratio of elastic film
            double sigma0 = -0.014*Ef; // Initial in plane bilateral stress in MPa, this is a guess
            double Em = 200000; // Young's modulus of the metal in MPa
            double nu_m = 0.25; // Poisson's ratio of the metal
            double alpha_m = 24e-6; // thermal coefficient of expansion of metal
            double alpha_s = 14e-6; // thermal coefficient of expansion of substrate, (would be Si, but Si is 2.4??e-6)
            double TH = 90.0; // temperature in C of max cycle temp
            double TL = -10.0; // temperature in C of min cycle temp
            double Y = 100.0; // uniaxial yield strength of metal in MPa
 
            // Simulation constants that you don't need to fiddle with
            double S = Sfactor * Ef; // Incorporates effect for elastic constraint values
            int Points = PointsPerCycle*NumberCycles; 
            double dT = 1 / Convert.ToDouble(PointsPerCycle); // timestep in units of cycles
            double deltax = (SimulationWidth / (xSteps-1));
            int timepointcount = 0;

            // Derived Constants
            double eta_R = Em/(12*(1-nu_m))*Math.Pow(((Em*(alpha_m-alpha_s)*(TH-TL)/(1-nu_m)/Y)-2),-1);
            double Df = Ef * Math.Pow(h,3)/(12*(1-Math.Pow(nu_f,2)));
            
            // Initial conditions constants
            double A0 = h * 0.01; // amplitude of initial perturbation
            double delta = h*20; // denominator of exponent for initial film height perturbatione your system undergoes ratcheting, 
            double Criteria = Em*(alpha_m-alpha_s)*(TH-TL)/((1-nu_m)*Y); // if this is more than 2 then the system will ratchet

            if (Criteria < 2)
            {
                MessageBox.Show("System will not ratchet.");
                return;
            }          
            //OutputCycles = [0,10,20,200]
            // initialize all lists to store cycle number and space dependent data
            double[] Outputw = new double[xSteps];
            double[] Outputux = new double[xSteps];
            double[] w = new double[xSteps];
            double[] ux = new double[xSteps];
            double[] taox = new double[xSteps];
            double[] Nxx = new double[xSteps];
            double[] p = new double[xSteps];
            double[] H = new double[xSteps];
            double[] w_past = new double[xSteps];
            double[] ux_past = new double[xSteps];
            double[] taox_past = new double[xSteps];
            double[] Nxx_past = new double[xSteps];
            double[] p_past = new double[xSteps];
            double[] H_past = new double[xSteps];
            


          
            for (int i = 0; i < xSteps; i++)
            {
                H[i] = H0;
                H_past[i] = H0;
            }    
   
            // Insert initial conditions for w and ux and solve for initial conditions of the others
            // ux initial conditions are zeros
            for (int i= 3; i < xSteps-3; i++)
            {
                w_past[i] = -A0*Math.Exp(-Math.Pow(deltax*i-(xSteps-1)*deltax/2,2)/Math.Pow(delta,2));
                H_past[i] = H0+w_past[i];
            }
            for (int i= 1; i < xSteps-1; i++)
            {
                Nxx_past[i] = sigma0*h + Ef*h/(1-Math.Pow(nu_f,2))*((ux_past[i+1]-ux_past[i-1])/(2*deltax) + 
                    0.5*Math.Pow((w_past[i+1]-w_past[i-1])/(2*deltax),2));
            } 
            for (int i= 2; i < xSteps-2; i++)
            {
                taox_past[i] = (Nxx_past[i+1]-Nxx_past[i-1])/(2*deltax);
                 if (w_past[i] > 0)
                {
                    p_past[i] = Df*((w_past[i-2]-4*w_past[i-1]+6*w_past[i]-4*w_past[i+1]+w_past[i+2])/Math.Pow(deltax,4))
                        -Nxx_past[i]*((w_past[i+1]-2*w_past[i]+w_past[i-1])/Math.Pow(deltax,2))-taox_past[i]*
                        ((w_past[i+1]-w_past[i-1])/(2*deltax))-S*w_past[i];
                }
                else
                {
                    p_past[i] = Df*((w_past[i-2]-4*w_past[i-1]+6*w_past[i]-4*w_past[i+1]+w_past[i+2])/Math.Pow(deltax,4))
                        -Nxx_past[i]*((w_past[i+1]-2*w_past[i]+w_past[i-1])/Math.Pow(deltax,2))-taox_past[i]*
                        ((w_past[i+1]-w_past[i-1])/(2*deltax));
                }            
            }
    
            // Time step through cycles and populate each matrix of w, ux, H, Nxx, taox, and p each cycle
            for (int j = 1; j < Points; j++)   
            {
                for (int i= 3; i < xSteps-3; i++)
                {
                    w[i] = w_past[i] + dT/eta_R*((Math.Pow(H_past[i],3)/3*(p_past[i+1]-2*p_past[i]+p_past[i-1])/
                        Math.Pow(deltax,2)+(Math.Pow(H_past[i],2)*(H_past[i+1]-H_past[i-1])/(2*deltax) * 
                        ((p_past[i+1]-p_past[i-1])/(2*deltax))))-(((H_past[i+1]-H_past[i-1])/(2*deltax))*H_past[i]*
                        taox_past[i]+Math.Pow(H_past[i],2)/2*(taox_past[i+1]-taox_past[i-1])/(2*deltax)));
                    H[i] = H0+w[i];
                    
                    ux[i] = dT/eta_R*(taox_past[i]*H_past[i]-Math.Pow(H_past[i],2)/2*(p_past[i+1]-p_past[i-1])/(2*deltax))+ux_past[i];
                }
                for (int i= 1; i < xSteps-1; i++)
                {
                    Nxx[i] = sigma0*h + Ef*h/(1-Math.Pow(nu_f,2))*((ux[i+1]-ux[i-1])/(2*deltax) + 0.5*Math.Pow((w[i+1]-w[i-1])/
                        (2*deltax),2));
                }
                for (int i= 2; i < xSteps-2; i++)
                {
                    taox[i] = (Nxx[i + 1] - Nxx[i - 1]) / (2 * deltax);
    
                    if (w[i] > 0)
                    {
                        p[i] = Df*((w[i-2]-4*w[i-1]+6*w[i]-4*w[i+1]+w[i+2])/Math.Pow(deltax,4))-Nxx[i]*((w[i+1]-2*w[i]+w[i-1])/
                            Math.Pow(deltax,2))-taox[i]*((w[i+1]-w[i-1])/(2*deltax))-S*w[i];
                    }
                        
                    else
                        p[i] = Df*((w[i-2]-4*w[i-1]+6*w[i]-4*w[i+1]+w[i+2])/Math.Pow(deltax,4))-Nxx[i]*((w[i+1]-2*w[i]+w[i-1])/
                            Math.Pow(deltax,2))-taox[i]*((w[i+1]-w[i-1])/(2*deltax));
                }
                for (int i=0; i < xSteps; i++)
                {
                    w_past[i] = w[i];
                    ux_past[i] = ux[i];
                    taox_past[i] = taox[i];
                    Nxx_past[i] = Nxx[i];
                    p_past[i] = p[i];
                    H_past[i] = H[i];
                }
                pbarProgress.Value = Convert.ToInt32(Convert.ToDouble(j) / Convert.ToDouble(Points) * 100);
            }

            for (int i = 1; i < xSteps; i++)
            {
                chtDisplacement.Series["Displacement (um)"].Points.AddXY(i*deltax, w[i]);
            }

        }

    }
}
