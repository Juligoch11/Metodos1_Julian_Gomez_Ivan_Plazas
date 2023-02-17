#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 19:38:27 2023

@author: julianeduardogomezchavarro
"""
import numpy as np
import matplotlib.pyplot as plt
R=2
x = np.linspace(-4,4,25)
y = np.linspace(-4,4,25)
def f(x,y,V=2,R=2):
    return V*x*(1 - R**2/(x**2+y**2))
def CentralDerivativex(f,x,y,h):
    return (f(x+h,y) - f(x-h,y))/(2*h)
def CentralDerivativey(f,x,y,h):
    return -(f(x,y+h) - f(x,y-h))/(2*h)
datosx = np.zeros((25,25))
datosy = np.zeros((25,25))
for i in range(len(x)):
    for j in range(len(y)):
        
        if (x[i]**2 + y[j]**2 > R**2):
        
            datosx[i,j] = CentralDerivativex(f,x[i],y[j],0.001)
            datosy[i,j] = CentralDerivativey(f,x[i],y[j],0.001)
            
fig1 = plt.figure(figsize=(10,10))
ax = fig1.add_subplot(1,1,1)

circle = plt.Circle((0,0),R,color='r',lw=2,fill=False)

ax.add_artist(circle)

for i in range(x.shape[0]):
    for j in range(y.shape[0]):
        if (x[i]**2 + y[j]**2 > R**2):
            ax.quiver(x[i],y[j],datosx[i,j],datosy[i,j],color='b',alpha=0.7)
        
        
ax.set_xlabel(r'$x[cm]$',fontsize=15)
ax.set_ylabel(r'$y[cm]$',fontsize=15)

plt.savefig('FlujoCilindro.pdf')