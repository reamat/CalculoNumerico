from __future__ import division
import numpy as np


def f(t,u):
	return np.sqrt(1+u)




u0=0
h=1e-1
Tmax=1
itmax=np.int(Tmax/h)

u=np.empty(itmax+1)
u[0]=u0

for i in np.arange(0,itmax):
	x=np.sqrt(1+u[i])
	
	u[i+1]= u[i]+h/8*np.sqrt(h**2 + 16 + 16*u[i] + 8*h*x)+ h/2*x + h**2/8	
	print u[i+1]
