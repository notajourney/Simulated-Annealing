# -*- coding: utf-8 -*-
"""
@author: ofersh@telhai.ac.il
Hill-Climber on a continuous domain bounded within [lb,ub]**n
"""
import numpy as np
import matplotlib.pyplot as plt
import objFunctions as fct

def basicHillClimber(n, evals, func=lambda x: x.dot(x)) :
    history = []
    #randomize vector  of +1 -1 sized n into --> xmax
    xmax =  2*np.random.randint(0,2, size=n)-1
    fmax = func(xmax)# the first  is the minimal
    
    history.append(fmax)# adding to histoy of mininma
    
    for _ in range(evals) :
        x = step(xmax,n,2)#discrete step::Default step = 1. means:closest neighbor
     
        f_x = func(x)#evaluate the new vector
        if f_x > fmax :#checking if the new vector is "better" then previous vector (we need to maximaize)
            xmax = x# if better: x min = x
            fmax = f_x
        history.append(fmax)
    return xmax,fmax,history
#
    

def step(vec, n, neighbor_order):
    temp = vec.copy()
    
    
    for x in range(neighbor_order):

        index = np.random.randint(0,n)
        temp[index] = -1*temp[index]
        
    return temp
  
    
if __name__ == "__main__" :
    
    n=100
    evals=10**5#number of calls to objective
    xmax,fmax,history = basicHillClimber(n,evals,fct.SwedishPump)
    plt.semilogy(history)#plot (not interessting)
    print("Hill Climber:maximal SwedishPump found is ", fmax)#" at location ", xmax)
    

    