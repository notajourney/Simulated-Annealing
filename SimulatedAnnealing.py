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
    
    
    xbest = xmax = local_state.uniform(size=n)*(ub - lb) + lb# we need to randomize +-1 vector of dim=100
    fbest = fmax = func(xmax)#stays the same
    eval_cntr = 1
    T = T_init
    history.append(fmax)
    
    
    while ((T > T_min) and eval_cntr < max_evals) :
        for _ in range(max_internal_runs) :
            x = variation(xmax)# variation is the step
                                # we need to implement step in discrete space
            f_x = func(x)#func = swidish :: here we evaluate the new vector
            eval_cntr += 1
            dE = f_x - fmax #de is negative iff  f_x is "better" fmax
            if dE <= 0 or local_state.uniform(size=1) < np.exp(-dE/T) :# accepting disimprovment
                xmax = x #updating minimum vector
                fmax = f_x#updating minimum value
                
            if dE < 0 :# saving the global best:: regardless to accepting disaprovment
                fbest=f_x   #this is necessarily the best value we have found so far
                xbest=x     #this is necessarily the best vector we have found so far
                
                
            history.append(fmax)
            
            if np.mod(eval_cntr,int(max_evals/10))==0 :
                print(eval_cntr," evals: fmax=",fmax)
            if fbest < f_lower_bound+eps_satisfactory :
                T=T_min
                break
        T *= alpha
    return xbest,fbest,history



#################################################Step Function#####################################################
def step(vec, n, repeat):
    temp = vec.copy()
    
    
    for x in range(repeat):

        index = np.random.randint(0,n)
        temp[index] = -1*temp[index]
        
    return temp

#################################################Step Function#####################################################
#
if __name__ == "__main__" :
    lb,ub = -5,5
    n=10
    evals=10**5
    Nruns=10
    fbest = []
    xbest = []
    for i in range(Nruns) :
        xmax,fmax,history = SimulatedAnnealing(n,lb,ub,evals,lambda x: x+np.random.normal(size=len(x)),fct.WildZumba,i+17)
        plt.semilogy(history)
        plt.show()
        print(i,": minimal Zumba found is ", fmax," at location ", xmax)
        fbest.append(fmax)
        xbest.append(xmax)
    print("====\n Best ever: ",min(fbest),"x*=",xbest[fbest.index(min(fbest))])