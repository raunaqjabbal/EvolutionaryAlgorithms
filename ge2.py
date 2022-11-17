from cmath import cos, pi, sqrt
from math import e
import numpy as np
import random

dim=5
pop_size=10
decoder=[]
bits=5
Obj=4

prob=1/(bits*dim)
# print("prob= ",prob)
def initialise():
    
    for i in range(bits-1,-1,-1):
        decoder.append(2**i)
    # print("decoder: "decoder)
    
    population=[]
    for i in range(pop_size):
        solution=[]
        for j in range(dim):
            solution.append([random.randint(0, 1)for _ in range(bits)])
        population.append(np.array(solution))
        
    return population
   

def decode(population):
    decoded_population=[]
    for solution in population:
        summation=[]
        # print("Encoded Vals: ",solution)
        for i in range (len(solution)):
            summation.append( sum([a*b for a,b in zip(solution[i],decoder)]) )
        # print("Decoded Vals: ",summation)
        decoded_population.append(summation)
    return decoded_population


def objfunction(population):
    decoded_population=decode(population)
    objvals=[]
    
    for decoded in decoded_population:
        objval=0
        if (Obj==1):
            objval=10*dim
            for val in decoded:
                objval = objval +(val*val-10*cos(2*pi*val))
                objval = objval.real          
                
        if (Obj==2):
            x=-20*e**(-0.2*sqrt(0.5*(decoded[0]**2+decoded[1]**2)))
            y=e**( 0.5* (cos(2*pi*decoded[0])+cos(2*pi*decoded[1])))
            objval=x-y+e+20
            objval=objval.real
        
        if (Obj==3):
            for a in decoded:
                objval=objval+a**2
        
        if (Obj==4):
            for i in range(dim-1):
                x=100*((decoded[i+1]-decoded[i]**2)**2)
                y=(1-decoded[i])**2
                objval=objval+x+y
        objvals.append(int(objval))
    
    return objvals
               
def crossover(a, b):
    c=[]
    for i in range(dim):    
        point = random.randint(1, bits - 2)
        c.append( np.hstack((a[i][0:point], b[i][point:])) )
    return np.array(c)

def mutation(a):
    for i in range(dim):    
        for j in range(bits):
            x=random.uniform(0,1)
            a[i][j] = int(not a[i][j]) if  x<= prob else a[i][j]
    return np.array(a)

def selection(population,objvals):
    new_population=[]
    new_objvals=[]
    for i in range(pop_size):
        a=random.randint(0, pop_size-1)
        b=random.randint(0, pop_size-1)
        
        if(objvals[a]<=objvals[b]):
            new_population.append(population[a])
            #new_objvals.append(objvals[a])
        else:
            new_population.append(population[b])
            #new_objvals.append(objvals[b])

    return new_population

def reproduction(population):
    new_population=[]
    for i in range(pop_size):
        a=random.randint(0, pop_size-1)
        b=random.randint(0, pop_size-1)
        
        new_solution=crossover(population[a],population[b])
        new_solution=mutation(new_solution)
        
        new_population.append(new_solution)
        
    return new_population
        

def main():
    population=initialise()
    objvals=objfunction(population)    
    min=objvals.index(np.min(objvals))
    max=objvals.index(np.max(objvals))
    bestobjval=objvals[min]
    bestsoln=population[min]

    
    for i in range (1000):
        population=selection(population,objvals)
        population=reproduction(population)
        
        
        objvals=objfunction(population)
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
        
        
    
    objvals=objfunction(population)
    population= [x for _, x in sorted(zip(objvals, population), key=lambda x: x[0])]
    objvals=sorted(objvals)
    
    print()
    print("Solutions:")
    for solution in decode(population):
        print(solution)
    print()
    print("Objective Function Values:")
    print(objvals) 
    
    
main()