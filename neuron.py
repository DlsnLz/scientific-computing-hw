# Construir las funciones n, m y h en el rango de 0-5 milisegundos.
# Hallar las interpolaciones para estas funciones: Saber cuanto pueden valer en cada punto.
# Hallar potencial de activacion neuronal (V)

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

#Constantes

temp = 6.3 
I = 15e-3
gK = 36
gNa = 120
gL = 0.3
CM = 1.0
VK = -77
VNa = 50
VL = -54.4

# Constante auxiliar
phi = 3 * np.exp((temp-6.3)/10)

def alpha_n(V):
	return phi *(0.01 * (V + 10)/(np.exp((V+ 10) / 10))-1)

def beta_n(V): 
	return phi *(0.125 * np.exp(V/80))
def alpha_m(V): 
	return phi *(0.01 * (V + 25)/(np.exp(V + 25) / 10) -1)
def beta_m(V):
 	return phi *(4 * np.exp(V / 18))
def alpha_h(V): 
	return phi *(0.07 * np.exp(V / 20))
def beta_h(V):
	return phi *(1 / (np.exp(V + 30) / 10) + 1)

def F(V, m, n, h):

	IK = gK * n ** 4 * (V - VK)
	INa = gNa * m ** 3 * h *(V-VNa)
	IL = gL * (V - VL)

	FV = (I - IK - INa - IL) / CM
	fn = alpha_n(V) * (1-n) - beta_n * (n)
      	fm = alpha_m(V) * (1-m) - beta_m * (m)
      	fh = alpha_h(V) * (1-h) - beta_h * (h)

	return FV, fn, fm, fh

# se crean las interpolaciones

nint = interp1d(t, n)
mint = interp1d(t, m)
hint = interp1d(t, h)

t0 = 2.55352
print nint(t0), mint(t0), hint(t0)

# graficando a n,m,h en funcion del tiempo..... colores lineas y formas: - o brg
plt.plot(t, n, 'b-', t0, nint(t0), 'bo')
plt.plot(t, m, 'r-', t0, mint(t0), 'ro')
plt.plot(t, h, 'g-', t0, hint(t0), 'go')
plt.show()

# Grafica del potencial de accion	
plt.plot(t, V, 'k-')
plt.show()
  
