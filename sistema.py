from __future__ import division
import numpy as np


def f(t,u):
	return -50*(u-np.cos(t))
#	return u**2-u**3
#	return np.array([u[1], -100*u[0]-101*u[1]])
#	return np.sqrt(1+u)
#	return np.sqrt(1+u)*(np.fabs(2-u))
#	return np.array([-u[1],u[0]+t])
#	return u**3+t-u

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

	fn_0=k1
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

	fn_0=k1
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

	fn_0=k1
	for i in np.arange(0,itmax-1):
		t=(i+1)*h
		fn_1 = f(t,   u[i+1,:])

		fn_til=fn_1

		u_til = u[i+1,:] + h*(-0.5*fn_0 + 1.5*fn_til) #prediz


		erro = 1
		while (erro>1e-10*np.linalg.norm(u_til)):
			fn_til= f(t+h,   u_til)
			u_til_2 = u[i+1,:] + h*(0.5*fn_1 + 0.5*fn_til)  #corrige
			erro = np.linalg.norm(u_til_2-u_til)
			u_til = u_til_2

		u[i+2,:]=u_til



		fn_0=fn_1


	return u



def adams_bash_4(h,Tmax,u1):
	dim=np.size(u1)
	itmax=np.int(Tmax/h)
	u=np.empty((itmax+1,dim))
	u[0,:]=u1
	fn=np.empty((4,dim))

	#inicaliza com RK4
	for i in np.arange(0,3):
		t=i*h
		k1 = f(t,     u[i,:]         )
		k2 = f(t+h/2, u[i,:] + h*k1/2)
		k3 = f(t+h/2, u[i,:] + h*k2/2)
		k4 = f(t+h,   u[i,:] + h*k3  )

		u[i+1,:]=u[i,:]+h*(k1+2*k2+2*k3+k4)/6
		fn[i]=k1



	for i in np.arange(0,itmax-3):
		fn[3] = f( (i+3)*h,  u[i+3,:])
		u[i+4,:] = u[i+3,:] + h*(-9*fn[0] + 37*fn[1]- 59*fn[2]+ 55*fn[3])/24

		fn[0]=fn[1]
		fn[1]=fn[2]
		fn[2]=fn[3]
		

	return u


def pred_corr_adams_4(h,Tmax,u1):
	dim=np.size(u1)
	itmax=np.int(Tmax/h)
	u=np.empty((itmax+1,dim))
	u[0,:]=u1
	fn=np.empty((5,dim))

	#inicaliza com RK4
	for i in np.arange(0,3):
		t=i*h
		k1 = f(t,     u[i,:]         )
		k2 = f(t+h/2, u[i,:] + h*k1/2)
		k3 = f(t+h/2, u[i,:] + h*k2/2)
		k4 = f(t+h,   u[i,:] + h*k3  )

		u[i+1,:]=u[i,:]+h*(k1+2*k2+2*k3+k4)/6
		fn[i]=k1



	for i in np.arange(0,itmax-3):
		fn[3] = f( (i+3)*h,  u[i+3,:])
		u[i+4,:] = u[i+3,:] + h*(-9*fn[0] + 37*fn[1]- 59*fn[2]+ 55*fn[3])/24

		for k in [0,1,2,3]:	
			fn[4] = f( (i+4)*h,  u[i+4,:])
			u[i+4,:] = u[i+3,:] + h*(fn[1] - 5*fn[2] + 19*fn[3]+ 9*fn[4])/24

	
		fn[0]=fn[1]
		fn[1]=fn[2]
		fn[2]=fn[3]
		

	return u



#u0=np.array([101,-10001])
u0=0.01
h=1e-2
Tmax=1000
itmax=np.int(Tmax/h)

#for metodo in [euler, euler_mod, RK3_classico, RK4_classico, adams_bash_2]:
#for metodo in [euler_mod, adams_bash_2, pred_corr_adams_2, pred_corr_adams_2_iterado, RK4_classico]:


for metodo in [pred_corr_adams_4, adams_bash_4,  RK4_classico,adams_bash_2, pred_corr_adams_2]:
	u=metodo(h,Tmax,u0)
	print u[itmax,:]
#	print u
print 100*np.exp(-100*Tmax)+np.exp(-Tmax)

	#for i in np.arange(0,itmax+1):
#print u



#u=RK2_generico(h,Tmax,u0,.5)
#print(u[itmax,:])

