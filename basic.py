from cmath import cos, pi, sqrt
from math import e
import numpy as np
import random
import pandas as pd



def initialise(n,dim):
    population=[]
    for i in range(n):
        solution=[]
        for j in range(dim):
            solution.append(random.uniform(-8,8))
        population.append(np.array(solution))
        
    return np.array(population)    
   
def objfunction(population, Obj):
    objvals=[]
    for element in population:
        objval=0
        if (Obj==1):            ##RASTRIGIN
            objval=10*len(element)
            for val in element:
                objval = objval+val**2-10*cos(2*pi*val)    
                objval = objval.real
                
        if (Obj==2):            ##ACKLEY
            x=-20*e**(-0.2*sqrt(0.5*(element[0]**2+element[1]**2)))
            y=e**( 0.5* (cos(2*pi*element[0])+cos(2*pi*element[1])))
            objval=x-y+e+20
            objval=objval.real
        
        if (Obj==3):            ##SPHERE
            for a in element:
                objval=objval+a**2
        
        if (Obj==4):            ##ROSENBROCK
            for i in range(len(element)-1):
                x=(element[i+1]-element[i]**2)**2
                y=(1-element[i])**2
                objval=objval+100*x+y
        
        objvals.append(round(objval,2))
    return objvals