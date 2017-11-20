#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Este trabalho está licenciado sob a Licença Creative Commons Atribuição-CompartilhaIgual 3.0 Não Adaptada. Para ver uma cópia desta licença, visite https://creativecommons.org/licenses/by-sa/3.0/ ou envie uma carta para Creative Commons, PO Box 1866, Mountain View, CA 94042, USA.

Author: Pedro H A Konzen - 08/2016
'''

import numpy as np
import scipy as sci
from scipy import optimize
import matplotlib.pyplot as plt

#font settings
plt.rc('text', usetex=True)
plt.rc('font', family='serif', size=12)

#canvas
fig = plt.figure(figsize=(3,3), dpi=300)

#axes definitions
ax = plt.subplot(1,1,1)

ax.set_xlim(-1,10)
ax.set_ylim(-1,10)

ax.set_xticks([])
ax.set_yticks([])

ax.set_frame_on(False)

ax.arrow(-1, 0, 11, 0, head_width=0.25,head_length=0.25, length_includes_head=True, facecolor='black')
ax.text(9,-0.75,r"$x$")

ax.arrow(0, -1, 0, 11, head_width=0.25, head_length=0.25, length_includes_head=True, facecolor='black')
ax.text(-0.75, 9, r"$y$")


def fun(x):
    return -0.5*(x-0.5)**1.25 + 8 - np.sin(x)

a = 1
b = 8
x = np.linspace (a, b)

ax.plot(x, fun(x))
ax.text(7,2.75,"$y = g(x)$")

x = np.linspace(-1,9)
ax.plot(x, x, 'k--')
ax.text(6,8.25,"$y = x$")


#ponto fixo
def g(x): return fun(x)-x
xstar = sci.optimize.fsolve(g,5)
print(xstar)
ax.plot([0, xstar], [xstar, xstar],color='gray',ls='dashed')
ax.plot([xstar, xstar], [0, xstar],color='gray',ls='dashed')
ax.plot([-0.1,0.1],[xstar, xstar],'k-')
ax.plot([xstar,xstar],[-0.1, 0.1],'k-')
ax.plot([xstar],[xstar],'ko',markersize=3)
ax.text(xstar-0.25,-0.75,"$x^{\!*}$")
ax.text(-0.75,xstar-0.1,"$x^{\!*}$")

fig_file =  "defn_ponto_fixo"
fig.savefig(fig_file+".eps", bbox_inches='tight')
fig.savefig(fig_file+".pdf", bbox_inches='tight')
fig.savefig(fig_file+".png", bbox_inches='tight')
fig.savefig(fig_file+".svg", bbox_inches='tight')


