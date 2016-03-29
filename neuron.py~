# Construir las funciones n, m y h en el rango de 0-5 milisegundos.
# Hallar las interpolaciones para estas funciones: Saber cuanto pueden valer en cada punto.

import numpy as np
import matplotlib
import matplotlib.pyplot as plt

d  = 0.001
n0 = 0.317
v0 = -65
T  = 6.3
phi= 3 ** ((T - 6.3)/10)
bn = phi*(0.125 ** (v/80))
an = phi*(0.01*(v+25)/(np.exp((v+10)/10)-1))



def f(n, m, h):
	
	N = (d*(an*(1-n0))-d*(bn*n)+
	|
