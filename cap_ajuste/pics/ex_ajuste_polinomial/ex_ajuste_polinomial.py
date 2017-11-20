#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Este trabalho está licenciado sob a Licença Creative Commons Atribuição-CompartilhaIgual 3.0 Não Adaptada. Para ver uma cópia desta licença, visite https://creativecommons.org/licenses/by-sa/3.0/ ou envie uma carta para Creative Commons, PO Box 1866, Mountain View, CA 94042, USA.

Author: Pedro H A Konzen - 10/2016

Descrição:
Polinômio de grau 2 que melhor se ajusta aos pontos dados na seguinte tabela:
\begin{equation*}
\begin{array}{l|ccccc}
i & 1   & 2  & 3 & 4 &  5\\\hline
x_i&0,00&0,25&0,50&0,75&1,00\\
y_i&-153&64&242&284&175
\end{array}
\end{equation*} 

Solução: $p(x) = -165,37143 + 1250,9714x -900,57143x^2$
'''

import numpy as np
import scipy as sci
from scipy import optimize
import matplotlib.pyplot as plt

#font letter
plt.rc('text', usetex=True)
plt.rc('font', family='serif', size=12)

#canvas
fig = plt.figure(figsize=(3,3), dpi=300, linewidth=0.0, facecolor="white")

#axes definitions
ax = plt.subplot(1,1,1)

ax.grid()

ax.set_ylim(-175,300)

#pontos
xi = [0,0.25,0.5,0.75,1]
yi = [-153,64,242,284,175]
ax.plot(xi, yi, 'ro', markersize=3, markeredgecolor="red")

ax.set_xticks(xi)
ax.set_yticks(yi)

#reta
def f(x):
    return -165.37143 + 1250.9714*x -900.57143*x**2

xx = np.linspace (-0.1, 1.25)
ax.plot(xx, f(xx), 'b-')

fig_file =  "ex_ajuste_polinomial"
fig.savefig(fig_file+".eps", bbox_inches='tight')
fig.savefig(fig_file+".svg", bbox_inches='tight')
fig.savefig(fig_file+".png", bbox_inches='tight')


