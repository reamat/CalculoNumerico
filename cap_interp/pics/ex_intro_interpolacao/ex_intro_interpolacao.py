#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Este trabalho está licenciado sob a Licença Creative Commons Atribuição-CompartilhaIgual 3.0 Não Adaptada. Para ver uma cópia desta licença, visite https://creativecommons.org/licenses/by-sa/3.0/ ou envie uma carta para Creative Commons, PO Box 1866, Mountain View, CA 94042, USA.

Author: Pedro H A Konzen - 10/2016

Descrição:
Simples exemplo de interpolação dos pontos
$\{(1, 1), (2, 2)\}$
por uma reta
$f(x) = a + bx$.
'''

import numpy as np
import scipy as sci
from scipy import optimize
import matplotlib.pyplot as plt

#canvas
fig = plt.figure(figsize=(3,3), dpi=300, linewidth=0.0, facecolor="white")

#axes definitions
ax = plt.subplot(1,1,1)

ax.set_xlim(-0.5,3.5)
ax.set_ylim(-0.5,3.5)

ax.set_xticks([])
ax.set_yticks([])

ax.set_frame_on(False)

ax.arrow(-0.5, 0, 4, 0, length_includes_head=True,
         facecolor='black', head_length=0.1, head_width=0.1)
ax.text(3.25,-0.25,r"$x$")

ax.arrow(0, -0.5, 0, 4, length_includes_head=True,
         facecolor='black', head_length=0.1, head_width=0.1)
ax.text(-0.25, 3.25, r"$y$")

#(x1, y1)
ax.text(0.65,1.2,r"$(1,1)$", fontsize=10)
ax.plot([1, 1], [0, 1], color='gray', ls="dashed")
ax.plot([0, 1], [1, 1], color='gray', ls="dashed")
ax.plot([1, 1], [-0.05, 0.05], 'k-')
ax.text(0.9,-0.25,r"$x_1$")
ax.plot([-0.05, 0.05], [1, 1], 'k-')
ax.text(-0.35,1,r"$y_1$")

#(x2, y2)
ax.text(1.65,2.2,r"$(2,2)$", fontsize=10)
ax.plot([2, 2], [0, 2], color='gray', ls="dashed")
ax.plot([0, 2], [2, 2], color='gray', ls="dashed")
ax.plot([2, 2], [-0.05, 0.05], 'k-')
ax.text(1.9,-0.25,r"$x_2$")
ax.plot([-0.05, 0.05], [2, 2], 'k-')
ax.text(-0.35,2,r"$y_2$")

#reta
a = 0.0
b = 1.0
x = np.linspace (-0.25, 3)
ax.plot(x, a + b*x, 'b-')
ax.text(2.75,2.5,r"$y=x$")

#pontos
ax.plot([1, 2], [1, 2], 'ro', markersize=4)

fig_file =  "ex_intro_interpolacao"
fig.savefig(fig_file+".eps", bbox_inches='tight')
fig.savefig(fig_file+".pdf", bbox_inches='tight')
fig.savefig(fig_file+".png", bbox_inches='tight')
fig.savefig(fig_file+".svg", bbox_inches='tight')


