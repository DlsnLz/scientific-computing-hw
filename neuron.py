# Construir las funciones n, m y h en el rango de 0-5 milisegundos.
# Hallar las interpolaciones para estas funciones: Saber cuanto pueden valer en cada punto.
# Hallar potencial de activacion neuronal (V)

import numpy as np
import matplotlib
import matplotlib.pyplot as plt

def f(n, m, h):
      
      N = alpha_n * (1-n0) - beta_n * n0
      M = alpha_m * (1-m0) - beta_m * m0
      H = alpha_h * (1-h0) - beta_h * h0
      
      return N, M, H

d1 = 0.003

n0 = 0.317
m0 = 0.05
h0 = 0.6
v = 77
temp = 6.3 # Grados centigrados (C)
phi = 3 * np.exp(temp-6.3)/10
alpha_n = phi *(0.01 * (-v + 10)/(np.exp((-v  + 10) / 10))-1)
beta_n = phi *(0.125 * np.exp(-v/80))
alpha_m = phi *(0.01 * (-v + 25)/(np.exp(-v + 25) / 10) -1)
beta_m = phi *(4 * np.exp(-v / 18))
alpha_h = phi *(0.07 * np.exp(-v / 20))
beta_h = phi *(1 / (np.exp(-v + 30) / 10) + 1)

n = 5 / d1
t = np.linspace(0, 5, num = n)
n = np.zeros(len(t))
m = np.zeros(len(t))
h = np.zeros(len(t))

for j in range(len(t)):

      N, M, H = f(n0, m0, h0)
      
      L = n0 + d1 * (n0+0.5*d1*N)
      M = m0 + d1 * (m0+0.5*d1*M) 
      R = h0 + d1 * (h0+0.5*d1*H)
      
      n0 = L
      m0 = M
      h0 = R
      
      n[j] = L
      m[j] = M
      h[j] = R
    
plt.plot(t, n)
plt.show()
  
