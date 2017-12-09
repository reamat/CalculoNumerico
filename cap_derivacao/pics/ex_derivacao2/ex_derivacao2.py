#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Este trabalho está licenciado sob a Licença Creative Commons Atribuição-CompartilhaIgual 3.0 Não Adaptada. Para ver uma cópia desta licença, visite https://creativecommons.org/licenses/by-sa/3.0/ ou envie uma carta para Creative Commons, PO Box 1866, Mountain View, CA 94042, USA.

Author: Pedro H A Konzen - 11/2016

Descrição:
\ref{ex:derivacao2}
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

ax.set_xlim(1e-1,1e-10)


#pontos
hh = [1e-1, 1e-2, 1e-3, 1e-4, 1e-5, 1e-6, 1e-7, 1e-8, 1e-9, 1e-10]

def erro_dp(h):
    Df = (np.exp(0.5*(2+h))-np.exp(0.5*2))/h
    return np.abs(Df - 0.5*np.exp(0.5*2))

def erro_dr(h):
    Df = (np.exp(0.5*(2))-np.exp(0.5*(2-h)))/h
    return np.abs(Df - 0.5*np.exp(0.5*2))

def erro_dc(h):
    Df = (np.exp(0.5*(2+h))-np.exp(0.5*(2-h)))/(2*h)
    return np.abs(Df - 0.5*np.exp(0.5*2))

ee_dp = []
ee_dr = []
ee_dc = []
for i,h in enumerate(hh):
    ee_dp.append(erro_dp(h))
    ee_dr.append(erro_dr(h))
    ee_dc.append(erro_dc(h))
    
ax.plot(hh, ee_dp, 'bo-', markersize=5, markeredgecolor="black", label="$D_{+,h}$")
ax.plot(hh, ee_dr, 'r^--', markersize=5, markeredgecolor="black", label="$D_{-,h}$")
ax.plot(hh, ee_dc, 'kv:', markersize=5, markeredgecolor="black", label="$D_{0,h}$")

ax.legend(numpoints=1, fontsize=10)

ax.set_xscale('log',basex=10)
ax.set_yscale('log',basex=10)

ax.set_xticks([1e-1,1e-3,1e-5,1e-7,1e-9])
ax.set_yticks([1e-1,1e-3,1e-5,1e-7,1e-9,1e-11])

ax.set_xlabel(r"$h$")
ax.set_ylabel(r"Erro absoluto")

fig_file =  "ex_derivacao2"
fig.savefig(fig_file+".eps", bbox_inches='tight')
fig.savefig(fig_file+".svg", bbox_inches='tight')
fig.savefig(fig_file+".png", bbox_inches='tight')


