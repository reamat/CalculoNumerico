// Gera o gráfico interpolacao_linear_segmentada.eps

// Coordenadas dos pontos
xi=0:5
yi=[0 4 3 0 2 0]

scf(0)

plot(xi,yi,'-')
plot(xi,yi,'.r')
xgrid
xs2eps(0,'interpolacao_linear_segmentada.test.eps')
exit()
