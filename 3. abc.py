from cmath import cos, pi, sqrt
from math import e
import numpy as np
import random
import pandas as pd
import basic
import copy
np.set_printoptions(suppress=True)


dim=7
pop_size=12
obj=4
ttl=5
iter=500

def employeebee(population,ttlarray):
    new_population=[]
    new_ttlarray=[]
    for i in range(pop_size):
        x1=population[i]
        x2=population[random.randint(0,pop_size-1)]
        
        pos=random.randint(0,dim-1)
        u=copy.deepcopy(x1)
        u[pos]=x1[pos]+(random.uniform(-1,+1)*np.subtract(x1[pos],x2[pos]))
        objvals=basic.objfunction([x1,u],obj)
        
        if(objvals[0]<=objvals[1]):
            new_population.append(x1)
            new_ttlarray.append(ttlarray[i]+1)
        else:
            new_population.append(u)
            new_ttlarray.append(0)
            
    return (new_population,new_ttlarray)    
    
def onlookerbee(population,ttlarray):
        objvals=basic.objfunction(population,obj)
        population= [x for _, x in sorted(zip(objvals, population), key=lambda x: x[0])]
        objvals=sorted(objvals)
        fitnessarray=1./(1+np.array(objvals))
        fitnessarray=np.cumsum(fitnessarray/sum(fitnessarray))
        # print("Population:", np.array(population))
        
        
        new_population=[]
        new_ttlarray=[]
        for _ in range(pop_size):
            p=random.uniform(0,1)
            index=fitnessarray.searchsorted(p)
            # print("p: ",p, " index: ",index)
            x1=population[index]
            x2=population[random.randint(0,pop_size-1) ]
            
            pos=random.randint(0,dim-1)
            u=copy.deepcopy(x1)
            u[pos]=x1[pos]+(random.uniform(-1,+1)*(x1[pos]-x2[pos])).astype(int)
            
            
            
            objvals=basic.objfunction([x1,u],obj)
            if(objvals[0]<=objvals[1]):
                new_population.append(x1)
                new_ttlarray.append(ttlarray[index]+1)
            else:
                new_population.append(u)
                new_ttlarray.append(0)
        
        return (new_population,new_ttlarray)
    
def scoutbee(population,ttlarray):
        while(np.max(ttlarray)>=ttl):
            pos=ttlarray.index(np.max(ttlarray))
            population.pop(pos)
            ttlarray.pop(pos)
            [solution]=basic.initialise(1,dim)
            population.append(solution)
            ttlarray.append(0)
            
        return (population,ttlarray)
    
def main():
    population=basic.initialise(pop_size,dim)
    ttlarray=np.zeros(pop_size)
    objvals=basic.objfunction(population,obj)    
    min=objvals.index(np.min(objvals))
    max=objvals.index(np.max(objvals))
    bestobjval=objvals[min]
    bestsoln=population[min]

    for i in range (iter):
        population,ttlarray=employeebee(population,ttlarray)
        
        population,ttlarray=onlookerbee(population,ttlarray)
        
        objvals=basic.objfunction(population,obj)
        
        min=objvals.index(np.min(objvals))
        max=objvals.index(np.max(objvals))
        if(objvals[min]<=bestobjval):
            bestobjval=objvals[min]
            bestsoln=population[min]
        else:
            population.pop(max)
            objvals.pop(max)
            ttlarray.pop(max)
            population.insert(0,bestsoln)
            objvals.insert(0,bestobjval)
            ttlarray.insert(0,0)
            
        population,ttlarray=scoutbee(population,ttlarray)
        
        
        
    objvals=basic.objfunction(population,obj)
    population= [x for _, x in sorted(zip(objvals, population), key=lambda x: x[0])]
    objvals=sorted(objvals)
    
    
    print()
    print("Population:")
    for solution in population:
        print(solution)
    print()
    print("TTL Values:")
    print(ttlarray)
    print()
    print("Objective Function Values:")
    print(objvals)    
    
main()