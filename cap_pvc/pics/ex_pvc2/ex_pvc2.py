#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Este trabalho está licenciado sob a Licença Creative Commons Atribuição-CompartilhaIgual 3.0 Não Adaptada. Para ver uma cópia desta licença, visite https://creativecommons.org/licenses/by-sa/3.0/ ou envie uma carta para Creative Commons, PO Box 1866, Mountain View, CA 94042, USA.

Author: Pedro H A Konzen - 10/2016

Descrição:
Gráfico das soluções analítica e numérica de
  \begin{eqnarray}
    -u_{xx} &=& 100(x-1)^2,\quad 0 < x < 1,\\
    u(0) &=& 0,\\
    u(1) &=& 0.
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

#analitica
def ua(x):
    return -100*(x-1)**4/12 - 100*x/12 + 100/12


xx = np.linspace (0, 1)
yy = np.zeros_like(xx)
for i,x in enumerate(xx):
    yy[i] = ua(x)

ax.plot(xx,yy,'b-')

#numerica
def un(N):
    #malha
    a = 0
    b = 1
    h = (b-a)/(N-1)
    xp = np.linspace(a,b,N)

    A = np.zeros((N,N))
    b = np.zeros(N)

    A[0,0] = 1
    b[0] = 0
    for i in np.arange(1,N-1):
        A[i,i-1] = 1
        A[i,i] = -2
        A[i,i+1] = 1
        b[i] = - 100 * h**2 * (xp[i]-1)**2
    A[N-1,N-1] = 1
    b[N-1] = 0

    u = np.linalg.solve(A,b)
    return (xp,u)

xx, uh = un(11)
ax.plot(xx, uh, 'ro', markersize=4)

fig_file =  "ex_pvc2"
fig.savefig(fig_file+".eps", bbox_inches='tight')
fig.savefig(fig_file+".svg", bbox_inches='tight')
fig.savefig(fig_file+".png", bbox_inches='tight')


