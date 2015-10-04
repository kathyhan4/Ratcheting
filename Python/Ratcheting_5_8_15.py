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
Ef = 7 # Young's modulus of elastic film in MPa
nu_f = 0.4 #Poisson's ratio of elastic film
sigma0 = -0.014*Ef # Initial in plane bilateral stress in MPa, this is a guess
Em = 69000 #Young's modulus of the metal
nu_m = 0.33 # Poisson's ratio of the metal
alpha_m = 24e-6 # thermal coefficient of expansion of metal
alpha_s = 2.8e-6 # thermal coefficient of expansion of substrate, Si
TH = 90 # temperature in C of max cycle temp
TL = -40 # temperature in C of min cycle temp
Y = 31 # uniaxial yield strength of metal in MPa

# Simulation Constants
PointsPerCycle = 100 #number of timepoints per cycle, higher number is slower, but will have more stable results
dT = 1/float(PointsPerCycle) #timestep in units of cycles
H0 = 0.037 #initial thickness of metal
h = 0.001 # film thickness
xSteps = 200
SimulationWidth = h * xSteps #will simulate a 200 um wide domain
NumberCycles = 10 # arbitrarily chose 1000 cycles, can graph any of these later
deltax = 0.001 #mesh size in x direction in mm
S = float(0) # try for S=0, S=0.1, and S=10 for elastic constraint values



# Derived Constants
#eta_R = Em/(12*(1-nu_m))*((Em*(alpha_m-alpha_s)*(TH-TL)/(1-nu_m)/Y)-2)**(-1)
eta_R = Ef*0.1
Df = Ef*h**3/(12*(1-nu_f**2))

# Initial conditions constants
A0 = h * 0.01 # amplitude of initial perturbation
delta = h*20 #denominator of exponent for initial film height perturbation

#initialize all lists to store cycle number and space dependent data

w = numpy.zeros((xSteps, NumberCycles*PointsPerCycle))
ux = numpy.zeros((xSteps, NumberCycles*PointsPerCycle))
taox = numpy.zeros((xSteps, NumberCycles*PointsPerCycle))
Nxx = numpy.zeros((xSteps, NumberCycles*PointsPerCycle))
p = numpy.zeros((xSteps, NumberCycles*PointsPerCycle))
H = numpy.zeros((xSteps, NumberCycles*PointsPerCycle))

for i in range(0,xSteps):
    for j in range(0,NumberCycles*PointsPerCycle):
        H[i,j] = H0

# Insert initial conditions for w and ux and solve for initial conditions of the others
# ux initial conditions are zeros
# Need at least four boundary conditions and one initial condition.  Let's say the value of w=0 at x=0 and x=xmax, dw/dx = 0 at x=0 and x=xmax


w[0,0] = A0*exp(-(deltax*i-0.1)**2/(delta**2))
w[xSteps-1,0] = A0*exp(-(deltax*i-0.1)**2/(delta**2))

for i in range(1,xSteps-2): #will go from 0 to xSteps - 1
    w[i,0] = A0*exp(-(deltax*i-0.1)**2/(delta**2))
    w[0,0] = 0
    w[xSteps-1] = 0
    w[1,0] = 0
    w[xSteps-2] = 0
    H[i,0] = H0+w[i,0]
    Nxx[i,0] = sigma0*h + Ef*h/(1-nu_f**2)*((ux[i+1,0]-ux[i-1,0])/2/deltax + 0.5*((w[i+1,0]-w[i-1,0])/2/deltax)**2)
    taox[i,0] = (Nxx[i+1,0]-Nxx[i-1,0])/2/deltax

for i in range(2,xSteps-3): #will go from 0 to xSteps - 1
    if w[i,0] > 0:
        p[i,0] = Df*((w[i-2,0]-4*w[i-1,0]+6*w[i,0]-4*w[i+1,0]+w[i+2,0])/(deltax**4))-Nxx[i,0]*((w[i+1,0]-2*w[i,0]+w[i-1,0])/(deltax**2))-taox[i,0]*((w[i+1,0]-w[i-1,0])/2/deltax)-S*w[i,0]
    else:
        p[i,0] = Df*((w[i-2,0]-4*w[i-1,0]+6*w[i,0]-4*w[i+1,0]+w[i+2,0])/(deltax**4))-Nxx[i,0]*((w[i+1,0]-2*w[i,0]+w[i-1,0])/(deltax**2))-taox[i,0]*((w[i+1,0]-w[i-1,0])/2/deltax)
   
#Time step through cycles and populate each matrix of w, ux, H, Nxx, taox, and p each cycle
   
for j in range(1,NumberCycles * PointsPerCycle):
    for i in range(1,xSteps-2): #will go from 0 to xSteps - 1

        w[i,j] = w[i,j-1] + dT/eta_R*(((H[i,j-1])**3/3*(p[i+1,j-1]-2*p[i,j-1]+p[i-1,j-1])/(deltax**2)+((H[i,j-1])**2*(H[i+1,j-1]-H[i-1,j-1])/2/deltax * \
        ((p[i+1,j-1]-p[i-1,j-1])/2/deltax)))-(((H[i+1,j-1]-H[i-1,j-1])/2/deltax)*H[i,j-1]*taox[i,j-1]+(H[i,j-1])**2/2*(taox[i+1,j-1]-taox[i-1,j-1])/2/deltax)) 
        w[0,j] = 0
        w[xSteps-1,j] = 0        
        w[1,j] = w[0,j]
        w[xSteps-2,j]= w[xSteps-1,j]
        ux[i,j] = dT/eta_R*(taox[i,j-1]*H[i,j-1]-(H[i,j-1])**2/2*(p[i+1,j-1]-p[i-1,j-1])/2/deltax)+ux[i,j-1]
        H[i,j] = H0+w[i,j]
        Nxx[i,j] = sigma0*h + Ef*h/(1-nu_f**2)*((ux[i+1,j]-ux[i-1,j])/2/deltax + 0.5*((w[i+1,j]-w[i-1,j])/2/deltax)**2)
        taox[i,j] = (Nxx[i+1,j]-Nxx[i-1,j])/2/deltax

    for i in range(2,xSteps-3): #will go from 0 to xSteps - 1
        if w[i,j] < 0:
            p[i,j] = Df*((w[i-2,j]-4*w[i-1,j]+6*w[i,j]-4*w[i+1,j]+w[i+2,j])/(deltax**4))-Nxx[i,j]*((w[i+1,j]-2*w[i,j]+w[i-1,j])/(deltax**2))-taox[i,j]*((w[i+1,j]-w[i-1,j])/2/deltax)-S*w[i,j]
        else:
            p[i,j] = Df*((w[i-2,j]-4*w[i-1,j]+6*w[i,j]-4*w[i+1,j]+w[i+2,j])/(deltax**4))-Nxx[i,j]*((w[i+1,j]-2*w[i,j]+w[i-1,j])/(deltax**2))-taox[i,j]*((w[i+1,j]-w[i-1,j])/2/deltax)

 
figure   
plt.plot(w[:,0],'k')
plt.plot(w[:,NumberCycles*PointsPerCycle/2],'g')
plt.plot(w[:,NumberCycles*PointsPerCycle*3/4],'r')