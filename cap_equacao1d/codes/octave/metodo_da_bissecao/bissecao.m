function [p] = bissecao(f, a, b, TOL, N)
  i = 1;
  fa = f(a);
  while (i <= N)
    #iteracao da bissecao
    p = a + (b-a)/2;
    fp = f(p);
    #condicao de parada
    if ((fp == 0) || ((b-a)/2 < TOL))
      return;
    endif
    #bissecta o intervalo
    i = i+1;
    if (fa * fp > 0)
      a = p;
      fa = fp;
    else
      b = p;
    endif
  endwhile
  error ('Num. max. de iter. excedido!');
endfunction
