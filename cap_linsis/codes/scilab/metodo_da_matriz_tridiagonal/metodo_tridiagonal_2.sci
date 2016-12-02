//entradas: vetores coluna a,b,c,d
//saida:    vetor coluna x
function x=TDMA2(a,b,c,d)
    n=size(a,1) // Recupera ordem do sistema.
    x=zeros(n,1) //Inicializa x

    c(1)=c(1)/b(1)
    for i=2:n-1
        c(i)=c(i)/(b(i)-a(i)*c(i-1))
    end
  
    d(1)=d(1)/b(1)
    for i=2:n
        d(i)=(d(i)-a(i)*d(i-1))/(b(i)-a(i)*c(i-1))
    end
   
    x(n)=d(n)   
    for i=n-1:-1:1
        x(i)=d(i)-c(i)*x(i+1)
    end    
endfunction
