#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Este trabalho está licenciado sob a Licença Creative Commons Atribuição-CompartilhaIgual 3.0 Não Adaptada. Para ver uma cópia desta licença, visite https://creativecommons.org/licenses/by-sa/3.0/ ou envie uma carta para Creative Commons, PO Box 1866, Mountain View, CA 94042, USA.

Author: Pedro H A Konzen - 11/2016

Descrição:
Gráfico do erro $|Df(1) - f'(1)|$, onde:
Df(1) = \frac{\cos(1 + h) - \cos(1)}{h}
e
f'(1) = -sin(1)
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

ax.set_xlim(1e-1,1e-10)


#pontos
hh = [1e-1, 1e-2, 1e-3, 1e-4, 1e-5, 1e-6, 1e-7, 1e-8, 1e-9, 1e-10]

def erro(h):
    Df = (np.cos(1+h)-np.cos(1))/h
    return np.abs(Df + np.sin(1))

ee = []
for i,h in enumerate(hh):
    ee.append(erro(h))
    
ax.plot(hh, ee, 'bo-', markersize=3, markeredgecolor="red")

ax.set_xscale('log',basex=10)
ax.set_yscale('log',basex=10)

ax.set_xticks([1e-1,1e-3,1e-5,1e-7,1e-9])
ax.set_yticks([1e-1,1e-3,1e-5,1e-7,1e-9])

ax.set_xlabel(r"$h$")
ax.set_ylabel(r"$|f'(1)-Df(1)|$")

fig_file =  "ex_derivacao"
fig.savefig(fig_file+".eps", bbox_inches='tight')
fig.savefig(fig_file+".svg", bbox_inches='tight')
fig.savefig(fig_file+".png", bbox_inches='tight')


