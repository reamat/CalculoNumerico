#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Este trabalho está licenciado sob a Licença Creative Commons Atribuição-CompartilhaIgual 3.0 Não Adaptada. Para ver uma cópia desta licença, visite https://creativecommons.org/licenses/by-sa/3.0/ ou envie uma carta para Creative Commons, PO Box 1866, Mountain View, CA 94042, USA.

Author: Pedro H A Konzen - 11/2016

Descrição:
Malha uniforme em um intervalho $[a, b]$.
'''

import numpy as np
import matplotlib.pyplot as plt

#font letter
plt.rc('text', usetex=True)
plt.rc('font', family='serif', size=12)

#canvas
fig = plt.figure(figsize=(3,1), dpi=300, linewidth=0.0, facecolor="white")
ax = plt.subplot(1,1,1)

#no axes
ax.axis("off")
ax.set_yticks([])
ax.set_xticks([])

ax.set_xlim(-0.1,1.1)
ax.set_ylim(-1,1.5)
plt.plot([-0.1,1.1],[0,0],'k-')

#[a, b]
plt.plot([0,0],[-0.1,0.1], 'k-')
ax.text(-0.025,-0.5,r"$a$")

plt.plot([1,1],[-0.1,0.1], 'k-')
ax.text(0.975,-0.5,r"$b$")

#pontos
ax.text(-0.025,0.25,r"$x_1$")
ax.text(0.975,0.25,r"$x_N$")

plt.plot([0.15,0.15],[-0.1,0.1], 'k-')
ax.text(0.125,0.25,r"$x_2$")

ax.text(0.25,0.25,r"$\cdots$")

plt.plot([0.45,0.45],[-0.1,0.1], 'k-')
ax.text(0.425,0.25,r"$x_i$")

ax.text(0.55,0.25,r"$\cdots$")

plt.plot([0.85,0.85],[-0.1,0.1], 'k-')
ax.text(0.75,0.25,r"$x_{N-1}$")

#h
plt.plot([0,0.15],[1,1],'k-')
plt.plot([0,0],[0.9,1.1],'k-')
plt.plot([0.15,0.15],[0.9,1.1],'k-')
plt.text(0.05,1.25,r"$h$")



fig_file =  "malha_uniforme"
fig.savefig(fig_file+".eps", bbox_inches='tight')
fig.savefig(fig_file+".svg", bbox_inches='tight')
fig.savefig(fig_file+".png", bbox_inches='tight')


