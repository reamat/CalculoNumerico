function [y] = trap_comp(f,a,b,n)
  h = (b-a)/n
  x = linspace(a,b,n+1)
  y = h*(f(x(1)) + f(x(n+1)))/2
  for i = 2:n
    y = y + h*f(x(i))
  end
endfunction
