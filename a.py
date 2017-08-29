from __future__ import division
from __future__ import print_function

import numpy as np



def RK4(h,Tmax,u1):
  	itmax = Tmax/h;
	u=np.empty(itmax+1)
	u[0]=u1

	for i in np.arange(0,itmax):
		t=i*h
		k1 = f(t,u[i])
		k2 = f(t+h/2,u[i]+h*k1/2)
		k3 = f(t+h/2,u[i]+h*k2/2)
		k4 = f(t+h,u[i]+h*k3)


		u[i+1]=u[i]+h*(k1+2*k2+2*k3+k4)/6
	return u




def euler_mod(h,Tmax,u1):
  	itmax = Tmax/h;
	x=np.empty(itmax+1)
	y=np.empty(itmax+1)
	x[0]=u1[0]
	y[0]=u1[1]

	for i in np.arange(0,itmax):
		t=i*h
		kx1 = (y[i])
		ky1 = -(np.sin(x[i])+y[i])

		x_til = x[i] + h*kx1
		y_til = y[i] + h*ky1

		kx2 = (y_til)
		ky2 = -(np.sin(x_til)+y_til)

		x[i+1]=x[i]+h*(kx1+kx2)/2
		y[i+1]=y[i]+h*(ky1+ky2)/2

	return [x,y]


def euler(h,Tmax,u1):
	u=u1
  	itmax = Tmax/h;
	for i in np.arange(0,itmax):
		t=i*h
		k1 = f(t,u)
		u = u + h*k1
	return u



def f(t,u):
	return -0.5*u +2 +t


def RK3_classico(h,Tmax,u1):
  	itmax = Tmax/h;
	u=np.empty(itmax+1)
	u[0]=u1
	
	for i in np.arange(0,itmax):
		t=i*h

		k1 = f(t,     u[i])
		k2 = f(t+h/2, u[i] + h*k1/2)
		k3 = f(t+h,   u[i] + h*(2*k2-k1))

		u[i+1] = u[i] + h*(k1+4*k2+k3)/6
	return u


def RK2_generico(h,Tmax,u1):
	alpha=2/3
  	itmax = Tmax/h;
	u=np.empty(itmax+1)
	u[0]=u1
	b2=1/(2*alpha)
	b1=1-b2
	for i in np.arange(0,itmax):
		t=i*h

		k1 = f(t,     u[i])
		k2 = f(t+h*alpha, u[i] + h*k1*alpha)

		u[i+1] = u[i] + h*(k1*b1+k2*b2)
	return u


	
Tmax=1			#tempo maximo de simulacao
u1=8			#condicoes iniciais na forma vetorial
h=1e-3			#passo


sol_exata = 2+8*np.exp(-.5)

for h in [1e-1, 1e-2, 1e-3, 1e-4]:
	itmax=Tmax/h
	#sol=RK3_classico(h,Tmax,u1);
	sol=RK4(h,Tmax,u1);		
	erro_relativo = np.fabs((sol[itmax]-sol_exata)/sol_exata)
	print("h=%1.0e - u(1) =~ %1.7f - erro_relativo = %1.1e" % (h, sol[itmax], erro_relativo) )
	h=h/10


