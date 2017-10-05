from __future__ import division
import numpy as np


## resolve u'(t)=l*u(t) + g

def g(t):
	return t*np.exp(-t)




u0=-1
h=1e-2
Tmax=2
itmax=np.int(Tmax/h)

u=np.empty(itmax+1)
fn=np.empty(itmax+1)

u[0]=u0
l=-2
#Iniciliza com Euler modificado
k1= l*u[0] + g(0)
k2= l*(u[0]+h*k1) + g(h)
u[1]= u[0]+ h *(k1+k2)/2

fn[0]= k1
fn[1]= l*u[1] + g(h)



for n in np.arange(0,itmax-1):
	gn2=g((n+2)*h)
	
	u[n+2]= (u[n+1] + h/12*(8*fn[n+1]-fn[n]) + 5*h/12*gn2 ) / (1+5*h/6)
	fn[n+2]=l*u[n+2]+gn2

for n in np.arange(0,itmax+1):
	print h*n,u[n], (h*n-1)*np.exp(-h*n)
