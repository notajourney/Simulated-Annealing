# -*- coding: utf-8 -*-
"""
@author: ofersh@telhai.ac.il
Hill-Climber on a continuous domain bounded within [lb,ub]**n
"""
import numpy as np
import matplotlib.pyplot as plt
import objFunctions as fct

def basicHillClimber(n, lb, ub, evals, func=lambda x: x.dot(x)) :
    history = []
    xmin = np.random.uniform(size=n)*(ub - lb) + lb
    fmin = func(xmin)
    history.append(fmin)
    for _ in range(evals) :
        x = xmin + np.random.normal(size=n)
        f_x = func(x)
        if f_x < fmin :
            xmin = x
            fmin = f_x
        history.append(fmin)
    return xmin,fmin,history
#
if __name__ == "__main__" :
    lb,ub = -5,5
    n=2
    evals=10**5
    xmin,fmin,history = basicHillClimber(n,lb,ub,evals,fct.WildZumba)
    plt.semilogy(history)
    print("minimal Zumba found is ", fmin," at location ", xmin)