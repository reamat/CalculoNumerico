//entradas: vetores coluna a,b,c,d
//saida:    vetor coluna x
function x=TDMA(a,b,c,d)
    n=size(a,1) // Recupera ordem do sistema. 
    
    cl=zeros(n,1) //Inicializa cl
    dl=zeros(n,1) //Inicializa dl
    x=zeros(n,1) //Inicializa x
    
    cl(1)=c(1)/b(1)
    for i=2:n-1
        cl(i)=c(i)/(b(i)-a(i)*cl(i-1))
    end
  
    dl(1)=d(1)/b(1)
    for i=2:n
        dl(i)=(d(i)-a(i)*dl(i-1))/(b(i)-a(i)*cl(i-1))
    end
   
    x(n)=dl(n)   
    for i=n-1:-1:1
        x(i)=dl(i)-cl(i)*x(i+1)
    end    
endfunction
