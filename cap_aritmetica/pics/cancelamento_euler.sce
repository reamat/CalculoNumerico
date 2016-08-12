function y=f(x)
    y=(1+x.^-1).^x
endfunction

xp=logspace(0,18,1000)

scf(0)
plot2d('ln',xp,f(xp),style=[2],rect=[1,0,1e18,8])

a=gca()
//a.axes_reverse=['on','off','off']
//a.box='on'
xs2pdf(0,'cancelamento_euler.pdf')
exit()