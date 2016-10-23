#!/usr/bin/python3
# coding: utf-8

#Este trabalho está licenciado sob a Licença
#Creative Commons Atribuição-CompartilhaIgual 3.0 Não Adaptada.
#Para ver uma cópia desta licença, visite
#http://creativecommons.org/licenses/by-sa/3.0/
#ou envie uma carta para Creative Commons,
#PO Box 1866, Mountain View, CA 94042, USA.

from math import *
import matplotlib.pyplot as plt
import numpy as np
import scipy as sci
from scipy import optimize

fig = plt.figure(figsize=(8.3,11.7), dpi=300)
ax = plt.subplot(111)

ax.axis("off")
ax.set_xlim((-2,10))
plt.arrow(-2,0,11,0,**{"linewidth":2, "head_width":0.2, "length_includes_head":True, "facecolor":'black'})

ax.set_ylim((-2,14))
plt.arrow(0,-2,0,14,**{"linewidth":1.5, "head_width":0.2, "length_includes_head":True, "facecolor":'black'})

xdata = np.array([2, 3, 4, 5, 6, 7.5])
ydata = np.array([-1, 1.5, 1.1, 2.5, 2.75, 6])
plt.plot(xdata,ydata,'ko')

def fun(x,a,b,c,d):
    return a + b*x + c*x**2 + d*x**3

xx = np.linspace(1.75, 8)
popt, pcov = sci.optimize.curve_fit(fun,xdata,ydata)
print(popt)
plt.plot(xx,fun(xx,*popt))

def dfun(x,a,b,c,d):
    return b + 2*c*x + 3*d*x**2

def tan(x0,x,a,b,c,d):
    return dfun(x0,a,b,c,d)*(x-x0)+fun(x0,a,b,c,d)

x0 = 3.25
xx = np.linspace(1,8)
yy = tan(x0,xx,*popt)
plt.plot(xx,yy,'r-')

#plt.savefig("capa.pdf", papertype='a4', bbox_inches='tight')
plt.savefig("capa.svg", papertype='a4', bbox_inches='tight')

