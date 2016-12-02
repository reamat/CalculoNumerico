function [x] = newton(F,JF,x0,TOL,N)
  x = x0    
  k = 1
  #iteracoes
  while (k <= N)
    #iteracao de Newton
    delta = -inv(JF(x))*F(x)
    x = x + delta
    #criterio de parada
    if (norm(delta,'inf')<TOL) then
      return
    endif
    k = k+1
  endwhile
  error('Num. de iter. max. atingido!')
endfunction
