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
n0 = 0.317
m0 = 0.05
h0 = 0.6
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

	n1 = ((dlt*(an*(1-n0)))-(dlt*(bn*n0)) + n0)
	m1 = ((dlt*(am*(1-m0)))-(dlt*(bm*m0)) + m0)
	h1 = ((dlt*(ah*(1-h0)))-(dlt*(bh*h0)) + h0)

	n0 = n1
	n[i] = n1

	m0 = m1
	m[i] = m1

	h0 = h1
	h[i] = h1

plt.plot(z, x)
plt.show()