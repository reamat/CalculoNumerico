function y=f(x)
    y=((1+x)-1)./x
endfunction

xp=linspace(1e-14,5e-17,1000)

scf(0)
plot2d('ln',xp,f(xp),style=[2],rect=[5e-17,-0.2,1e-14,2])

a=gca()
a.axes_reverse=['on','off','off']
a.box='on'
xs2pdf(0,'cancelamento_0.pdf')
exit()
