function y=f(x)
    y=(1+x.^-1).^x
endfunction

xp=logspace(14,16,1000)

scf(0)
plot2d('ln',xp,f(xp),style=[2],rect=[1e14,0,1e16,8])

a=gca()
//a.axes_reverse=['on','off','off']
//a.box='on'
xs2pdf(0,'cancelamento_euler2.pdf')
exit()
