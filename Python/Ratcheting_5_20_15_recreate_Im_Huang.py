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

# Simulation Constants
PointsPerCycle = 20 #number of timepoints per cycle, higher number is slower, but should have more stable results
dT = 1/float(PointsPerCycle) #timestep in units of cycles
H0 = 0.005 #initial thickness of metal in mm
h = 0.001 # film thickness in mm
xSteps = 201
SimulationWidth = 0.4 # will simulate a 200 um wide domain when set to 0.2 mm
NumberCycles = 600 # arbitrarily chose number of cycles, can graph any of these later
deltax = SimulationWidth / xSteps #mesh size in x direction in mm
S = float64(0) * Ef # try for S=0, S=0.1, and S=10 for elastic constraint values
Points = int(PointsPerCycle*NumberCycles)

# Derived Constants
#eta_R = Em/(12*(1-nu_m))*((Em*(alpha_m-alpha_s)*(TH-TL)/(1-nu_m)/Y)-2)**(-1)
eta_R = 33300.0 #MPa
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
# Need at least four boundary conditions and one initial condition.  Let's say the value of w=0 at x=0 and x=xmax, dw/dx = 0 at x=0 and x=xmax

for i in range(0,xSteps): 
    w[i,0] = -A0*exp(-(deltax*i-(xSteps-1)*deltax/2)**2/(delta**2))
    H[i,0] = H0+w[i,0]

#H[0,0] = H0
#H[xSteps-1,0] = H0

for i in range(2,xSteps-2): 
    Nxx[i,0] = sigma0*h + Ef*h/(1-nu_f**2)*((ux[i+1,0]-ux[i-1,0])/2/deltax + 0.5*((w[i+1,0]-w[i-1,0])/2/deltax)**2)

#Nxx[0,0] = Nxx[1,0]
#Nxx[xSteps-1,0] = Nxx[xSteps-2,0]

for i in range(2,xSteps-2): 
    taox[i,0] = (Nxx[i+1,0]-Nxx[i-1,0])/2/deltax

    
#taox[0,0] = taox[1,0]
#taox[xSteps-1,0] = taox[xSteps-2,0]
#p[0,0] = 0
#p[xSteps-1,0] = 0
#
#p[1,0] = p[0,0]
##        p[1,0] = 0
#
#p[xSteps-2,0] = p[xSteps-1,0]
for i in range(2,xSteps-2): 
    if w[i,0] > 0:
        p[i,0] = Df*((w[i-2,0]-4*w[i-1,0]+6*w[i,0]-4*w[i+1,0]+w[i+2,0])/(deltax**4))-Nxx[i,0]*((w[i+1,0]-2*w[i,0]+w[i-1,0])/(deltax**2))-\
        taox[i,0]*((w[i+1,0]-w[i-1,0])/2/deltax)-S*w[i,0]

    else:
        p[i,0] = Df*((w[i-2,0]-4*w[i-1,0]+6*w[i,0]-4*w[i+1,0]+w[i+2,0])/(deltax**4))-Nxx[i,0]*((w[i+1,0]-2*w[i,0]+w[i-1,0])/(deltax**2))-\
        taox[i,0]*((w[i+1,0]-w[i-1,0])/2/deltax)
#p[0,0] = 0
#p[xSteps-1,0] = 0
#
#p[1,0] = p[2,0]
##        p[1,0] = 0
#
#p[xSteps-2,0] = p[xSteps-3,0]
##        p[xSteps-2,0] = 0
#
#p[0,0] = p[1,0]
#p[xSteps-1,0] = p[xSteps-2,0]
#p[0,0] = 0
#p[xSteps-1,0] = 0

#ux[0,0] = 0
#ux[xSteps-1,0] = 0

#Time step through cycles and populate each matrix of w, ux, H, Nxx, taox, and p each cycle
   
for j in range(1,Points):

    w[0,j] = 0
    w[xSteps-1,j] = 0     
    w[1,j] = 0
    w[xSteps-2,j] = 0

    ux[0,j] = 0
    ux[xSteps-1,j] = 0
    ux[1,j] = 0
    ux[xSteps-2,j] = 0
    
    H[0,j] = H0
    H[xSteps-1,j] = H0
    H[01,j] = H0
    H[xSteps-2,j] = H0

    for i in range(5,xSteps-5): 
        w[i,j] = w[i,j-1] + dT/eta_R*(((H[i,j-1])**3/3*(p[i+1,j-1]-2*p[i,j-1]+p[i-1,j-1])/\
        (deltax**2)+((H[i,j-1])**2*(H[i+1,j-1]-H[i-1,j-1])/2/deltax * \
        ((p[i+1,j-1]-p[i-1,j-1])/2/deltax)))-(((H[i+1,j-1]-H[i-1,j-1])/2/deltax)*H[i,j-1]*\
        taox[i,j-1]+(H[i,j-1])**2/2*(taox[i+1,j-1]-taox[i-1,j-1])/2/deltax))
        
#        w[2,j]=0
#        w[xSteps-3,j]=0
        
#        w1 = dT/eta_R*(((H[i,j-1])**3/3*(p[i+1,j-1]-2*p[i,j-1]+p[i-1,j-1])/\
#        (deltax**2)+((H[i,j-1])**2*(H[i+1,j-1]-H[i-1,j-1])/2/deltax * \
#        ((p[i+1,j-1]-p[i-1,j-1])/2/deltax))))
#        
#        w11 = dT/eta_R*(((H[i,j-1])**3/3*(p[i+1,j-1]-2*p[i,j-1]+p[i-1,j-1])/\
#        (deltax**2)))
#        w111 = (H[i,j-1])**3/3
#        w112 = (p[i+1,j-1]-2*p[i,j-1]+p[i-1,j-1])
#        
#        w12 = dT/eta_R*((H[i,j-1])**2*(H[i+1,j-1]-H[i-1,j-1])/2/deltax * \
#        ((p[i+1,j-1]-p[i-1,j-1])/2/deltax))
#              
#        w2 = dT/eta_R*(-(((H[i+1,j-1]-H[i-1,j-1])/2/deltax)*H[i,j-1]*\
#        taox[i,j-1]+(H[i,j-1])**2/2*(taox[i+1,j-1]-taox[i-1,j-1])/2/deltax))
#        print 'w1'
#        print w1
#        print 'w2'
#        print w2
#        print 'w111'
#        print w111
#        print 'w112'
#        print w112
        
        H[i,j] = H0+w[i,j]
        
    for i in range(5,xSteps-5): 
        ux[i,j] = dT/eta_R*(taox[i,j-1]*H[i,j-1]-(H[i,j-1])**2/2*(p[i+1,j-1]-p[i-1,j-1])/2/deltax)+ux[i,j-1]
#        ux1 = dT/eta_R*(taox[i,j-1]*H[i,j-1]-(H[i,j-1])**2/2*(p[i+1,j-1]-p[i-1,j-1])/2/deltax)
#        ux2 = ux[i,j-1]
#        print 'ux1'
#        print ux1
#        print 'ux2'
#        print ux2
        ux[2,j]=0
        ux[xSteps-3,j]=0
                
    for i in range(2,xSteps-2): 
        Nxx[i,j] = sigma0*h + Ef*h/(1-nu_f**2)*((ux[i+1,j]-ux[i-1,j])/2/deltax + 0.5*((w[i+1,j]-w[i-1,j])/2/deltax)**2)
#        Nxx1 = sigma0*h
#        Nxx2 = Ef*h/(1-nu_f**2)*((ux[i+1,0]-ux[i-1,0])/2/deltax + 0.5*((w[i+1,0]-w[i-1,0])/2/deltax)**2)
#        print 'Nxx1'
#        print Nxx1
#        print 'Nxx2'
#        print Nxx2
        
#    Nxx[0,j] = Nxx[1,j]
#    Nxx[xSteps-1,j] = Nxx[xSteps-2,j]
#    Nxx[0,j] = sigma0*h
#    Nxx[xSteps-1,j] = sigma0*h
    
    for i in range(2,xSteps-2): 
        taox[i,j] = (Nxx[i+1,j]-Nxx[i-1,j])/2/deltax
        
#    taox[0,j] = taox[1,j]
#    taox[xSteps-1,j] = taox[xSteps-2,j]

#    p[0,j] = 0
#    p[xSteps-1,j] = 0
#    p[1,j] = p[0,j]
##            p[1,j] = 0
#    p[xSteps-2,j] = p[xSteps-1,j]     
    
    for i in range(2,xSteps-2): 
        if w[i,j] > 0:
            p[i,j] = Df*((w[i-2,j]-4*w[i-1,j]+6*w[i,j]-4*w[i+1,j]+w[i+2,j])/(deltax**4))-Nxx[i,j]*((w[i+1,j]-2*w[i,j]+w[i-1,j])/(deltax**2))-\
            taox[i,j]*((w[i+1,j]-w[i-1,j])/2/deltax)-S*w[i,j]
            p1 = Df*((w[i-2,0]-4*w[i-1,0]+6*w[i,0]-4*w[i+1,0]+w[i+2,0])/(deltax**4))
            p2 =  -Nxx[i,0]*((w[i+1,0]-2*w[i,0]+w[i-1,0])/(deltax**2))
            p3 = -taox[i,0]*((w[i+1,0]-w[i-1,0])/2/deltax)-S*w[i,0] 
            p4 = -S*w[i,0]
#            print 'p1'
#            print p1
#            print 'p2'
#            print p2
#            print 'p3'
#            print p3
#            print 'p4'
#            print p4
        else:
            p[i,j] = Df*((w[i-2,j]-4*w[i-1,j]+6*w[i,j]-4*w[i+1,j]+w[i+2,j])/(deltax**4))-Nxx[i,j]*((w[i+1,j]-2*w[i,j]+w[i-1,j])/(deltax**2))-\
            taox[i,j]*((w[i+1,j]-w[i-1,j])/2/deltax)
            p5 = Df*((w[i-2,0]-4*w[i-1,0]+6*w[i,0]-4*w[i+1,0]+w[i+2,0])/(deltax**4))
            p6 =  -Nxx[i,0]*((w[i+1,0]-2*w[i,0]+w[i-1,0])/(deltax**2))
            p7 = -taox[i,0]*((w[i+1,0]-w[i-1,0])/2/deltax)-S*w[i,0] 
#            print 'p5'
#            print p5
#            print 'p6'
#            print p6
#            print 'p7'
#            print p7    
#        print i
#    p[0,j] = 0
#    p[xSteps-1,j] = 0
#    p[1,j] = p[2,j]
##            p[1,j] = 0
#    p[xSteps-2,j] = p[xSteps-3,j]
##            p[xSteps-2,j] = 0
#    p[0,j] = p[1,j] 
#    p[xSteps-1,j] = p[xSteps-2,j]
#    p[0,j] = 0
#    p[xSteps-1,j] = 0
    
 
figure   
plt.plot(w[:,0],'k')
plt.plot(w[:,2],'b')
plt.plot(w[:,Points/2],'g')
plt.plot(w[:,Points-1],'r')