from __future__ import division

def bissecao(f, a, b, TOL, N):
    i = 1
    fa = f(a)
    while (i <= N):
        #iteracao da bissecao
        p = a + (b-a)/2
        fp = f(p)
        #condicao de parada
        if ((fp == 0) or ((b-a)/2 < TOL)):
            return p
        #bissecta o intervalo
        i = i+1
        if (fa * fp > 0):
            a = p
            fa = fp
        else:
            b = p
  
    raise NameError('Num. max. de iter. excedido!');
