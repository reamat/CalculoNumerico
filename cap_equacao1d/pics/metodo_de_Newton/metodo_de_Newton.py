#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Este trabalho está licenciado sob a Licença Creative Commons Atribuição-CompartilhaIgual 3.0 Não Adaptada. Para ver uma cópia desta licença, visite https://creativecommons.org/licenses/by-sa/3.0/ ou envie uma carta para Creative Commons, PO Box 1866, Mountain View, CA 94042, USA.

Author: Pedro H A Konzen - 08/2016

Descrição:
Ilustração do método de Newton.

Description:
Illustration of the Newton's method.
'''

import numpy as np
import scipy as sci
from scipy import optimize
import matplotlib.pyplot as plt

#canvas
fig = plt.figure(figsize=(3,3), dpi=300, linewidth=0.0, facecolor="white")

#axes definitions
ax = plt.subplot(1,1,1)

ax.set_xlim(-1,3)
ax.set_ylim(-5,30)

ax.set_xticks([])
ax.set_yticks([])

ax.set_frame_on(False)

ax.arrow(-1, 0, 4, 0, length_includes_head=True, facecolor='black', head_length=0.1, head_width=0.5)
ax.text(2.75,-3.5,r"$x$")

ax.arrow(0, -2, 0, 31, length_includes_head=True, facecolor='black', head_length=0.5, head_width=0.1)
ax.text(-0.25, 26, r"$y$")

def fun(x):
    return (x+0.5)**3-1

def dfun(x):
    return 3*(x+0.5)**2

a = 0.25
b = 2.5
x = np.linspace (a, b)
ax.plot(x, fun(x), lw=1.25)

def rtan(x,x0):
    return dfun(x0)*(x-x0) + fun(x0)

x0=2.15
x = np.linspace(x0-0.9,x0+0.4)
ax.plot(x,rtan(x,x0),color="gray",lw=0.75)

x1 = x0 - fun(x0)/dfun(x0)
x = np.linspace(x1-0.6,x1+0.7)
ax.plot(x,rtan(x,x1),color="gray",lw=0.75)


#dashed lines
#(a, f(a))
a = x0
ax.plot ([0, a], [fun(a), fun(a)], color='gray', linestyle='dashed')
ax.plot ([a, a], [fun(a), 0], color='gray', linestyle='dashed')
ax.plot (a, fun(a), 'ko', markersize=3)
ax.plot ([a, a], [-0.5, 0.5], color='black')
ax.plot ([-0.1, 0.1], [fun(a), fun(a)], color='black')
ax.text (-1, fun(a)-0.1, r"$f(x^{(1)})$")
ax.text (a - 0.25, -3.5, r"$x^{(1)}$")

#dashed lines
#(a, f(a))
a = x1
ax.plot ([0, a], [fun(a), fun(a)], color='gray', linestyle='dashed')
ax.plot ([a, a], [fun(a), 0], color='gray', linestyle='dashed')
ax.plot (a, fun(a), 'ko', markersize=3)
ax.plot ([a, a], [-0.5, 0.5], color='black')
ax.plot ([-0.1, 0.1], [fun(a), fun(a)], color='black')
ax.text (-1, fun(a)-0.1, r"$f(x^{(2)})$")
ax.text (a - 0.25, -3.5, r"$x^{(2)}$")

#dashed lines
#(a, f(a))
a = x1 - fun(x1)/dfun(x1)
ax.plot ([a, a], [-0.5, 0.5], color='black')
ax.text (a - 0.25, -3.5, r"$x^{(3)}$")

xstar = sci.optimize.fsolve(fun,a)
ax.plot ([xstar, xstar], [0, 0], 'ro', markersize=3)
ax.text (xstar - 0.25, 0.5, r"$x\!^{*}$")



'''
#(b, f(b))
ax.plot (b, fun(b), 'ko', markersize=3)
ax.text (-1.75, fun(b)-0.1, r"$f(b)$")
ax.plot ([-0.1, 0.1], [fun(b), fun(b)], color='black')
ax.plot ([0, b], [fun(b), fun(b)], color='gray', linestyle='dashed')
ax.plot ([b, b], [fun(b), 0], color='gray', linestyle='dashed')
ax.plot ([b, b], [-0.1, 0.1], color='black')
ax.text (b - 0.25, 0.25, r"$b$")


#f(p) = 0
p = sci.optimize.fsolve(fun,(a+b)/2)
ax.plot (p, fun(p), 'ko', markersize=3, markerfacecolor='red')
ax.text (p, 0.25, r"$x\!^*$")
'''

#plt.show()

fig_file =  "metodo_de_Newton"
fig.savefig(fig_file+".eps", bbox_inches='tight')
fig.savefig(fig_file+".svg", bbox_inches='tight')
fig.savefig(fig_file+".png", bbox_inches='tight')


