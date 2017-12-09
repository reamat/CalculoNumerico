#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Este trabalho está licenciado sob a Licença Creative Commons Atribuição-CompartilhaIgual 3.0 Não Adaptada. Para ver uma cópia desta licença, visite https://creativecommons.org/licenses/by-sa/3.0/ ou envie uma carta para Creative Commons, PO Box 1866, Mountain View, CA 94042, USA.

Author: Pedro H A Konzen - 08/2016
'''

import numpy as np
import matplotlib.pyplot as plt

#font settings
plt.rc('text', usetex=True)
plt.rc('font', family='serif', size=12)

#canvas
fig = plt.figure(figsize=(2,2), dpi=300, facecolor="white")

#axes definitions
ax = plt.subplot(1,1,1)

ax.set_xlim(-1,4)
ax.set_ylim(-1.5,3)

ax.set_xticks([])
ax.set_yticks([])

ax.set_frame_on(False)

ax.arrow(-1, 0, 5, 0, head_width=0.1,head_length=0.1, length_includes_head=True, facecolor='black')
ax.text(3.75,-0.5,r"$x$")

ax.arrow(0, -1.5, 0, 4.5, head_width=0.1, head_length=0.1, length_includes_head=True, facecolor='black')
ax.text(-0.5, 2.75, r"$y$")

a = 0.5
b = 3
def f(x):
    return -4 + 8*x - 5*x**2 + x**3


#dashed lines
#(a, f(a))
ax.plot (a, f(a), 'ko', markersize=3)
ax.plot ([a, a], [f(a), 0], color='gray', linestyle='dashed')
ax.plot ([a, a], [-0.1, 0.1], color='black')
ax.text (a - 0.3, 0.25, r"$\frac{1}{2}$")

#(b, f(b))
ax.plot (b, f(b), 'ko', markersize=3)
ax.plot ([b, b], [f(b), 0], color='gray', linestyle='dashed')
ax.plot ([b, b], [-0.1, 0.1], color='black')
ax.text (b - 0.3, -0.5, r"$3$")

x = np.linspace (a, b, 100, endpoint=True)
ax.plot(x, f(x))


#plt.show()
fig_file =  "ex_metodo_da_bissecao"
fig.savefig(fig_file+".eps", bbox_inches='tight')
fig.savefig(fig_file+".pdf", bbox_inches='tight')
fig.savefig(fig_file+".png", bbox_inches='tight')
fig.savefig(fig_file+".svg", bbox_inches='tight')


