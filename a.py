from __future__ import division
import numpy as np

def euler(h,Tmax):
	u=1
	t=0
  	itmax = Tmax/h;
	for i in np.arange(itmax):
		u = u + h*np.cos(t)*u
		t=t+h
	return u

	
h=1e-4
for t in [1, 2, 3, 4]:
	sol_euler=euler(h,t);
	sol_exata=np.exp( np.sin(t))
	erro_relativo = np.fabs((sol_euler-sol_exata)/sol_exata)
	print("h=%1.0e - u(%1.1f) =~ %1.7f - erro_relativo = %1.1e - exata=%1.7f" % (h, t, sol_euler, erro_relativo, sol_exata) )

h=1e-2
print;
for t in [1, 2, 3, 4]:
	sol_euler=euler(h,t);
	sol_exata=np.exp( np.sin(t))
	erro_relativo = np.fabs((sol_euler-sol_exata)/sol_exata)
	print("h=%1.0e - u(%1.1f) =~ %1.7f - erro_relativo = %1.1e" % (h, t, sol_euler, erro_relativo) )

