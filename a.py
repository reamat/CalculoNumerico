from __future__ import division
import numpy as np

def f(t,u):
	return np.cos(t*u)


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
	u=u1
  	itmax = Tmax/h;
	for i in np.arange(0,itmax):
		t=i*h
		k1 = f(t,u)
		u_til = u + h*k1
		k2 = f(t+h,u_til)
		u=u+h*(k1+k2)/2
	return u


def euler(h,Tmax,u1):
	u=u1
  	itmax = Tmax/h;
	for i in np.arange(0,itmax):
		t=i*h
		k1 = f(t,u)
		u = u + h*k1
	return u
	

t=2
u1=1
sol_exata = (1 + np.exp(-t))**2/4
n=0
sol=[0,0,0,0,0,0,0,0]
err=[0,0,0,0,0,0,0,0]
for h in [1e-1, 1e-2, 1e-3, 1e-4, 1e-5]:
	sol_euler=euler_mod(h,t,u1);
	erro_relativo = np.fabs((sol_euler-sol_exata)/sol_exata)
	print("h=%1.0e - u(1) =~ %1.17f - erro_relativo = %1.1e" % (h, sol_euler, erro_relativo) )
	sol[n]=sol_euler;
	err[n]=erro_relativo
	n=n+1
		
print("%1.7f & %1.7f & %1.7f & %1.7f & %1.7f" % (sol[0], sol[1], sol[2], sol[3], sol[4]) )
print("%1.1e & %1.1e & %1.1e & %1.1e & %1.1e" % (err[0], err[1], err[2], err[3], err[4]) )

print sol_exata;

#for h in [1e-1, 1e-2, 1e-3, 1e-4, 1e-5]:
#	sol_euler=euler_mod(h,t,u1);
#	erro_relativo = np.fabs((sol_euler-sol_exata)/sol_exata)
#	print("h=%1.0e - u(1) =~ %1.7f - erro_relativo = %1.1e" % (h, sol_euler, erro_relativo) )

