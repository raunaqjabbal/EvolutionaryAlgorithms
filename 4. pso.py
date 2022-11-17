import numpy as np
import random
import pandas as pd
import basic
from copy import deepcopy
np.set_printoptions(suppress=True)

dim=5
pop_size=10
obj=4
c1=0.5
c2=0.5
iter=1000
alpha=1

def v2(population,v,pbest,gbest):
    for i in range(pop_size):
        term1=c1*random.uniform(0,1)*(pbest[i]-population[i])
        term2=c2*random.uniform(0,1)*(gbest-population[i])
        v[i]=alpha*(v[i]+term1+term2)
        v[i]=np.clip(v[i],-8,8)
        
def main():
    population=basic.initialise(pop_size,dim)
    v=basic.initialise(pop_size,dim)
    
    pbest=population    
    pbestval=basic.objfunction(population,obj)
    gbestval=min(pbestval)
    gbest=population[pbestval.index(gbestval)]
    
    for i in range (iter):
        v2(population,v,pbest,gbest)    
        population=population+v
        
        objvals=basic.objfunction(population,obj)
        
        for i in range(pop_size):
            if pbestval[i]>=objvals[i]:
                pbest[i]=population[i]
                pbestval[i]=objvals[i]
    
                if gbestval>=pbestval[i]:
                    gbest=population[i]
                    gbestval=pbestval[i]
                    
        
        
    # objvals=basic.objfunction(population,obj)
    # population= [x for _, x in sorted(zip(objvals, population), key=lambda x: x[0])]
    # objvals=sorted(objvals)
    
    
    print()
    print("GBESTVAL: ",gbestval)
    print(gbest)
    print()
    print("PBESTVAL: ",pbestval)
    print(pbest)
    print()
    # print("Objective Function Values:")
    # print(objvals)   
    # print()
    # print("Population:")
    # for solution in population:
    #     print(solution)
     
main()