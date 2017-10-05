from __future__ import division
import numpy as np


def f(t):
	return np.array([t, t**2])

def Adams_Moulton_4(A,h,Tmax,u1):
	dim=A.shape[0]
	B=np.linalg.inv(np.eye(dim)-3/8*h*A);

	itmax=np.int(Tmax/h)
	u=np.empty((dim, itmax+1))
	fn=np.empty((dim,3))
	u[:,0]=u1

	#Iniciliza com RK4
	for i in np.arange(0,3):
		t=i*h
		k1 = f(t)+np.matmul(A,u[:,i])

#		print A
#		print A.dot((u[:,1]+ (k1[0,:]+k1*h/2)).T)


		k2 = f(t+h/2) + A.dot((u[:,i]+k1*h/2).T).T
		k3 = f(t+h/2) + A.dot((u[:,i]+k2*h/2).T).T
		k4 = f(t+h)   + A.dot((u[:,i]+k3*h).T).T

		print k2
		u[:,i+1]=u[:,i]+h*(k1+2*k2+2*k3+k4)/6
		fn[:,i]= h*A.dot(u[:,i+1]) + f(t+h)
		
	for i in np.arange(0,itmax-1):
		t=(i+1)*h
		soma = 1/24*fn[:,0]-5/24*fn[:,1]+19/24*fn[:,2]*3/8*fn[:,0] +3/8*f(t)
		
		u[:,i+2] = B.dot(u[:,i+1] + h*soma)



#4 & $\frac{1}{24}$ & $-{\frac {5}{24}}$ & ${\frac {19}{24}}$ & $\frac{3}{8}$ &&&&\\


	return u

A=np.matrix([[1, 1],[2, 3]])
u1=np.array([0,1])


h=1e-1
Tmax=1
itmax=np.int(Tmax/h)


Adams_Moulton_4(A,h,Tmax,u1)



