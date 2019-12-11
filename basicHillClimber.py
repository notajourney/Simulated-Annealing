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
    #randomize vector  of +1 -1 sized n into --> xmin
    fmin = func(xmin)# the first  is the minimal
    
    history.append(fmin)# adding to histoy of mininma
    
    for _ in range(evals) :
        x = xmin + np.random.normal(size=n)## step: we need to imolement discrete step:
        # generate a random between zero to n-1 and flip that coordinate(multiply by -1)
        f_x = func(x)#evaluate the new vector
        if f_x < fmin :#checking if the new vector is "better" then previous vector (we need to maximaize)
            xmin = x# if better: x min = x
            fmin = f_x
        history.append(fmin)
    return xmin,fmin,history
#
if __name__ == "__main__" :
    
    n=100
    evals=10**3#number of calls to objective
    xmin,fmin,history = basicHillClimber(n,evals,fct.SwedishPump)
    plt.semilogy(history)#plot (not interessting)
    print("minimal Zumba found is ", fmin," at location ", xmin)