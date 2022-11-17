import numpy as np
import random
import basic
import copy
np.set_printoptions(suppress=True)

dim=4
pop_size=20
obj=1
beta=0.5
prob=0.75
iter=100
             
def crossover(population):
    new_population=[]
    for _ in range(pop_size):
        population=np.array(random.sample(list(population),len(population)))
        x=population[0]
        u=mutation(population)
        z=copy.deepcopy(x)
        
        j_dash=random.randint(0,dim-1)          
        for j in range(dim):
            p=random.uniform(0,1)
            if  p<= prob or j==j_dash:
                z[j] = u[j]
        
        objvals=basic.objfunction([z,x],obj)
        if(objvals[0]<objvals[1]):
            new_population.append(z) 
        else:
            new_population.append(x)
    return new_population

def mutation(population):
    x1=population[1]
    x2=population[2]
    x3=population[3]
    u=x1+(beta*np.subtract(x2,x3))
    return np.array(u) 

def main():
    population=basic.initialise(pop_size,dim)
    bestobjval=np.inf
    bestsoln=np.inf
    for i in range (iter):
        population=crossover(population)
        objvals=basic.objfunction(population,obj)
        
        min=objvals.index(np.min(objvals))
        max=objvals.index(np.max(objvals))
        if(objvals[min]<=bestobjval):
            bestobjval=objvals[min]
            bestsoln=population[min]
        else:
            population.pop(max)
            objvals.pop(max)
            population.insert(0,bestsoln)
            objvals.insert(0,bestobjval)
    
    objvals=basic.objfunction(population,obj)
    population= [x for _, x in sorted(zip(objvals, population), key=lambda x: x[0])]
    objvals=sorted(objvals)
    
    print()
    print("Population:")
    for solution in population:
        print(solution)
    print()
    print("objective Function Values:")
    print(objvals)    
    
    # objvals=basic.objfunction([[-1.55249,1.19142,-3.43872,-3.06005]],4)
    # print(objvals)
    
main()
