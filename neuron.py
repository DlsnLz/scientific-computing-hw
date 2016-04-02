# Construir las funciones n, m y h en el rango de 0-5 milisegundos.
# Hallar las interpolaciones para estas funciones: Saber cuanto pueden valer en cada punto.
# Hallar potencial de activacion neuronal.

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

def fun(n, m, h):
  
  N = an * (1-n) - bn * n
  M = am * (1-m) - bm * m
  H = ah * (1-h) - bh * h
  
  return N, M, H

delta = 0.003
T = 6.3
v = -65
phi= 3 * np.exp ( (T-6.3) / 10 )
bn = phi * ( 0.125 * np.exp (v / 80) )
an = phi * ( 0.01 * ( v + 25 ) ) / np.exp ( ( (v+10) / 10 ) -1 )
bm = phi * ( 4 * np.exp ( 4 / 18 ) )
am = phi * ( 0.01 * ( v + 25 ) ) / np.exp ( ( ( v + 25 ) / 10)-1)
bh = phi * ( 1 / np.exp ((( v + 30 ) / 10 ) + 1 ) )
ah = phi * ( 0.07 * np.exp ( v / 20 ) )

t = np.linspace (0, 10, num=10, endpoint = True)
n = np.cos(-x**2 / 9)
f = interp1d(x, y, kind = 'cubic')

plt.plot (t, n)
plt.show
