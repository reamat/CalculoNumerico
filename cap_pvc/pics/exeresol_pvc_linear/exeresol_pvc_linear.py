#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Este trabalho está licenciado sob a Licença Creative Commons Atribuição-CompartilhaIgual 3.0 Não Adaptada. Para ver uma cópia desta licença, visite https://creativecommons.org/licenses/by-sa/3.0/ ou envie uma carta para Creative Commons, PO Box 1866, Mountain View, CA 94042, USA.

Author: Pedro H A Konzen - 10/2016

Descrição:
Gráfico das solução numérica de
  \begin{eqnarray}
    -u_{xx} + u  &=& e^{-x},\quad 0<x<1,\\
    u(0,5) &=& 1,\\
    u(1,5) &=& 2.
  \end{eqnarray}
'''

from __future__ import division
import numpy as np
from numpy import linalg
import matplotlib.pyplot as plt

#font letter
plt.rc('text', usetex=True)
plt.rc('font', family='serif', size=12)

#canvas
fig = plt.figure(figsize=(3,3), dpi=300, linewidth=0.0, facecolor="white")

#axes definitions
ax = plt.subplot(1,1,1)

ax.grid()

#numerica
def un(N):
    #malha
    a = 0.5
    b = 1.5
    N = 11
    h = (b-a)/(N-1)
    x = np.linspace(a,b,N)
    
    A = np.zeros((N,N))
    b = np.zeros(N)
    
    A[0,0] = 1
    b[0] = 1
    for i in np.arange(1,N-1):
        A[i,i-1] = -1
        A[i,i] = 2 + h**2
        A[i,i+1] = -1
        b[i] = h**2 * np.exp(x[i])
    A[N-1,N-1] = 1
    b[N-1] = 2
    
    u = np.linalg.solve(A,b)
    
    return (x,u)

xx, uh = un(11)
ax.plot(xx, uh, 'b-o', markersize=4)

ax.set_xlim(0.5,1.5)
ax.set_xticks(np.linspace(0.5,1.5,5))
ax.set_ylim(1,2)

fig_file =  "exeresol_pvc_linear"
fig.savefig(fig_file+".eps", bbox_inches='tight')
fig.savefig(fig_file+".svg", bbox_inches='tight')
fig.savefig(fig_file+".png", bbox_inches='tight')


