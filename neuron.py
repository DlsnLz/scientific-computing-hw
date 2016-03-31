# Construir las funciones n, m y h en el rango de 0-5 milisegundos.
# Hallar las interpolaciones para estas funciones: Saber cuanto pueden valer en cada punto.

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import sys

x  = range(6)
y  = range(6)
z  = range(6)
dlt= 0.001
v  = -65
x0 = 0.317
y0 = 0.05
z0 = 0.6
T  = 6.3
phi= 3 **((T-6.3)/10)
bn = phi*(0.125 ** (v/80))
an = phi*(0.01*(v+25))/np.exp(((v+10)/10)-1)
bm = phi*(4 ** (4/18))
am = phi*(0.01*(v+25))/np.exp(((v+25)/10)-1)
bh = phi*(1/np.exp(((v+30)/10)+1))
ah = phi*(0.07 ** (v/20))


def f(n, m, h):
  
	n = an*(1-n)-bn*n0
	m = am*(1-m)-bm*m0
	h = ah*(1-h)-bh*h0
	
	return n, m, h
   
for i in range(6):

	x1 = ((dlt*(an*(1-x0)))-(dlt*(bn*x0)) + x0)
	y1 = ((dlt*(am*(1-y0)))-(dlt*(bm*y0)) + y0)
	z1 = ((dlt*(ah*(1-z0)))-(dlt*(bh*z0)) + z0)

	x0 = x1
	x[i] = x1

	y0 = y1
	y[i] = y1

	z0 = z1
	z[i] = z1

plt.plot()
plt.show()