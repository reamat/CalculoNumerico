from __future__ import division

import numpy as np

def metodo_potencias(A, x0, tol=1e-10, it_max=1000):
    x = np.copy(x0)
    p = np.argmax(x)

    x = x/x[p]

    for i in range(it_max):
        y = np.dot(A, x)
        u = y[p]  # lambda = autovalor
        p = np.argmax(y)
        if y[p] == 0:
            return 0, x
        x1 = y/y[p]
        if np.abs(x - x1).max() < tol:  # verificando a tolerancia
            return u, x1
        x = x1

    raise NameError('num. max. de iteracoes excedido.')

A = np.array([
        [1, 0, 0],
        [2, 3, 0],
        [3, 4, 2]
        ])

x0 = np.ones((3, 1))  # Aproximacao inicial

u, x = metodo_potencias(A, x0)
print(u)
print(x.T)
