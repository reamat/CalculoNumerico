// Gera o gráfico interpolacao_linear_segmentada.eps

// Coordenadas dos pontos
x=linspace(0,2)

// Curva 1+x^2
plot(x,1+x.^2,'k')

// Reta na extremidade direita do gráfico
plot([0 2],[1 5],'r')



// Desativando a caixa em volta do gráfico
a=gca()
a.box='on'
a.sub_ticks=[1,0]
a.x_location='origin'
a.x_label.auto_position='off'
a.x_label.position=[2.05 -0.1]
a.x_label.text='x'
//a.x_label.text.font_size=2
a.x_ticks.locations=0:0.2:2
a.x_ticks.labels=['$\text{x}_0=\text{a}$','','','','','','','','','','$\text{x}_1=\text{b}$']
a.y_location='origin'
a.y_label.auto_position='off'
a.y_label.position=[-.08 5.05]
a.y_label.text='f(x)'
a.y_label.font_angle=0
// É necessário redefinir y_tick.locations e y_tick.labels pois a dimensão 
// inicial é diferente da que está sendo redefinida. 
a.y_ticks=tlist(["ticks", "locations", "labels"],0:0.5:5,repmat('',1,11))



xs2eps(0,'int_2.eps')
exit()
