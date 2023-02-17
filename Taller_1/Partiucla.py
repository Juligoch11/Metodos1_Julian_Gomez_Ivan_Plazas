#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 11 21:55:24 2023

@author: julianeduardogomezchavarro
"""


import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as anim
from tqdm import tqdm
from time import sleep

class Particle:
    
    def __init__(self,r0,v0,a0,t,m=1,radius=0.3,Id=0):
        
        self.dt = t[1] - t[0]
        
        self.r = r0
        self.v = v0
        self.a = a0
        
        self.R = np.zeros((len(t),len(r0)))
        self.V = np.zeros_like(self.R)
        self.A = np.zeros_like(self.R)
        
        self.radius = radius
        
    def Evolution(self,i):
        
        self.SetPosition(i)
        self.SetVelocity(i)
        
        self.r += self.dt*self.v
        self.v += self.dt*self.a
        
    def SetPosition(self,i):
        self.R[i] = self.r
        
    def GetPosition(self,scale=1):
        return self.R[::scale]
    
    def SetVelocity(self,i):
        self.V[i] = self.v

    def GetVelocity(self,scale=1):
        return self.V[::scale]

    def CheckLimits(self,Limits):
        
        for i in range(2):
        
            if self.r[i] + self.radius > Limits[i][1] and self.v[i] > 0.:
                self.v[i] = -1.0*self.v[i]
            if self.r[i] - self.radius < Limits[i][0] and self.v[i] < 0.:
                self.v[i] = -1.0*self.v[i]
    def RunSimulation1(t,Wall):
    
        r0 = np.array([0.1,0.1])
        v0 = np.array([1.,5.])
        a0 = np.array([0.,0])
    
    
        p1 = Particle(r0,v0,a0,t)
    
        Wall_ = Wall.copy()
    
    
        for it in tqdm(range(len(t)), desc='Running simulation', unit=' Steps'):
           sleep(0.0001)
           p1.Evolution(it)
           p1.CheckLimits(Wall_)
    
        return p1
    
scale=1
t=[:,scale]

fig = plt.figure(figsize=(5,5))
ax = fig.add_subplot(111)


def init():
        ax.set_xlim(Limits[0][0],Limits[0][1])
        ax.set_ylim(Limits[1][0],Limits[1][1])
    
def Update(i):
    
    ax.clear()
    init()
    ax.set_title(r'$ t=%.2f \ s$' %(t[i]))
    
     
    x = Particles.GetPosition(scale)[i,0]
    y = Particles.GetPosition(scale)[i,1]
    vx = Particles.GetVelocity(scale)[i,0]
    vy = Particles.GetVelocity(scale)[i,1]
    
    circle = plt.Circle((x,y),Particles.radius, fill=True, color='k')
    ax.add_patch(circle)
    
    ax.arrow(x,y,vx,vy,color='r',head_width=0.2,length_includes_head=True)
    
    
Animation = anim.FuncAnimation(fig,Update,frames=len(t),init_func=init)
