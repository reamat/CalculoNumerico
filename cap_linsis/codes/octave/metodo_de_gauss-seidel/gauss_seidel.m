function [x]=gauss_seidel(A,b,x,tol,N)
  n = size(A,1);
  x0 = x;
  iter = 1;
  while (iter <= N)
    #iteracao G-S
    for i = 1:n
      x(i) = (b(i) - A(i,[1:i-1,i+1:n])*x([1:i-1,i+1:n]))/A(i,i);
    endfor
    #condicao de parada
    if (norm(x-x0,'inf')<tol)
      return
    endif
    #prepara nova iteracao
    x0 = x;
    iter += 1;
  endwhile
  error('num. max. iter. excedido.')  
endfunction

