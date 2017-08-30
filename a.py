from __future__ import division
from __future__ import print_function

import numpy as np

def euler(h,Tmax,u1):
	itmax=np.int(Tmax/h)
	u=np.empty(itmax+1)
	u[0]=u1

	for i in np.arange(0,itmax):
		t=i*h
		k1 = f(t,u[i])
		u[i+1] = u[i] + h*k1
	return u




def euler_mod(h,Tmax,u1):
  	itmax = np.int(Tmax/h)
	u=np.empty(itmax+1)
	u[0]=u1

	for i in np.arange(0,itmax):
		t=i*h
		k1 = f(t, u[i])
		k2 = f(t+h, u[i]+h*k1)
		
		u[i+1]=u[i]+h*(k1+k2)/2

	return u




def RK2_generico(h,Tmax,u1,alpha):
  	itmax = Tmax/h;
	u=np.empty(itmax+1)
	u[0]=u1
	b2=1/(2*alpha)
	b1=1-b2
	print(b1)
	for i in np.arange(0,itmax):
		t=i*h

		k1 = f(t,     u[i])
		k2 = f(t+h*alpha, u[i] + h*k1*alpha)

		u[i+1] = u[i] + h*(k1*b1+k2*b2)
	return u



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



def RK4_classico(h,Tmax,u1):
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









def f(t,u):
	return -0.5*u +2 +t
	#return u+t
	#return 2e-1* u**2
	#return np.sqrt(u)

def f_e(t,u1):
	return 2*t +8*np.exp(-.5*t)
	#return u1/(1-2e-1*u1*t)
	#return (t+2)**2/4
Tmax=1.0			#tempo maximo de simulacao
u1=8			#condicoes iniciais na forma vetorial

#sol_exata = 2+8*np.exp(-.5)
sol_exata = f_e(Tmax,u1)#2*np.exp(Tmax)-Tmax-1
tab=np.empty([4,4])
err=np.empty([4,4])
m=0
p=0
nomes=['Euler', 'Euler mod.', 'RK$_3$', 'RK$_4$']
for metodo in [euler, euler_mod, RK3_classico, RK4_classico]:
	for h in [1, 1e-1, 1e-2, 1e-3]:
		itmax=np.int(Tmax/h)
		sol=metodo(h,Tmax,u1)
		erro_relativo = np.fabs((sol[itmax]-sol_exata)/sol_exata)
		tab[m,p]=sol[itmax]
		err[m,p]=erro_relativo
		#print(" & %1.7f" % ( sol[itmax]),end='' )
		#print("%1.2e & " % ( erro_relativo),end='' )
		p=p+1
	m=m+1
	p=0
	#print('')

for m in [0,1,2,3]:
	print(nomes[m],end='')
	for p in [0,1,2,3]:
		print(" & %1.7f" % ( tab[m,p]),end='' )
		#print("%1.2e & " % ( erro_relativo),end='' )
	print('\\\\')
	print('\hline')

	print('$\\varepsilon_{rel}$',end='')
	for p in [0,1,2,3]:
		print(" & %1.1e" % ( err[m,p]),end='' )
		#print("%1.2e & " % ( erro_relativo),end='' )
	print('\\\\')
	print('\hline')



#print("h=%1.0e - u(1) =~ %1.7f - erro_relativo = %1.1e" % (h, sol[itmax], erro_relativo) )
	
