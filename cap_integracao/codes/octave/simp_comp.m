function [y] = simp_comp(f,a,b,n)
  h = (b-a)/(2*n)
  x = linspace(a,b,2*n+1)
  y = f(x(1))
  for i = 1:n-1
    y = y + 2*f(x(2*i+1))
  endfor
  for i = 1:n
    y = y + 4*f(x(2*i))
  endfor
  y = y + f(x(2*n+1))
  y = h*y/3
endfunction
