#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Este trabalho está licenciado sob a Licença Creative Commons Atribuição-CompartilhaIgual 3.0 Não Adaptada. Para ver uma cópia desta licença, visite https://creativecommons.org/licenses/by-sa/3.0/ ou envie uma carta para Creative Commons, PO Box 1866, Mountain View, CA 94042, USA.

Author: Pedro H A Konzen - 10/2016

Descrição:
Calcule as iterações do ponto fixo para $g(x) = \cos(x)$ com aproximação inicial $x^{(1)} = 0,7$, estime o erro absoluto da aproximação e verfique a taxa de convergência.
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

#ax.set_ylim(-175,300)

#ponto fixo
#funcao do pto. fixo
def g(x):
    return np.cos(x)

#est. da solucao
xe = sci.optimize.fixed_point(g, 0.7)

#aprox. inicial
x = [0.7]
eps = [np.fabs(x[0]-xe)]
print("%1.5f %1.1e\n" % (x[0], eps[0]))

for i in np.arange(6):
  x.append(g(x[i]))
  eps.append(np.fabs(x[i+1]-xe))
  print("%1.5f %1.1e\n" % (x[i+1], eps[i+1]))
  x0 = x


#pontos
xi = np.arange(1,8)
yi = eps
ax.plot(xi, yi, 'ko-', markersize=3,
        markeredgecolor="blue", markerfacecolor="blue")

#taxa de convergencia linear
def r(x):
    return eps[0]*(0.85-1)*(x-1) + eps[0]

plt.plot(xi,r(xi),'k--')

ax.text(3.5,0.0275,r"$\beta = 0,\!85$",backgroundcolor="white")

ax.set_xlabel(r"$n$")
ax.set_ylabel(r"$\epsilon_n$")

ax.set_yticks([0.0, 0.01,0.02,0.03,0.04])
ax.set_yticklabels(["$0,\!00$", "$0,\!01$", "$0,\!02$", "$0,\!03$", "$0,\!04$"])

fig_file =  "ex_ponto_fixo_3"
fig.savefig(fig_file+".eps", bbox_inches='tight')
fig.savefig(fig_file+".svg", bbox_inches='tight')
fig.savefig(fig_file+".png", bbox_inches='tight')


