#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 11 21:45:54 2023

@author: julianeduardogomezchavarro
"""

import matplotlib.pyplot as plt
import numpy as np

def sucesion_fibonacci(n:int):
    if n == 0:
        total= 0
    elif n == 1:
        total= 1
    else:
        total= sucesion_fibonacci(n - 1) + sucesion_fibonacci(n - 2)
    return total

def fibonacci_20():
    L=np.array([])
    for i in range(21):
        resultado=sucesion_fibonacci(i)
        L=np.append(L,resultado)
    ejex=np.arange(len(L))
    plt.figure()
    plt.plot(ejex,L)
    plt.show()
    
fibonacci_20()
def numero_aureo(x):
    return (1+5**(1/2))/2

def aureo():
    final=np.zeros(19)
    for j in range(2,21):
        final[j-2]=sucesion_fibonacci(j)/sucesion_fibonacci(j-1)
    x= range(-1,20)
    plt.figure()
    plt.plot(final)
    plt.plot(x, [numero_aureo(i) for i in x], "r--", linewidth=1.75)
    plt.xlim(-0.75,18.5)
    plt.legend(["Estimación usando la serie","Número aureo"])
    
aureo()


