#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Este trabalho está licenciado sob a Licença Creative Commons Atribuição-CompartilhaIgual 3.0 Não Adaptada. Para ver uma cópia desta licença, visite https://creativecommons.org/licenses/by-sa/3.0/ ou envie uma carta para Creative Commons, PO Box 1866, Mountain View, CA 94042, USA.

Author: Picknick - 09/2016

Descrição:
Ilustração do método das secantes.

Description:
Illustration of the secants' method.
'''

import numpy as np
import scipy as sci
from scipy import optimize
import matplotlib.pyplot as plt

#canvas
fig = plt.figure(figsize=(3,3), dpi=300, linewidth=0.0, facecolor="white")

#axes definitions
ax = plt.subplot(1,1,1)

ax.set_xlim(-1,3.5)
ax.set_ylim(-5,30)

ax.set_xticks([])
ax.set_yticks([])

ax.set_frame_on(False)

ax.arrow(-1, 0, 4.5, 0, length_includes_head=True, facecolor='black', head_length=0.1, head_width=0.5)
ax.text(3.25,-3.5,r"$x$")

ax.arrow(0, -2, 0, 31, length_includes_head=True, facecolor='black', head_length=0.5, head_width=0.1)
ax.text(-0.4, 27.5, r"$y$")

def fun(x):
    return 0.8*(x+0.5)**3-1

a = 0.25
b = 2.75
x = np.linspace (a, b)
ax.plot(x, fun(x), lw=1.25)

def rsec(x,x0,x1):
    return (fun(x1)-fun(x0))/(x1-x0)*(x-x1) + fun(x1)

#(x1,f(x1))
x1=2.65
a = x1
ax.plot ([0, a], [fun(a), fun(a)], color='gray', linestyle='dashed')
ax.plot ([a, a], [fun(a), 0], color='gray', linestyle='dashed')
ax.plot (a, fun(a), 'ko', markersize=3)
ax.plot ([a, a], [-0.5, 0.5], color='black')
ax.plot ([-0.05, 0.05], [fun(a), fun(a)], color='black')
ax.text (-1, fun(a)-0.1, r"$f(x^{(1)})$")
ax.text (a - 0.25, -3.5, r"$x^{(1)}$")

#(x2,fx2)
x2=2.15
a = x2
ax.plot ([0, a], [fun(a), fun(a)], color='gray', linestyle='dashed')
ax.plot ([a, a], [fun(a), 0], color='gray', linestyle='dashed')
ax.plot (a, fun(a), 'ko', markersize=3)
ax.plot ([a, a], [-0.5, 0.5], color='black')
ax.plot ([-0.05, 0.05], [fun(a), fun(a)], color='black')
ax.text (-1, fun(a)-0.1, r"$f(x^{(2)})$")
ax.text (a - 0.25, -3.5, r"$x^{(2)}$")

#secant for x1 and x2
xx = np.linspace(x2-0.75,x2+0.7)
ax.plot(xx,rsec(xx,x1,x2),color="gray",lw=0.75)

#(x3,f(x3))
x3 = x2 - fun(x2)*(x2-x1)/(fun(x2)-fun(x1))
a = x3
ax.plot ([0, a], [fun(a), fun(a)], color='gray', linestyle='dashed')
ax.plot ([a, a], [fun(a), 0], color='gray', linestyle='dashed')
ax.plot (a, fun(a), 'ko', markersize=3)
ax.plot ([a, a], [-0.5, 0.5], color='black')
ax.plot ([-0.05, 0.05], [fun(a), fun(a)], color='black')
ax.text (-1, fun(a)-0.1, r"$f(x^{(3)})$")
ax.text (a - 0.2, -3.5, r"$x^{(3)}$")

#secant for x2 and x3
xx = np.linspace(x3-0.5,x3+1)
ax.plot(xx,rsec(xx,x2,x3),color="gray",lw=0.75)

#(x4, f(x4))
x4 = x3 - fun(x3)*(x3-x2)/(fun(x3)-fun(x2))
a = x4
ax.plot ([a, a], [-0.5, 0.5], color='black')
ax.text (a - 0.3, -3.5, r"$x^{(4)}$")

xstar = sci.optimize.fsolve(fun,a)
ax.plot ([xstar, xstar], [0, 0], 'ro', markersize=3)
ax.text (xstar - 0.25, 0.5, r"$x\!^{*}$")

fig_file =  "metodo_das_secantes"
fig.savefig(fig_file+".eps", bbox_inches='tight')
fig.savefig(fig_file+".svg", bbox_inches='tight')
fig.savefig(fig_file+".png", bbox_inches='tight')


