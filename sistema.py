from __future__ import division
import numpy as np


def f(t,u):
#	return np.array(u[1], 10*u[1]+11*u[0])
#	return np.sqrt(1+u)
	return np.sqrt(1+u)*(np.fabs(2-u))
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


def adams_bash_2(h,Tmax,u1):
	dim=np.size(u1)
	itmax=np.int(Tmax/h)
	u=np.empty((itmax+1,dim))
	u[0,:]=u1

	#inicaliza com RK2
	k1 = f(0,   u[0,:])
	k2 = f(h, u[0,:] + k1* h)
	u[1,:] = u[0,:] + (k1+k2)* h/2

#	print k1,k2

	fn_0=k2
	for i in np.arange(0,itmax-1):
		t=(i+1)*h
		fn_1 = f(t,   u[i+1,:])
		u[i+2,:] = u[i+1,:] + h*(-.5*fn_0 + 1.5*fn_1)
		fn_0=fn_1
	return u


def pred_corr_adams_2(h,Tmax,u1):
	dim=np.size(u1)
	itmax=np.int(Tmax/h)
	u=np.empty((itmax+1,dim))
	u[0,:]=u1

	#inicaliza com RK2
	k1 = f(0,   u[0,:])#
	k2 = f(h, u[0,:] + k1* h)
	u[1,:] = u[0,:] + (k1+k2)* h/2

	fn_0=k2
	for i in np.arange(0,itmax-1):
		t=(i+1)*h
		fn_1 = f(t,   u[i+1,:])

		fn_til=fn_1
		u_til = u[i+1,:] + h*(-.5*fn_0 + 1.5*fn_til)
		fn_til= f(t+h,   u_til)



		u[i+2,:] = u[i+1,:] + h*(0.5*fn_1 + .5*fn_til)
		fn_0=fn_1

	return u


def pred_corr_adams_2_iterado(h,Tmax,u1):
	dim=np.size(u1)
	itmax=np.int(Tmax/h)
	u=np.empty((itmax+1,dim))
	u[0,:]=u1

	#inicaliza com RK2
	k1 = f(0,   u[0,:])
	k2 = f(h, u[0,:] + k1* h)
	u[1,:] = u[0,:] + (k1+k2)* h/2

	fn_0=k2
	for i in np.arange(0,itmax-1):
		t=(i+1)*h
		fn_1 = f(t,   u[i+1,:])

		fn_til=fn_1

		u_til = u[i+1,:] + h*(-0.5*fn_0 + 1.5*fn_til) #prediz


		erro = 1
		while (erro>1e-10*u_til):
			fn_til= f(t+h,   u_til)
			u_til_2 = u[i+1,:] + h*(0.5*fn_1 + 0.5*fn_til)  #corrige
			erro = np.fabs(u_til_2-u_til)
			u_til = u_til_2

		u[i+2,:]=u_til



		fn_0=fn_1

	return u



u0=np.array([0])
h=10e-1
Tmax=1
itmax=np.int(Tmax/h)

#for metodo in [euler, euler_mod, RK3_classico, RK4_classico, adams_bash_2]:
for metodo in [euler_mod, adams_bash_2, pred_corr_adams_2, pred_corr_adams_2_iterado, RK4_classico]:
#for metodo in [adams_bash_2]:
	u=metodo(h,Tmax,u0)
	print(u[itmax,:])

	#for i in np.arange(0,itmax+1):
	#	print u[i,:]



#u=RK2_generico(h,Tmax,u0,.5)
#print(u[itmax,:])

