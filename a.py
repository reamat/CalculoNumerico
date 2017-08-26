from __future__ import division
import numpy as np

def euler_mod(h,Tmax):
	u=8
  	itmax = Tmax/h;
	t=0
	for i in np.arange(0,itmax):
		t=i*h
		k1 = -0.5*u+2+t
		u_til = u + h*k1
		k2 = -0.5*u_til+2+(t+h)
		u=u+h*(k1+k2)/2
	return u


def euler(h,Tmax):
	u=1
  	itmax = Tmax/h;
	t=0
	for i in np.arange(0,itmax):
	
		k1 = -u+t
		u = u + h*k1
		t=t+h	
	return u
	


h=1e-1
for t in [1, 2, 3, 4]:
	sol_euler=euler(h,t);
	sol_exata = 2*np.exp(-t)+t-1
	erro_relativo = np.fabs((sol_euler-sol_exata)/sol_exata)
	print("h=%1.0e - u(%1.1f) =~ %1.7f - erro_relativo = %1.1e - exata=%1.7f" % (h, t, sol_euler, erro_relativo, sol_exata) )

h=1e-2
print;
for t in [1, 2, 3, 4]:
	sol_euler=euler(h,t);
	sol_exata = 2*np.exp(-t)+t-1
	erro_relativo = np.fabs((sol_euler-sol_exata)/sol_exata)
	print("h=%1.0e - u(%1.1f) =~ %1.7f - erro_relativo = %1.1e" % (h, t, sol_euler, erro_relativo) )



sol_exata = 2+8*np.exp(-1/2)
for h in [1e-1, 1e-2, 1e-3, 1e-4, 1e-5]:
	sol_euler=euler(h,1);
	erro_relativo = np.fabs((sol_euler-sol_exata)/sol_exata)
	print("h=%1.0e - u(1) =~ %1.7f - erro_relativo = %1.1e" % (h, sol_euler, erro_relativo) )
	
print;
