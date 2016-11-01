// Gera o gráfico interpolacao_linear_segmentada.eps

// Coordenadas dos pontos
x=linspace(0,2)

// Curva 1+x^2
plot(x,1+x.^2,'k')

// Reta na extremidade direita do gráfico
plot([2 2],[0 5],'k')

// Barras verdes
plot([0,0.5,0.5],[1+0.25^2,1+0.25^2,0],'g')
plot([0.5,0.5,1,1],[0,1+0.75^2,1+0.75^2,0],'g')
plot([1,1,1.5,1.5],[0,1+1.25^2,1+1.25^2,0],'g')
plot([1.5,1.5,2],[0,1+1.75^2,1+1.75^2],'g')

// Barras vermelhas
plot([0,1,1],[1+0.5^2,1+0.5^2,0],'r')
plot([1,1,2],[0,1+1.5^2,1+1.5^2],'r')

// Barra preta
plot([0 2],[2 2],'k')

// Desativando a caixa em volta do gráfico
a=gca()
a.box='off'

// Mudando a cor das barras verdes -> verde escuro
for n=4:7
    p=a.children(n)
    p.children.foreground=13
end

xs2eps(0,'int_1.eps')
exit()
