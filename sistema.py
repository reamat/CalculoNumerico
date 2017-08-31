from __future__ import division
import numpy as np


def f(t,u):
	return u*(1-u)
#	return np.array([-u[1],u[0]+t])


def euler(h,Tmax,u1):
	dim=np.size(u1)
	itmax=np.int(Tmax/h)
	u=np.empty((itmax+1,dim))

	u[0,:]=u1

	for i in np.arange(0,itmax):
		t=i*h
		k1 = f(t,u[i,:])
		u[i+1,:] = u[i,:] + k1* h
	return u



def euler_mod(h,Tmax,u1):
	dim=np.size(u1)
	itmax=np.int(Tmax/h)
	u=np.empty((itmax+1,dim))
	u[0,:]=u1

	for i in np.arange(0,itmax):
		t=i*h
		k1 = f(t,   u[i,:])
		k2 = f(t+h, u[i,:] + k1* h)
		u[i+1,:] = u[i,:] + (k1+k2)* h/2
	return u


def RK2_generico(h,Tmax,u1,alpha):
	dim=np.size(u1)
	itmax=np.int(Tmax/h)
	u=np.empty((itmax+1,dim))

	b2=1/(2*alpha)
	b1=1-b2

	u[0,:]=u1
	for i in np.arange(0,itmax):
		t=i*h

		k1 = f(t,         u[i,:]             )
		k2 = f(t+h*alpha, u[i,:] + h*k1*alpha)

		u[i+1] = u[i] + h*(k1*b1+k2*b2)
	return u


def RK3_classico(h,Tmax,u1):
	dim=np.size(u1)
	itmax=np.int(Tmax/h)
	u=np.empty((itmax+1,dim))

	u[0,:]=u1
	
	for i in np.arange(0,itmax):
		t=i*h

		k1 = f(t,     u[i,:]              )
		k2 = f(t+h/2, u[i,:] + h*k1/2     )
		k3 = f(t+h,   u[i,:] + h*(2*k2-k1))

		u[i+1,:] = u[i,:] + h*(k1+4*k2+k3)/6
	return u


def RK4_classico(h,Tmax,u1):
	dim=np.size(u1)
	itmax=np.int(Tmax/h)
	u=np.empty((itmax+1,dim))

	u[0,:]=u1

	for i in np.arange(0,itmax):
		t=i*h
		k1 = f(t,     u[i,:]         )
		k2 = f(t+h/2, u[i,:] + h*k1/2)
		k3 = f(t+h/2, u[i,:] + h*k2/2)
		k4 = f(t+h,   u[i,:] + h*k3  )


		u[i+1,:]=u[i,:]+h*(k1+2*k2+2*k3+k4)/6
	return u




u0=np.array([1/2])
h=1e-3
Tmax=1
itmax=np.int(Tmax/h)

for metodo in [euler, euler_mod, RK3_classico, RK4_classico]:
	u=metodo(h,Tmax,u0)
	print(u[itmax,:])

u=RK2_generico(h,Tmax,u0,.5)
print(u[itmax,:])

