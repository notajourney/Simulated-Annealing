# -*- coding: utf-8 -*-
"""
@author: ofersh@telhai.ac.il
Simulated Annealing on a continuous domain bounded within [lb,ub]**n
"""
import numpy as np
import matplotlib.pyplot as plt
import objFunctions as fct

def SimulatedAnnealing(n, max_evals, variation=lambda x: x+np.random.normal(size=len(x)), func=lambda x: x.dot(x), seed=None) :
    T_init=6.0 #initial temp
    T_min=1e-4 #minimal temp
    alpha=0.99 # the factor that shrinks the temp
    f_lower_bound = 0#??
    eps_satisfactory = 1e-5#??
    max_internal_runs = 50 # for internal loop
    local_state = np.random.RandomState(seed)#??
    history = []
    
    
    xbest = xmin = local_state.uniform(size=n)*(ub - lb) + lb# we need to randomize +-1 vector of dim=100
    fbest = fmin = func(xmin)#stays the same
    eval_cntr = 1
    T = T_init
    history.append(fmin)
    
    
    while ((T > T_min) and eval_cntr < max_evals) :
        for _ in range(max_internal_runs) :
            x = variation(xmin)# variation is the step
                                # we need to implement step in discrete space
            f_x = func(x)#func = swidish :: here we evaluate the new vector
            eval_cntr += 1
            dE = f_x - fmin 
            if dE <= 0 or local_state.uniform(size=1) < np.exp(-dE/T) :
                xmin = x
                fmin = f_x
            if dE < 0 :
                fbest=f_x
                xbest=x
            history.append(fmin)
            if np.mod(eval_cntr,int(max_evals/10))==0 :
                print(eval_cntr," evals: fmin=",fmin)
            if fbest < f_lower_bound+eps_satisfactory :
                T=T_min
                break
        T *= alpha
    return xbest,fbest,history
#
if __name__ == "__main__" :
    lb,ub = -5,5
    n=10
    evals=10**5
    Nruns=10
    fbest = []
    xbest = []
    for i in range(Nruns) :
        xmin,fmin,history = SimulatedAnnealing(n,lb,ub,evals,lambda x: x+np.random.normal(size=len(x)),fct.WildZumba,i+17)
        plt.semilogy(history)
        plt.show()
        print(i,": minimal Zumba found is ", fmin," at location ", xmin)
        fbest.append(fmin)
        xbest.append(xmin)
    print("====\n Best ever: ",min(fbest),"x*=",xbest[fbest.index(min(fbest))])