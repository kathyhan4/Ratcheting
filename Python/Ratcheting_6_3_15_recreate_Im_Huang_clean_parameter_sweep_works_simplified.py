# -*- coding: utf-8 -*-
"""
Created on Fri May 08 13:17:40 2015

@author: khan
"""
# Numerical simulation of Ratcheting based on "Ratcheting-induced wrinkling of 
#an elastic film on a metal layer under cyclic temperatures" by Im and Huang 
#2004, Acta Materialia 52 p.3707-3719
#And "Wrinkling of a compressed elastic film on a viscous layer" by Huang and Suo, 
#Journal of Applied Physics, volume 91, number 3, p. 1135

import csv
import os
from numpy import array
import numpy
import datetime
#from datetime import datetime
import time
import matplotlib.pyplot as plt
import dateutil
from pylab import *
import bisect


nu_f_values = [0.3]
SimulationWidth_values = [200]
PointsPerCycle_values = [10000]
#output = numpy.zeros((len(nu_f_values),len(PointsPerCycle_values)))
OutputCycles = [0,10,20,200]



for s in range(0,len(nu_f_values)):
    for q in range(0,len(PointsPerCycle_values)):
        xSteps = 201
        Outputw = numpy.zeros((xSteps,len(OutputCycles)))
        Outputux = numpy.zeros((xSteps,len(OutputCycles)))
        timepointcount = 0
        # First check to make sur# Material Properties Constants
        Ef = 333000. # Young's modulus of elastic film in MPa
        nu_f = 0.3 #Poisson's ratio of elastic film
        sigma0 = -0.014*Ef # Initial in plane bilateral stress in MPa, this is a guess
#        nu_f = nu_f_values[s]
        Em = 200000. #Young's modulus of the metal in MPa
        nu_m = 0.25 # Poisson's ratio of the metal
        #alpha_m = 24e-6 # thermal coefficient of expansion of metal
        #alpha_s = 2.8e-6 # thermal coefficient of expansion of substrate, Si
        alpha_m = 24e-6 # thermal coefficient of expansion of metal
        alpha_s = 14e-6 # thermal coefficient of expansion of substrate, (would be Si, but Si is 2.4??e-6)
        TH = 90.0 # temperature in C of max cycle temp
        TL = -10.0 # temperature in C of min cycle temp
        Y = 100.0 # uniaxial yield strength of metal in MPa
        
        # Simulation Constants
        h = float(1) # film thickness in microns
#        PointsPerCycle = 10 #number of timepoints per cycle, higher number is slower, but should have more stable results
        PointsPerCycle = PointsPerCycle_values[q]
        NumberCycles = 1 # arbitrarily chose number of cycles, can graph any of these later
        dT = 1/float(PointsPerCycle) #timestep in units of cycles
        H0 = 10 * h #initial thickness of metal in units of h

        SimulationWidth = 200 * h # will simulate a 200 um wide 

#        SimulationWidth = SimulationWidth_values[q]*h
        #deltax = SimulationWidth / (xSteps-1) #mesh size in x direction in mm
        deltax = (SimulationWidth / (xSteps-1))
        S = float64(0.1) * Ef # try for S=0, S=0.1, and S=10 for elastic constraint values
        Points = int(PointsPerCycle*NumberCycles)
        
        # Derived Constants
        eta_R = Em/(12*(1-nu_m))*((Em*(alpha_m-alpha_s)*(TH-TL)/(1-nu_m)/Y)-2)**(-1)
        #eta_R = 33300.0 #MPa
        Df = Ef*h**3/(12*(1-nu_f**2))
        
        # Initial conditions constants
        A0 = h * 0.01 # amplitude of initial perturbation
        delta = h*20 #denominator of exponent for initial film height perturbatione your system undergoes ratcheting, Em(alpha_m-alpha_s)(TH-TL)/((1-nu_m)Y)>2 if this isn't true then don't run program
        Criteria = Em*(alpha_m-alpha_s)*(TH-TL)/((1-nu_m)*Y)
        
        if Criteria > 2:
            print 'Proceed with analysis'
        else:
            print 'System will not ratchet'
        
        #initialize all lists to store cycle number and space dependent data
        
#        w = numpy.zeros((xSteps, Points),dtype=numpy.float64)
#        ux = numpy.zeros((xSteps, Points),dtype=numpy.float64)
#        taox = numpy.zeros((xSteps, Points),dtype=numpy.float64)
#        Nxx = numpy.zeros((xSteps, Points),dtype=numpy.float64)
#        p = numpy.zeros((xSteps, Points),dtype=numpy.float64)
#        H = numpy.zeros((xSteps, Points),dtype=numpy.float64)
        w = numpy.zeros((xSteps),dtype=numpy.float64)
        ux = numpy.zeros((xSteps),dtype=numpy.float64)
        taox = numpy.zeros((xSteps),dtype=numpy.float64)
        Nxx = numpy.zeros((xSteps),dtype=numpy.float64)
        p = numpy.zeros((xSteps),dtype=numpy.float64)
        H = numpy.zeros((xSteps),dtype=numpy.float64)
        w_past = numpy.zeros((xSteps),dtype=numpy.float64)
        ux_past = numpy.zeros((xSteps),dtype=numpy.float64)
        taox_past = numpy.zeros((xSteps),dtype=numpy.float64)
        Nxx_past = numpy.zeros((xSteps),dtype=numpy.float64)
        p_past = numpy.zeros((xSteps),dtype=numpy.float64)
        H_past = numpy.zeros((xSteps),dtype=numpy.float64)
        
        for i in range(0,xSteps):
            H[i] = H0
            H_past[i] = H0
                
        
        # Insert initial conditions for w and ux and solve for initial conditions of the others
        # ux initial conditions are zeros
        
        for i in range(3,xSteps-3): 
            w_past[i] = -A0*exp(-(deltax*float(i)-(int(xSteps)-1.)*deltax/2)**2/(delta**2))
            H_past[i] = H0+w_past[i]
        
        for i in range(1,xSteps-1): 
            Nxx_past[i] = sigma0*h + Ef*h/(1-nu_f**2)*((ux_past[i+1]-ux_past[i-1])/(2*deltax) + 0.5*((w_past[i+1]-w_past[i-1])/(2*deltax))**2)
        
        for i in range(2,xSteps-2): 
            taox_past[i] = (Nxx_past[i+1]-Nxx_past[i-1])/(2*deltax)
            if w_past[i] > 0:
                p_past[i] = Df*((w_past[i-2]-4*w_past[i-1]+6*w_past[i]-4*w_past[i+1]+w_past[i+2])/(deltax**4))-Nxx_past[i]*((w_past[i+1]-2*w_past[i]+w_past[i-1])/(deltax**2))- \
                taox_past[i]*((w_past[i+1]-w_past[i-1])/(2*deltax))-S*w_past[i]
        
            else:
                p_past[i] = Df*((w_past[i-2]-4*w_past[i-1]+6*w_past[i]-4*w_past[i+1]+w_past[i+2])/(deltax**4))-Nxx_past[i]*((w_past[i+1]-2*w_past[i]+w_past[i-1])/(deltax**2))- \
                taox_past[i]*((w_past[i+1]-w_past[i-1])/(2*deltax))        
        #Time step through cycles and populate each matrix of w, ux, H, Nxx, taox, and p each cycle
           
        for j in range(1,Points):
        
        
            for i in range(3,xSteps-3): 
                w[i] = w_past[i] + dT/eta_R*(((H_past[i])**3/3*(p_past[i+1]-2*p_past[i]+p_past[i-1])/ \
                (deltax**2)+((H_past[i])**2*(H_past[i+1]-H_past[i-1])/(2*deltax) * \
                ((p_past[i+1]-p_past[i-1])/(2*deltax))))-(((H_past[i+1]-H_past[i-1])/(2*deltax))*H_past[i]* \
                taox_past[i]+(H_past[i])**2/2*(taox_past[i+1]-taox_past[i-1])/(2*deltax)))
                
                H[i] = H0+w[i]
                
                ux[i] = dT/eta_R*(taox_past[i]*H_past[i]-(H_past[i])**2/2*(p_past[i+1]-p_past[i-1])/(2*deltax))+ux_past[i]
                       
            for i in range(1,xSteps-1): 
                Nxx[i] = sigma0*h + Ef*h/(1-nu_f**2)*((ux[i+1]-ux[i-1])/(2*deltax) + 0.5*((w[i+1]-w[i-1])/(2*deltax))**2)
        
            for i in range(2,xSteps-2): 
                taox[i] = (Nxx[i+1]-Nxx[i-1])/(2*deltax)

                if w[i] > 0:
                    p[i] = Df*((w[i-2]-4*w[i-1]+6*w[i]-4*w[i+1]+w[i+2])/(deltax**4))-Nxx[i]*((w[i+1]-2*w[i]+w[i-1])/(deltax**2))- \
                    taox[i]*((w[i+1]-w[i-1])/(2*deltax))-S*w[i]
        
                else:
                    p[i] = Df*((w[i-2]-4*w[i-1]+6*w[i]-4*w[i+1]+w[i+2])/(deltax**4))-Nxx[i]*((w[i+1]-2*w[i]+w[i-1])/(deltax**2))- \
                    taox[i]*((w[i+1]-w[i-1])/(2*deltax))
                    
            for i in range(0,xSteps):
                w_past[i] = w[i]
                ux_past[i] = ux[i]
                taox_past[i] = taox[i]
                Nxx_past[i] = Nxx[i]
                p_past[i] = p[i]
                H_past[i] = H[i]

            for i in range(len(OutputCycles)):
                if timepointcount == OutputCycles[i]*PointsPerCycle:
                    for k in range(xSteps):
                        Outputw[k] = w[k]
                        Outputux[k] = ux[k]
            timepointcount = timepointcount + 1
            print j
#        output[s,q] = w[int((xSteps-1)/2),Points-1]    
 
figure   
plt.plot(Outputw[:,0],'-b')
plt.plot(Outputw[:,len(OutputCycles)-1],'r')