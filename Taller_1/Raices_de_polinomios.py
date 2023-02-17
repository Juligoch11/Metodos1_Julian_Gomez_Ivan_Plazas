#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 11:33:44 2023

@author: julianeduardogomezchavarro
"""
import numpy as np


def f(x):
    return ((3*(x)**5)+(5*(x)**4)-((x)**3))

def CentralDerivative(x, h=0.001):
        return ((f(x+h) - f(x-h))/(2*h))

def newtrap(x):
        
    newx = x - f(x)/CentralDerivative(x)
    
    return newx

def solution():
  
   final=np.array([])
   raices= np.array([])
   valores= np.linspace(-3,5,100)
   
   for c in range(len(valores)):
       dato=valores[c] 
       for i in range(100):
           dato=newtrap(dato)
           total= round(dato,2)
       raices= np.append(raices,total)   
   for j in range(len(raices)):
       if raices[j]== -0:
           raices[j]= abs(raices[j])
       if raices[j] in final:
           final=final
       else:
           final=np.append(final,raices[j])
 
   return final
print(solution())

