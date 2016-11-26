import numpy as np

def TDMA(a,b,c,d):
    #preliminares
    a = a.astype('double')
    b = b.astype('double')
    c = c.astype('double')
    d = d.astype('double')

    #recupera ordem do sistema
    n=np.shape(a)[0]
   
    #inicializa vetores auxiliares
    cl=np.zeros(n)
    dl=np.zeros(n)
    x=np.zeros(n)
    
    #calcula cl e dl
    cl[0]=c[0]/b[0]
    for i in np.arange(1,n-1,1):
       cl[i]=c[i]/(b[i]-a[i]*cl[i-1])

    dl[0]=d[0]/b[0]
    for i in np.arange(1,n,1):
       dl[i]=(d[i]-a[i]*dl[i-1])/(b[i]-a[i]*cl[i-1])
   
    #faz substituicao reversa para obter a solucao x
    x[n-1]=dl[n-1]   
    for i in np.arange(n-2,-1,-1):  
       x[i]=dl[i]-cl[i]*x[i+1]
  
    return x



