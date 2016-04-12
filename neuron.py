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
gK = 36.
gNa = 120.
gL = 0.3
CM = 1.0
VK = -77.
VNa = 50.
VL = -54.4

# Constante auxiliar

phi = 3 * np.exp((temp - 6.3) / 10)

# Funciones auxiliares

def alpha_n(V):
    return phi * 0.01 * (V + 55) / (1 - np.exp(-0.1 * (V + 55)))
def beta_n(V): 
    return phi * 0.125 * np.exp(-0.0125 * (V + 65))
def alpha_m(V): 
    return phi * 0.1 * (V + 40) / (1 - np.exp(	-0.1 * (V + 40)))
def beta_m(V):
    return phi * 4.0 * np.exp(-0.0556 * (V + 65))
def alpha_h(V): 
    return phi * 0.07 * np.exp(-0.05 * (V + 65))
def beta_h(V):
    return phi / (1 + np.exp(-0.1 * (V + 35)))

def F(V, m, n, h):

	IK  = gK * n**4 * (V - VK)
	INa = gNa* m**3 * h *(V-VNa)
	IL  = gL * (V - VL)

	FV = (I - IK - INa - IL) / CM
	Fn = alpha_n(V) * (1-n) - beta_n(V) * (n)
	Fm = alpha_m(V) * (1-m) - beta_m(V) * (m)
	Fh = alpha_h(V) * (1-h) - beta_h(V) * (h)

	return FV, Fn, Fm, Fh

#tiempo

tmax = 4.0
dt = 1e-3

#array

t = np.arange(0, tmax, step = dt)
V = np.zeros(len(t))
n = np.zeros(len(t))
m = np.zeros(len(t))
h = np.zeros(len(t))

# Condiciones iniciales

V[0] = -65
n[0] = 0.317
m[0] = 0.05
h[0] = 0.6

# Arreglo con la operacion de Runge-kuta
for i in range(len(t)-1):

    FV1, Fn1, Fm1, Fh1 = F(V[i], n[i], m[i], h[i])
    
    V1 = V[i] + 0.5 * dt * FV1
    n1 = n[i] + 0.5 * dt * Fn1
    m1 = m[i] + 0.5 * dt * Fm1
    h1 = h[i] + 0.5 * dt * Fh1
    
    FV2, Fn2, fm2, fh2 = F(V1, n1, m1, h1)
    
    V[i+1]= V[i] + dt * FV1
    n[i+1]= n[i] + dt * Fn1
    m[i+1]= m[i] + dt * Fm1
    h[i+1]= h[i] + dt * Fh1
    
# se crean las interpolaciones

nint = interp1d(t, n)
mint = interp1d(t, m)
hint = interp1d(t, h)

t0 = 1.9999
print nint(t0), mint(t0), hint(t0)

# graficando a n,m,h en funcion del tiempo..... colores lineas y formas: - o brg
plt.plot(t, n, 'b-', t0, nint(t0), 'bo')
plt.plot(t, m, 'r-', t0, mint(t0), 'ro')
plt.plot(t, h, 'g-', t0, hint(t0), 'go')
plt.show()

# Grafica del potencial de accion	
plt.plot(t, V, 'k-')
plt.show()