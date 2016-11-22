function [L,A]=fatoraLU(A)
    n=size(A,1)
    L=eye(n,n)
    for j=1:n-1
        for i=j+1:n
            L(i,j    )=A(i,j)/A(j,j)
            A(i,j+1:n)=A(i,j+1:n)-L(i,j)*A(j,j+1:n)
            A(i,j    )=0
        end
    end
endfunction
