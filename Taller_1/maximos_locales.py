#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 11 21:30:28 2023

@author: julianeduardogomezchavarro
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def maximos_locales(name:str):
    
    L= np.array([])
    archivo=open(name, "r")
    linea=archivo.readline()
    while len(linea)!=0:
        datos= linea.replace("\n", "").split()
        columna=(float(datos[0]),float(datos[1]))
        L=np.append(L,columna)
        
        
        linea=archivo.readline()
    c=int(len(L)/2)
    L=L.reshape(c,2)
    
    maximos=np.array([])
    for i in range(1, len(L) - 1):
        if (L[i][1] > L[i - 1][1]) and (L[i][1] > L[i + 1][1]):
           maximos=np.append(maximos, L[i])
    d=int(len(maximos)/2)
    maximos=maximos.reshape(d,2)
    columnas=["x","y"]
    dt_lista= pd.DataFrame(L, columns=columnas)
    dt_maximuns= pd.DataFrame(maximos, columns=columnas)
    return dt_lista,dt_maximuns  
def visor(datos,datos2):
    plt.figure()
    subplot= datos.plot("x","y", legend=None)
    datos2.plot(kind="scatter", x="x",y="y", color="r", marker="o", ax=subplot)
   
    plt.show()
 
       
x,d=maximos_locales("EstrellaEspectro.txt")
visor(x,d)
     
    


