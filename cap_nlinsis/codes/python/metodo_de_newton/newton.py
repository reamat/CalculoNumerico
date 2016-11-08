from __future__ import division
import numpy as np
from numpy import linalg

def newton(F,JF,x0,TOL,N):
    #preliminares
    x = np.copy(x0).astype('double')
    k=0
    #iteracoes
    while (k < N):
       k += 1
       #iteracao Newton
       delta = -np.linalg.inv(JF(x)).dot(F(x))
       x = x + delta
       #criterio de parada
       if (np.linalg.norm(delta,np.inf) < TOL):
           return x

    raise NameError('num. max. iter. excedido.')
