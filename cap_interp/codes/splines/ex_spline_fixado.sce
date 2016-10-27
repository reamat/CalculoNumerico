//limpa memoria
clear A, B, a, b, c, d
//pontos fornecidos
xi = [0; %pi/2; %pi; 3*%pi/2; 2*%pi]
yi = sin(xi)
//numero de pontos
n = 5
disp('Pontos fornecidos:')
disp([xi, yi])
//vetor h
h = xi(2:n) - xi(1:n-1);
//matriz A
for i=1:n
    for j=1:n
        if ((j==1) & (i==1)) then
            A(i,j) = 2*h(1);
        elseif (j == i-1) then
            A(i,j) = h(i-1);
        elseif ((i>1) & (i<n) & (i==j)) then
            A(i,j) = 2*(h(i) + h(i-1));
        elseif (j==i+1) then
            A(i,j) = h(i);
        elseif ((j==n) & (i==n)) then
            A(i,j) = 2*h(n-1);
        else
            A(i,j) = 0;
        end
    end
end
disp('Matriz A:')
disp(A)
//vetor z
for i=1:n
  if ((i==1)) then
    z(i) = 3*(yi(2)-yi(1))/h(1) - 3*cos(xi(1));
  elseif ((i>1) & (i < n)) then
    z(i) = 3*(yi(i+1)-yi(i))/h(i) ...
           - 3*(yi(i) - yi(i-1))/h(i-1);
  elseif (i == n) then
    z(i) = 3*cos(xi(n)) - 3*(yi(n) - yi(n-1))/h(n-1);
  end
end
disp('Vetor z:')
disp(z)
//coeficientes c
c = inv(A)*z
disp('Coeficientes c:')
disp(c)
//coeficientes a
a = yi(1:n-1);
disp('Coeficientes a:')
disp(a)
//coeficientes b
for j=1:n-1
  b(j) = (3*yi(j+1) - 3*yi(j) - 2*c(j)*h(j)^2 ...
	  - c(j+1)*h(j)^2)/(3*h(j));
end
disp('Coeficientes b:')
disp(b)
//coeficientes d
for j=1:n-1
  d(j) = (c(j+1) - c(j))/(3*h(j));
end
disp('Coeficientes d:')
disp(d)
//spline cubico obtido
function [y] = s(x)
  for i=1:n-2
    if ((x>=xi(i)) & (x<xi(i+1))) then
      y = a(i) + b(i)*(x-xi(i)) ...
          + c(i)*(x-xi(i))^2 + d(i)*(x-xi(i))^3;
    end
  end
  if ((x>=xi(n-1)) & (x<=xi(n))) then
    y = a(n-1) + b(n-1)*(x-xi(n-1)) ...
        + c(n-1)*(x-xi(n-1))^2 + d(n-1)*(x-xi(n-1))^3;
  end
endfunction

