#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 11 21:27:31 2023

@author: julianeduardogomezchavarro
"""
import numpy as np
def factorial(n)->int:
    fact=1
    z= np.zeros(n,dtype=int)
    z[1]=fact
    if n==0 or n==1:
        return fact
    elif n > 20:
        
        for i in range(2,n):
            fact*=i
            z[i]=fact
    else:
        for i in range(2,n):
            fact*=i
            z[i]=fact
    return z


    
print (factorial(6))