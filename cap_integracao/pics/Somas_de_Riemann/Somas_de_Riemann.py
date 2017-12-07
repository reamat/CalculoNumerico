#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt

#font letter
plt.rc('text', usetex=True)
plt.rc('font', family='serif', size=12)

#figure
fig = plt.figure(figsize=(6,4), dpi=100, 
                 linewidth=0.0, facecolor="white")
ax = plt.subplot(1,1,1)
ax.set_axis_off()
ax.grid("off")
ax.set_xlim(-0.1,1.7)
ax.set_ylim(-0.05,0.4)

#axes
ax.arrow(-0.1,0,1.8,0,length_includes_head=True,
             head_width=0.01, head_length=0.03)
ax.text(1.7-0.05,-0.02,r"$x$")
ax.arrow(0,-0.05,0,0.45,length_includes_head=True,
             head_width=0.03, head_length=0.01)
ax.text(-0.06,0.38,r"$y$")


#fun
ax.text(1.3,0.275,r"$y=f(x)$")
def f(x):
    return np.exp(-x)*np.sin(x)

#integral limits
a = 0.1
b = 1.5
ax.text(a-0.01,-0.02,r"$a$")
ax.plot([a,a],[0,f(a)],color="black",linestyle="dashed")
ax.text(b-0.01,-0.02,r"$b$")
ax.plot([b,b],[0,f(b)],color="black",linestyle="dashed")

#plot fun
xx = np.linspace(a,b)
yy = f(xx)
ax.plot(xx,yy)

#fill area
ax.fill(xx,yy,color="blue",alpha=0.1,linewidth=0)
ax.fill([a,a,b,b],[0,f(a),f(b),0],color="blue",alpha=0.1,linewidth=0)

#bars
x = [a,0.5,0.8,1.2,b]
xs = [0.4,0.65,0.9,1.35]

ax.text(x[0]-0.01,-0.04,r"$x_1$")
ax.plot([xs[0],xs[0]],[0,f(xs[0])],color="black",linestyle="dashed")
ax.text(xs[0]-0.015,-0.03,r"$x_1^*$")
ax.plot([x[0],x[0],x[1],x[1]],[0,f(xs[0]),f(xs[0]),0],color="red")
ax.fill([x[0],x[0],x[1],x[1]],[0,f(xs[0]),f(xs[0]),0],
            color="red",alpha=0.1)
ax.text(x[1]-0.015,-0.03,r"$x_2$")

#ax.plot([xs[1],xs[1]],[0,f(xs[1])],color="black",linestyle="dashed")
ax.text(xs[1]-0.015,-0.03,r"$\cdots$")
ax.plot([x[1],x[1],x[2],x[2]],[0,f(xs[1]),f(xs[1]),0],color="red")
ax.fill([x[1],x[1],x[2],x[2]],[0,f(xs[1]),f(xs[1]),0],
            color="red",alpha=0.1)

ax.text(x[2]-0.015,-0.03,r"$x_i$")
ax.plot([xs[2],xs[2]],[0,f(xs[2])],color="black",linestyle="dashed")
ax.text(xs[2]-0.015,-0.03,r"$x_i^*$")
ax.plot([x[2],x[2],x[3],x[3]],[0,f(xs[2]),f(xs[2]),0],color="red")
ax.fill([x[2],x[2],x[3],x[3]],[0,f(xs[2]),f(xs[2]),0],
            color="red",alpha=0.1)
ax.text(x[3]-0.015,-0.03,r"$x_{i+1}$")

#ax.plot([xs[3],xs[3]],[0,f(xs[3])],color="black",linestyle="dashed")
ax.text(xs[3]-0.015,-0.03,r"$\cdots$")
ax.plot([x[3],x[3],x[4],x[4]],[0,f(xs[3]),f(xs[3]),0],color="red")
ax.fill([x[3],x[3],x[4],x[4]],[0,f(xs[3]),f(xs[3]),0],
            color="red",alpha=0.1)
ax.text(x[4]-0.015,-0.04,r"$x_n$")

fig.savefig("Somas_de_Riemann.eps",bbox_inches="tight")
fig.savefig("Somas_de_Riemann.png",bbox_inches="tight")
plt.show()
