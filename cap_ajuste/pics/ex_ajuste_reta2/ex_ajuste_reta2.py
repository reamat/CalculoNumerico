#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Este trabalho está licenciado sob a Licença Creative Commons Atribuição-CompartilhaIgual 3.0 Não Adaptada. Para ver uma cópia desta licença, visite https://creativecommons.org/licenses/by-sa/3.0/ ou envie uma carta para Creative Commons, PO Box 1866, Mountain View, CA 94042, USA.

Author: Pedro H A Konzen - 10/2016

Descrição:
Reta que melhor se ajusta aos pontos dados na seguinte tabela:
\begin{equation*}
\begin{array}{l|ccccc}
i & 1   & 2  & 3 & 4 &  5\\\hline
x_i&0,01&1,02&2,04&2,95&3,55\\
y_i&1,99&4,55&7,20&9,51&10,82
\end{array}
\end{equation*}

Solução: y =  1,9988251 + 2,5157653x.
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


#pontos
xi = [0.01,1.02,2.04,2.95,3.55]
yi = [1.99,4.55,7.2,9.51,10.82]
ax.plot(xi, yi, 'ro', markersize=3, markeredgecolor="red")

ax.set_xticks(xi)
ax.set_yticks(yi)

#reta
def r(x):
    return 1.9988251 + 2.5157653*x

xx = np.linspace (-0.25, 3.75)
ax.plot(xx, r(xx), 'b-')
ax.set_title("$y =  1,\!9988251 + 2,\!5157653x$")


fig_file =  "ex_ajuste_reta2"
fig.savefig(fig_file+".eps", bbox_inches='tight')
fig.savefig(fig_file+".svg", bbox_inches='tight')
fig.savefig(fig_file+".png", bbox_inches='tight')


