from __future__ import division
import numpy as np

def f(t,u):
#	return np.asarray([u[1], (1-u[2]/10)*u[1]-u[0], (u[0]**2-u[2])/10 ])
	#return np.asarray([-2*u[0]+np.sqrt(u[1]), -u[1]+u[0] ])
	#return np.asarray([u[1], -u[1]-np.sin(u[0]) ])
	return -u**2+t

def euler_RK4(h,Tmax,u1):
	u=u1
  	itmax = Tmax/h;
	for i in np.arange(0,itmax):
		t=i*h
		k1 = f(t,u)
		k2 = f(t+h/2,u+h*k1/2)
		k3 = f(t+h/2,u+h*k2/2)
		k4 = f(t+h,u+h*k3)


		u=u+h*(k1+2*k2+2*k3+k4)/6
	return u


def euler_mod(h,Tmax,u1):
	
	n=0
  	itmax = Tmax/h;
	for i in [0:1:itmax]:
		t=i*h
		k1 = f(t,u[i])
		u_til = u[i] + h*k1
		k2 = f(t+h,u_til)
		u=[u, u[i]+h*(k1+k2)/2]
	return u


def euler(h,Tmax,u1):
	u=u1
  	itmax = Tmax/h;
	for i in np.arange(0,itmax):
		t=i*h
		k1 = f(t,u)
		u = u + h*k1
	return u
	



Tmax=2 			#tempo maximo de simulacao
u1=np.asarray([0])	#condicoes iniciais na forma vetorial
h=1e-4			#passo
#sol_euler=euler_mod(h,Tmax,u1);

itmax=Tmax/h

#for t in [0, .5, 1, 1.5, 2]:
#	k=t/h
#	print("h=%1.0e - x(%1.1f) =~ %1.6f - y(%1.1f) =~ %1.6f" % (h, t, sol_euler[0][k], t, sol_euler[1][k]) )





t=2
u1=0#[2,0]
for h in [e-1, e-2, e-3, e-4]:
	sol_euler=euler_mod(h,t,u1);
#	print("h=%1.0e - u(1) =~ %1.7f - u(2) =~ %1.7f - u(3) =~ %1.17f" % (h, sol_euler[0], sol_euler[1], sol_euler[2]) )
		
	#print("h=%1.0e - u(1) =~ %1.7f - u(2) =~ %1.7f" % (h, sol_euler[0], sol_euler[1]) )

	print("%1.7f" % (sol_euler[0]) )


