#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Este trabalho está licenciado sob a Licença Creative Commons Atribuição-CompartilhaIgual 3.0 Não Adaptada. Para ver uma cópia desta licença, visite https://creativecommons.org/licenses/by-sa/3.0/ ou envie uma carta para Creative Commons, PO Box 1866, Mountain View, CA 94042, USA.

Author: Pedro H A Konzen - 03/2015
Last update: 08/2016 by phkonzen
'''

import numpy as np
import matplotlib.pyplot as plt

#font settings
plt.rc('text', usetex=True)
plt.rc('font', family='serif', size=12)

#canvas
fig = plt.figure(figsize=(3,3), dpi=300, linewidth=0.0, facecolor="white")

#axes definitions
ax = plt.subplot(1,1,1)

ax.set_xlim(-2,10)
ax.set_ylim(-5,5)

ax.set_xticks([])
ax.set_yticks([])

ax.set_frame_on(False)

ax.arrow(-2, 0, 12, 0, head_width=0.25,head_length=0.25, length_includes_head=True, facecolor='black')
ax.text(9.5,-0.75,r"$x$")

ax.arrow(0, -5, 0, 10, head_width=0.25, head_length=0.25, length_includes_head=True, facecolor='black')
ax.text(-0.75, 4.5, r"$y$")

def f(x):
    return -4 * np.cos ((x-1)/(np.pi))

a = 2
b = 8
x = np.linspace (a, b, 100, endpoint=True)

ax.plot(x, f(x))

#dashed lines
#(a, f(a))
ax.plot (a, f(a), 'ko', markersize=3)
ax.text (-2, f(a), r"$f(a)$")
ax.plot ([-0.1, 0.1], [f(a), f(a)], color='black')
ax.plot ([0, a], [f(a), f(a)], color='gray', linestyle='dashed')
ax.plot ([a, a], [f(a), 0], color='gray', linestyle='dashed')
ax.plot ([a, a], [-0.1, 0.1], color='black')
ax.text (a - 0.25, 0.35, r"$a$")

#(b, f(b))
ax.plot (b, f(b), 'ko', markersize=3)
ax.text (-2, f(b), r"$f(b)$")
ax.plot ([0, b], [f(b), f(b)], color='gray', linestyle='dashed')
ax.plot ([b, b], [f(b), 0], color='gray', linestyle='dashed')
ax.plot ([-0.1, 0.1], [f(b), f(b)], color='black')
ax.plot ([b, b], [-0.1, 0.1], color='black')
ax.text (b - 0.25, -0.75, r"$b$")


#(p, f(p))
p = (a + b)/2
ax.plot (p, f(p), 'ko', markersize=3)
ax.text (-2.75, f(p), r"$f(x^{(0)})$")
ax.plot ([0, p], [f(p), f(p)], color='gray', linestyle='dashed')
ax.plot ([p, p], [f(p), 0], color='gray', linestyle='dashed')
ax.plot ([-0.1, 0.1], [f(p), f(p)], color='black')
ax.plot ([p, p], [-0.1, 0.1], color='black')
ax.text (p - 0.25, 0.35, r"$x^{(0)}$")

#(p1, f(p1))
p1 = (p + b)/2
ax.plot ([p1, p1], [-0.1, 0.1], color='black')
ax.text (p1 - 0.25, -0.75, r"$x^{(1)}$")

#chosen interval
plt.plot([p,b],[0,0],'r-',lw=1)

#plt.show()

fig_file =  "metodo_da_bissecao"
fig.savefig(fig_file+".eps", bbox_inches='tight')
fig.savefig(fig_file+".pdf", bbox_inches='tight')
fig.savefig(fig_file+".png", bbox_inches='tight')
fig.savefig(fig_file+".svg", bbox_inches='tight')


