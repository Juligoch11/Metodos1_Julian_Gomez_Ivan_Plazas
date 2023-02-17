#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 11 21:27:31 2023

@author: julianeduardogomezchavarro
"""
import numpy as np
def factorial(n)->int:
    fact=1
    if n==0 or n==1:
        return fact
    c=n+1
    z= np.zeros(c,dtype=int)
    z[0]=fact
   
    if n > 20:
        
        for i in range(1,c):
            fact*=i
            z[i]=fact
    else:
        for i in range(1,c):
            fact*=i
            z[i]=fact
    return z


    
print (factorial(12))