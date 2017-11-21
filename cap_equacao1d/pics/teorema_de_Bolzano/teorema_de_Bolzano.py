#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Este trabalho está licenciado sob a Licença Creative Commons Atribuição-CompartilhaIgual 3.0 Não Adaptada. Para ver uma cópia desta licença, visite https://creativecommons.org/licenses/by-sa/3.0/ ou envie uma carta para Creative Commons, PO Box 1866, Mountain View, CA 94042, USA.

Author: Pedro H A Konzen - 08/2016

Descrição:
Ilustração do teorema de Bolzano.

Description:
Illustration of the Bolzano's theorem.
'''

import numpy as np
import scipy as sci
from scipy import optimize
import matplotlib.pyplot as plt

#canvas
fig = plt.figure(figsize=(3,3), dpi=300, linewidth=0.0, facecolor="white")

#axes definitions
ax = plt.subplot(1,1,1)

ax.set_xlim(-2,10)
ax.set_ylim(-5,5)

ax.set_xticks([])
ax.set_yticks([])

ax.set_frame_on(False)

ax.arrow(-2, 0, 12, 0, length_includes_head=True, facecolor='black', head_width=0.2)
ax.text(9.5,-0.75,r"$x$")

ax.arrow(0, -5, 0, 10, length_includes_head=True, facecolor='black', head_width=0.2)
ax.text(-0.75, 4.5, r"$y$")

def fun(x):
    return 3*np.sin(x/1.8)

a = 2
b = 8
x = np.linspace (a, b, 100, endpoint=True)
ax.plot(x, fun(x))

#dashed lines
#(a, f(a))
ax.plot (a, fun(a), 'ko', markersize=3)
ax.text (-1.75, fun(a)-0.1, r"$f(a)$")
ax.plot ([-0.1, 0.1], [fun(a), fun(a)], color='black')
ax.plot ([0, a], [fun(a), fun(a)], color='gray', linestyle='dashed')
ax.plot ([a, a], [fun(a), 0], color='gray', linestyle='dashed')
ax.plot ([a, a], [-0.1, 0.1], color='black')
ax.text (a - 0.25, -0.75, r"$a$")

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


#plt.show()

fig_file =  "teorema_de_Bolzano"
fig.savefig(fig_file+".eps", bbox_inches='tight')
fig.savefig(fig_file+".svg", bbox_inches='tight')
fig.savefig(fig_file+".png", bbox_inches='tight')


