function y=f(x)
    y=exp(x)
endfunction

a=0;
b=1;

exato=exp(1)-exp(0)
for k=1:8
    n=2^k;
    T(k,1)=trapezio(a,b,n)
    S(k,1)=simpson(a,b,n)
   // T(k,2)=abs( exato-T(k,1))
    if(k~=1) then
        //S(k,3)=S(k-1,2)/S(k,2)
    end
end
disp(T)
