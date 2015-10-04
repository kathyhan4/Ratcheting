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

# Material Properties Constants
Ef = 333000. # Young's modulus of elastic film in MPa
nu_f = 0.3 #Poisson's ratio of elastic film
sigma0 = -0.014*Ef # Initial in plane bilateral stress in MPa, this is a guess
Em = 200000. #Young's modulus of the metal in MPa
nu_m = 0.25 # Poisson's ratio of the metal
#alpha_m = 24e-6 # thermal coefficient of expansion of metal
#alpha_s = 2.8e-6 # thermal coefficient of expansion of substrate, Si
alpha_m = 24e-6 # thermal coefficient of expansion of metal
alpha_s = 14e-6 # thermal coefficient of expansion of substrate, (would be Si, but Si is 2.4??e-6)
TH = 90.0 # temperature in C of max cycle temp
TL = -10.0 # temperature in C of min cycle temp
Y = 100.0 # uniaxial yield strength of metal in MPa

def ratchet(PointsPerCycle=10000, NumberCycles=20, H0 = 10, xSteps=201, SimulationWidth=200, Sfactor=0):
    # Simulation Constants
    h = float(1) # film thickness in microns
#    PointsPerCycle = 1 #number of timepoints per cycle, higher number is slower, but should have more stable results
#    NumberCycles = 10 # arbitrarily chose number of cycles, can graph any of these later
    dT = 1/float(PointsPerCycle) #timestep in units of cycles
#    H0 = 10 * h #initial thickness of metal in units of h
#    xSteps = 201
#    SimulationWidth = 200 * h # will simulate a 200 um wide 
    #deltax = SimulationWidth / (xSteps-1) #mesh size in x direction in mm
    deltax = (SimulationWidth / (xSteps-1))
    S = float64(Sfactor) * Ef # try for S=0, S=0.1, and S=10 for elastic constraint values
    Points = int(PointsPerCycle*NumberCycles)
    
    # Derived Constants
    eta_R = Em/(12*(1-nu_m))*((Em*(alpha_m-alpha_s)*(TH-TL)/(1-nu_m)/Y)-2)**(-1)
    #eta_R = 33300.0 #MPa
    Df = Ef*h**3/(12*(1-nu_f**2))
    
    # Initial conditions constants
    A0 = h * 0.01 # amplitude of initial perturbation
    delta = h*20 #denominator of exponent for initial film height perturbation
    
    # First check to make sure your system undergoes ratcheting, Em(alpha_m-alpha_s)(TH-TL)/((1-nu_m)Y)>2 if this isn't true then don't run program
    Criteria = Em*(alpha_m-alpha_s)*(TH-TL)/((1-nu_m)*Y)
    
    if Criteria > 2:
        print 'Proceed with analysis'
    else:
        print 'System will not ratchet'
    
    #initialize all lists to store cycle number and space dependent data
    
    w = numpy.zeros((xSteps, Points),dtype=numpy.float64)
    ux = numpy.zeros((xSteps, Points),dtype=numpy.float64)
    taox = numpy.zeros((xSteps, Points),dtype=numpy.float64)
    Nxx = numpy.zeros((xSteps, Points),dtype=numpy.float64)
    p = numpy.zeros((xSteps, Points),dtype=numpy.float64)
    H = numpy.zeros((xSteps, Points),dtype=numpy.float64)
    
    for i in range(0,xSteps):
        for j in range(0,Points):
            H[i,j] = H0
    
    # Insert initial conditions for w and ux and solve for initial conditions of the others
    # ux initial conditions are zeros
    
    for i in range(0,xSteps): 
        w[i,0] = A0*math.sin(float(i)*2*pi/20)
        H[i,0] = H0+w[i,0]
    
    for i in range(1,xSteps-1): 
        Nxx[i,0] = sigma0*h + Ef*h/(1-nu_f**2)*((ux[i+1,0]-ux[i-1,0])/2/deltax + 0.5*((w[i+1,0]-w[i-1,0])/2/deltax)**2)
    Nxx[0,0] = sigma0*h + Ef*h/(1-nu_f**2)*((ux[1,0]-ux[xSteps-1,0])/2/deltax + 0.5*((w[1,0]-w[xSteps-1,0])/2/deltax)**2)
    Nxx[xSteps-1,0] = sigma0*h + Ef*h/(1-nu_f**2)*((ux[0,0]-ux[xSteps-2,0])/2/deltax + 0.5*((w[0,0]-w[xSteps-2,0])/2/deltax)**2)
    
    for i in range(1,xSteps-1): 
        taox[i,0] = (Nxx[i+1,0]-Nxx[i-1,0])/2/deltax
    taox[0,0] = (Nxx[1,0]-Nxx[xSteps-1,0])/2/deltax
    taox[xSteps-1,0] = (Nxx[0,0]-Nxx[xSteps-2,0])/2/deltax
    
    for i in range(2,xSteps-2): 
        if w[i,0] > 0:
            p[i,0] = Df*((w[i-2,0]-4*w[i-1,0]+6*w[i,0]-4*w[i+1,0]+w[i+2,0])/(deltax**4))-Nxx[i,0]*((w[i+1,0]-2*w[i,0]+w[i-1,0])/(deltax**2))-\
            taox[i,0]*((w[i+1,0]-w[i-1,0])/2/deltax)-S*w[i,0]
    
        else:
            p[i,0] = Df*((w[i-2,0]-4*w[i-1,0]+6*w[i,0]-4*w[i+1,0]+w[i+2,0])/(deltax**4))-Nxx[i,0]*((w[i+1,0]-2*w[i,0]+w[i-1,0])/(deltax**2))-\
            taox[i,0]*((w[i+1,0]-w[i-1,0])/2/deltax)
            
    if w[0,0] > 0:
        p[0,0] = Df*((w[xSteps-2,0]-4*w[xSteps-1,0]+6*w[0,0]-4*w[1,0]+w[2,0])/(deltax**4))-Nxx[0,0]*((w[1,0]-2*w[0,0]+w[xSteps-1,0])/(deltax**2))-\
        taox[0,0]*((w[1,0]-w[xSteps-1,0])/2/deltax)-S*w[i,0]
    else:
        p[0,0] = Df*((w[xSteps-2,0]-4*w[xSteps-1,0]+6*w[0,0]-4*w[1,0]+w[2,0])/(deltax**4))-Nxx[0,0]*((w[1,0]-2*w[0,0]+w[xSteps-1,0])/(deltax**2))-\
        taox[0,0]*((w[1,0]-w[xSteps-1,0])/2/deltax)
    
    if w[1,0] > 0:    
        p[1,0] = Df*((w[xSteps-1,0]-4*w[0,0]+6*w[1,0]-4*w[2,0]+w[3,0])/(deltax**4))-Nxx[1,0]*((w[2,0]-2*w[1,0]+w[0,0])/(deltax**2))-\
        taox[1,0]*((w[2,0]-w[0,0])/2/deltax)-S*w[1,0]
    else:
        p[1,0] = Df*((w[xSteps-1,0]-4*w[0,0]+6*w[1,0]-4*w[2,0]+w[3,0])/(deltax**4))-Nxx[1,0]*((w[2,0]-2*w[1,0]+w[0,0])/(deltax**2))-\
        taox[1,0]*((w[2,0]-w[0,0])/2/deltax)
        
    if w[xSteps-2,0] > 0:     
        p[xSteps-2,0] = Df*((w[xSteps-4,0]-4*w[xSteps-3,0]+6*w[xSteps-2,0]-4*w[xSteps-1,0]+w[0,0])/(deltax**4))-Nxx[xSteps-2,0]*((w[xSteps-1,0]-2*w[xSteps-2,0]+w[xSteps-3,0])/(deltax**2))-\
        taox[xSteps-2,0]*((w[xSteps-1,0]-w[xSteps-3,0])/2/deltax)-S*w[xSteps-2,0]
    else: 
        p[xSteps-2,0] = Df*((w[xSteps-4,0]-4*w[xSteps-3,0]+6*w[xSteps-2,0]-4*w[xSteps-1,0]+w[0,0])/(deltax**4))-Nxx[xSteps-2,0]*((w[xSteps-1,0]-2*w[xSteps-2,0]+w[xSteps-3,0])/(deltax**2))-\
        taox[xSteps-2,0]*((w[xSteps-1,0]-w[xSteps-3,0])/2/deltax)
        
    if w[xSteps-1,0] > 0:     
        p[xSteps-1,0] = Df*((w[xSteps-3,0]-4*w[xSteps-2,0]+6*w[xSteps-1,0]-4*w[0,0]+w[1,0])/(deltax**4))-Nxx[xSteps-1,0]*((w[0,0]-2*w[xSteps-1,0]+w[xSteps-2,0])/(deltax**2))-\
        taox[xSteps-1,0]*((w[0,0]-w[xSteps-2,0])/2/deltax)-S*w[xSteps-1,0]
    else:    
        p[xSteps-1,0] = Df*((w[xSteps-3,0]-4*w[xSteps-2,0]+6*w[xSteps-1,0]-4*w[0,0]+w[1,0])/(deltax**4))-Nxx[xSteps-1,0]*((w[0,0]-2*w[xSteps-1,0]+w[xSteps-2,0])/(deltax**2))-\
        taox[xSteps-1,0]*((w[0,0]-w[xSteps-2,0])/2/deltax)
        
    #Time step through cycles and populate each matrix of w, ux, H, Nxx, taox, and p each cycle
       
    for j in range(1,Points):
    
    #    w[0,j] = 0
    #    w[xSteps-1,j] = 0     
    #    w[1,j] = 0
    #    w[xSteps-2,j] = 0
    #
    #    ux[0,j] = 0
    #    ux[xSteps-1,j] = 0
    #    ux[1,j] = 0
    #    ux[xSteps-2,j] = 0
    #    
    #    H[0,j] = H0
    #    H[xSteps-1,j] = H0
    #    H[01,j] = H0
    #    H[xSteps-2,j] = H0
    
        for i in range(1,xSteps-1): 
    #        w[i,j] = w[i,j-1] + dT/eta_R*(((H[i,j-1])**3/3*(p[i+1,j-1]-2*p[i,j-1]+p[i-1,j-1])/\
    #        (deltax**2)+((H[i,j-1])**2*(H[i+1,j-1]-H[i-1,j-1])/2/deltax * \
    #        ((p[i+1,j-1]-p[i-1,j-1])/2/deltax)))-(((H[i+1,j-1]-H[i-1,j-1])/2/deltax)*H[i,j-1]*\
    #        taox[i,j-1]+(H[i,j-1])**2/2*(taox[i+1,j-1]-taox[i-1,j-1])/2/deltax))        
            w[i,j] = w[i,j-1] + dT/eta_R*((1-2*nu_m)/2/(1-nu_m)*H[i,j-1]/eta_R*h**3/12*(-p[i,j-1])-(mu_R/eta_R*w[i,j-1]))        
           
            H[i,j] = H0+w[i,j]
            
    #    w[0,j] = w[0,j-1] + dT/eta_R*(((H[0,j-1])**3/3*(p[1,j-1]-2*p[0,j-1]+p[xSteps-1,j-1])/\
    #    (deltax**2)+((H[0,j-1])**2*(H[1,j-1]-H[xSteps-1,j-1])/2/deltax * \
    #    ((p[1,j-1]-p[xSteps-1,j-1])/2/deltax)))-(((H[1,j-1]-H[xSteps-1,j-1])/2/deltax)*H[0,j-1]*\
    #    taox[0,j-1]+(H[0,j-1])**2/2*(taox[1,j-1]-taox[xSteps-1,j-1])/2/deltax))
        w[0,j] = w[0,j-1] + dT/eta_R*((1-2*nu_m)/2/(1-nu_m)*H[0,j-1]/eta_R*h**3/12*(-p[0,j-1])-(mu_R/eta_R*w[0,j-1]))
        
        w[xSteps-1,j] = w[xSteps-1,j-1] + dT/eta_R*((1-2*nu_m)/2/(1-nu_m)*H[xSteps-1,j-1]/eta_R*h**3/12*(-p[xSteps-1,j-1])-(mu_R/eta_R*w[xSteps-1,j-1]))     
        
        for i in range(1,xSteps-1): 
            ux[i,j] = dT/eta_R*(H[i,j-1]*taox[i,j-1]-mu_R*ux[i,j-1])+ux[i,j-1]
            
        ux[0,j] = dT/eta_R*(H[0,j-1]*taox[0,j-1]-mu_R*ux[0,j-1])+ux[0,j-1]
        ux[xSteps-1,j] = dT/eta_R*(H[xSteps-1,j-1]*taox[xSteps-1,j-1]-mu_R*ux[xSteps-1,j-1])+ux[xSteps-1,j-1]
    #        ux[2,j]=0
    #        ux[xSteps-3,j]=0
                    
        for i in range(1,xSteps-1): 
            Nxx[i,j] = sigma0*h + Ef*h/(1-nu_f**2)*((ux[i+1,j]-ux[i-1,j])/2/deltax + 0.5*((w[i+1,j]-w[i-1,j])/2/deltax)**2)
            
        Nxx[0,j] = sigma0*h + Ef*h/(1-nu_f**2)*((ux[1,j]-ux[xSteps-1,j])/2/deltax + 0.5*((w[1,j]-w[xSteps-1,j])/2/deltax)**2)
        Nxx[xSteps-1,j] = sigma0*h + Ef*h/(1-nu_f**2)*((ux[0,j]-ux[xSteps-2,j])/2/deltax + 0.5*((w[0,j]-w[xSteps-2,j])/2/deltax)**2)
        
        for i in range(2,xSteps-2): 
            taox[i,j] = (Nxx[i+1,j]-Nxx[i-1,j])/2/deltax
            
        taox[0,j] = (Nxx[1,j]-Nxx[xSteps-1,j])/2/deltax
        taox[xSteps-1,j] = (Nxx[0,j]-Nxx[xSteps-2,j])/2/deltax
         
        
        for i in range(2,xSteps-2): 
            if w[i,j] > 0:
                p[i,j] = Df*((w[i-2,j]-4*w[i-1,j]+6*w[i,j]-4*w[i+1,j]+w[i+2,j])/(deltax**4))-Nxx[i,j]*((w[i+1,j]-2*w[i,j]+w[i-1,j])/(deltax**2))-\
                taox[i,j]*((w[i+1,j]-w[i-1,j])/2/deltax)-S*w[i,j]
    #            p1 = Df*((w[i-2,0]-4*w[i-1,0]+6*w[i,0]-4*w[i+1,0]+w[i+2,0])/(deltax**4))
    #            p2 =  -Nxx[i,0]*((w[i+1,0]-2*w[i,0]+w[i-1,0])/(deltax**2))
    #            p3 = -taox[i,0]*((w[i+1,0]-w[i-1,0])/2/deltax)-S*w[i,0] 
    #            p4 = -S*w[i,0]
    
            else:
                p[i,j] = Df*((w[i-2,j]-4*w[i-1,j]+6*w[i,j]-4*w[i+1,j]+w[i+2,j])/(deltax**4))-Nxx[i,j]*((w[i+1,j]-2*w[i,j]+w[i-1,j])/(deltax**2))-\
                taox[i,j]*((w[i+1,j]-w[i-1,j])/2/deltax)
    #            p5 = Df*((w[i-2,0]-4*w[i-1,0]+6*w[i,0]-4*w[i+1,0]+w[i+2,0])/(deltax**4))
    #            p6 =  -Nxx[i,0]*((w[i+1,0]-2*w[i,0]+w[i-1,0])/(deltax**2))
    #            p7 = -taox[i,0]*((w[i+1,0]-w[i-1,0])/2/deltax)-S*w[i,0] 
                
        if w[0,j] > 0:
            p[0,j] = Df*((w[xSteps-2,j]-4*w[xSteps-1,j]+6*w[0,j]-4*w[1,j]+w[2,j])/(deltax**4))-Nxx[0,j]*((w[1,j]-2*w[0,j]+w[xSteps-1,j])/(deltax**2))-\
            taox[0,j]*((w[1,j]-w[xSteps-1,j])/2/deltax)-S*w[i,j]
        else:
            p[0,j] = Df*((w[xSteps-2,j]-4*w[xSteps-1,j]+6*w[0,j]-4*w[1,j]+w[2,j])/(deltax**4))-Nxx[0,j]*((w[1,j]-2*w[0,j]+w[xSteps-1,j])/(deltax**2))-\
            taox[0,j]*((w[1,j]-w[xSteps-1,j])/2/deltax)
        
        if w[1,j] > 0:    
            p[1,j] = Df*((w[xSteps-1,j]-4*w[0,j]+6*w[1,j]-4*w[2,j]+w[3,j])/(deltax**4))-Nxx[1,j]*((w[2,j]-2*w[1,j]+w[0,j])/(deltax**2))-\
            taox[1,j]*((w[2,j]-w[0,j])/2/deltax)-S*w[1,j]
        else:
            p[1,j] = Df*((w[xSteps-1,j]-4*w[0,j]+6*w[1,j]-4*w[2,j]+w[3,j])/(deltax**4))-Nxx[1,j]*((w[2,j]-2*w[1,j]+w[0,j])/(deltax**2))-\
            taox[1,j]*((w[2,j]-w[0,j])/2/deltax)
            
        if w[xSteps-2,j] > 0:     
            p[xSteps-2,j] = Df*((w[xSteps-4,j]-4*w[xSteps-3,j]+6*w[xSteps-2,j]-4*w[xSteps-1,j]+w[0,j])/(deltax**4))-Nxx[xSteps-2,j]*((w[xSteps-1,j]-2*w[xSteps-2,j]+w[xSteps-3,j])/(deltax**2))-\
            taox[xSteps-2,j]*((w[xSteps-1,j]-w[xSteps-3,j])/2/deltax)-S*w[xSteps-2,j]
        else: 
            p[xSteps-2,j] = Df*((w[xSteps-4,j]-4*w[xSteps-3,j]+6*w[xSteps-2,j]-4*w[xSteps-1,j]+w[0,j])/(deltax**4))-Nxx[xSteps-2,j]*((w[xSteps-1,j]-2*w[xSteps-2,j]+w[xSteps-3,j])/(deltax**2))-\
            taox[xSteps-2,j]*((w[xSteps-1,j]-w[xSteps-3,j])/2/deltax)
            
        if w[xSteps-1,j] > 0:     
            p[xSteps-1,j] = Df*((w[xSteps-3,j]-4*w[xSteps-2,j]+6*w[xSteps-1,j]-4*w[0,j]+w[1,j])/(deltax**4))-Nxx[xSteps-1,j]*((w[0,j]-2*w[xSteps-1,j]+w[xSteps-2,j])/(deltax**2))-\
            taox[xSteps-1,j]*((w[0,j]-w[xSteps-2,j])/2/deltax)-S*w[xSteps-1,j]
        else:    
            p[xSteps-1,j] = Df*((w[xSteps-3,j]-4*w[xSteps-2,j]+6*w[xSteps-1,j]-4*w[0,j]+w[1,j])/(deltax**4))-Nxx[xSteps-1,j]*((w[0,j]-2*w[xSteps-1,j]+w[xSteps-2,j])/(deltax**2))-\
            taox[xSteps-1,j]*((w[0,j]-w[xSteps-2,j])/2/deltax)

    
 
    figure   
    plt.plot(w[:,0],'k')
    plt.plot(w[:,2],'b')
    plt.plot(w[:,Points/2],'g')
    plt.plot(w[:,Points-1],'r')
