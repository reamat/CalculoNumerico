function [p] = bissecao(f, a, b, TOL, N)
  fa = f(a)
  for i = 0:N do
    //raiz aproximada
    p = a + (b-a)/2
    fp = f(p)
    //condicao de parada
    if ((fp == 0) | ((b-a)/2 < TOL)) then
      return
    end
    //bissecta o intervalo
    if (fa * fp > 0) then
      a = p
    else
      b = p
    end
  end
  error ('Num. max. de iter. excedido!')
endfunction
