import numpy as np

def TDMA(a,b,c,d):
    #preliminares
    a = a.astype('double')
    b = b.astype('double')
    c = c.astype('double')
    d = d.astype('double')

    #recupera ordem do sistema
    n=np.shape(a)[0]
   
    #inicializa vetor x
    x=np.zeros(n)
    
    #calcula cl e dl sobrescrevendo-os em c e d
    c[0]=c[0]/b[0]
    for i in np.arange(1,n-1,1):
       c[i]=c[i]/(b[i]-a[i]*c[i-1])

    d[0]=d[0]/b[0]
    for i in np.arange(1,n,1):
       d[i]=(d[i]-a[i]*d[i-1])/(b[i]-a[i]*c[i-1])
   
    #faz substituicao reversa para obter a solucao x
    x[n-1]=d[n-1]   
    for i in np.arange(n-2,-1,-1):  
       x[i]=d[i]-c[i]*x[i+1]
  
    return x


