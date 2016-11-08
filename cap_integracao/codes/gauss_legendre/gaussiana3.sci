function S=gaussiana(a,b,n)
h=(b-a)/n             // n intervalos
x=linspace(a,b,n+1)

w1=5/9; t1=-sqrt(3/5);
w2=8/9; t2=0;
w3=w1;  t3=-t1;

S=0
for i=1:n
    alpha=(x(i+1)-x(i))/2
    bet  =(x(i+1)+x(i))/2 
    x1=alpha*t1+bet;
    x2=alpha*t2+bet;
    x3=alpha*t3+bet;
    
    A =(w1*f(x1)+w2*f(x2)+w3*f(x3))* h/2
    S=S+A
end
endfunction
