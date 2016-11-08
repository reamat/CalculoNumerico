// Gera o gráfico interpolacao_linear_segmentada.eps

// Coordenadas dos pontos
xi=0:10
yi=[1.95 1.67 3.71 3.37 5.12 5.79 7.5 7.55 9.33 9.41 11.48]

f=scf(0)

plot(xi,yi)

a=gca()
a.box='off'

p=get('hdl')
p.children.mark_mode='on'
p.children.mark_style=4
p.children.mark_size=10
p.children.line_mode='off'
//xgrid
xs2eps(0,'graf_der.eps')
exit()
