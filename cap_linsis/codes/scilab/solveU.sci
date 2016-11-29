function [x]=solveU(U,b)  // U:= matriz triangular superior
   n=size(U,1)           // b:= vetor
   x(n)=b(n)/U(n,n)
   for i=n-1:-1:1
        x(i)=(b(i)-U(i,i+1:n)*x(i+1:n)  )/U(i,i)
    end
endfunction
