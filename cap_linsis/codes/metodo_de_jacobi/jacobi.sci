function [x,deltax]=jacobi(A,b,x,tol,N)
n=size(A,1)
xnew     =x
convergiu=%F                //FALSE;

k=1
while k<=N & ~convergiu 
  xnew(1)=(b(1) - A(1,2:n)*x(2:n))/A(1,1)
  for i=2:n-1
    xnew(i)=(b(i) -A(i,1:i-1)*x(1:i-1) ...
                  -A(i,i+1:n)*x(i+1:n) )/A(i,i)
  end
  xnew(n)=  (b(n) -A(n,1:n-1)*x(1:n-1) )/A(n,n)

  deltax=max( abs(x-xnew) )
  if deltax<tol then
     convergiu=%T       //TRUE
  end
  k=k+1    
  x=xnew                 // atualiza x
  disp([k,x',deltax])    // depuracao
end
if ~convergiu then
    error('Nao convergiu')
end
       
endfunction

