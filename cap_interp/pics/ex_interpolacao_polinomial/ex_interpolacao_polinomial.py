#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Este trabalho está licenciado sob a Licença Creative Commons Atribuição-CompartilhaIgual 3.0 Não Adaptada. Para ver uma cópia desta licença, visite https://creativecommons.org/licenses/by-sa/3.0/ ou envie uma carta para Creative Commons, PO Box 1866, Mountain View, CA 94042, USA.

Author: Pedro H A Konzen - 10/2016

Descrição:
Interpolacao polinomial do conjunto de pontos
$\{(0, 1), (1, 2), (2, -3), (3, -20)\}$
'''
from __future__ import division
import numpy as np
import scipy as sci
from scipy import optimize
import matplotlib.pyplot as plt

#canvas
fig = plt.figure(figsize=(3,3), dpi=300, linewidth=0.0, facecolor="white")

#axes definitions
ax = plt.subplot(1,1,1)

ax.set_xlim(-1,4)
ax.set_ylim(-9,9)

ax.set_xticks([])
ax.set_yticks([])

ax.set_frame_on(False)

ax.arrow(-1, 0, 4.75, 0, length_includes_head=True,
         facecolor='black', head_length=0.1, head_width=0.2)
ax.text(3.4,-0.75,r"$x$")

ax.arrow(0, -9, 0, 17, length_includes_head=True,
         facecolor='black', head_length=0.3, head_width=0.05)
ax.text(-0.35, 7.25, r"$y$")

#(0, 1)
x = 0
y = 1
ax.text(-0.35,-1.25,r"$0$")
ax.plot([-0.05, 0.05], [y, y], 'k-')
ax.text(-0.35,y,r"$1$")

#(1, 6)
x = 1
y = 6
ax.plot([x, x], [0, y], color='gray', ls="dashed")
ax.plot([0, x], [y, y], color='gray', ls="dashed")
ax.plot([x, x], [-0.1, 0.1], 'k-')
ax.text(x-0.2,-1.25,r"$1$")
ax.plot([-0.05, 0.05], [y, y], 'k-')
ax.text(-0.35,y,r"$6$")

#(2, 5)
x = 2
y = 5
ax.plot([x, x], [0, y], color='gray', ls="dashed")
ax.plot([0, x], [y, y], color='gray', ls="dashed")
ax.plot([x, x], [-0.1, 0.1], 'k-')
ax.text(x-0.2,-1.25,r"$2$")
ax.plot([-0.05, 0.05], [y, y], 'k-')
ax.text(-0.35,y,r"$5$")

#(3, -8)
x = 3
y = -8
ax.plot([x, x], [0, y], color='gray', ls="dashed")
ax.plot([0, x], [y, y], color='gray', ls="dashed")
ax.plot([x, x], [-0.1, 0.1], 'k-')
ax.text(x-0.2,-1.25,r"$3$")
ax.plot([-0.05, 0.05], [y, y], 'k-')
ax.text(-0.65,y,r"$-8$")

#polinomio
def p(x):
    return 1 + 6*x - x**3
    
xx = np.linspace (-0.5, 3.25)
ax.plot(xx, p(xx), 'b-')
ax.text(0.5,8.75,r"$y = 1 + 6x - x^3$")

#pontos
ax.plot([0, 1, 2, 3], [1, 6, 5, -8], 'ro', markersize=4)

fig_file =  "ex_interpolacao_polinomial"
fig.savefig(fig_file+".eps", bbox_inches='tight')
fig.savefig(fig_file+".pdf", bbox_inches='tight')
fig.savefig(fig_file+".png", bbox_inches='tight')
fig.savefig(fig_file+".svg", bbox_inches='tight')


