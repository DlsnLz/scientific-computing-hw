# Construir las funciones n, m y h en el rango de 0-5 milisegundos.
# Hallar las interpolaciones para estas funciones: Saber cuanto pueden valer en cada punto.
# Hallar potencial de activacion neuronal (V)

import numpy as np
import matplotlib
import matplotlib.pyplot as plt


temp = 6.3 # Grados centigrados (C)
phi = 3 * np.exp(temp-6.3)/10

# particula de activacion de potasio
alpha_n = lambda v: phi *(0.01 * (-v + 10)/(np.exp((-v  + 10) / 10))-1) if v!= 10 else 0.1
beta_n  = lambda v: phi *(0.125 * np.exp(-v/80))
n_inf   = lambda v: alpha_n(-v)/(alpha_n(-v)+beta_n(-v))

# Las particulas m y h son numeros adimensionales entre 0 y 1.
# particula de activacion del sodio (Na)
alpha_m = lambda v: phi *(0.01 * (-v + 25)/(np.exp(-v + 25) / 10) -1)  if v!= 25 else 1  
beta_m  = lambda v: phi *(4 * np.exp(-v / 18))
m_inf   = lambda v: alpha_m(-v)/(alpha_m(-v)+beta_m(-v))

# particula de inactivacion del sodio (Na)
alpha_h = lambda v: phi *(0.07 * np.exp(-v / 20))
beta_h  = lambda v: phi *(1 / (np.exp(-v + 30) / 10) + 1)
h_inf   = lambda v: alpha_h(-v)/(alpha_h(-v)+beta_h(-v))

g_Na = 120    # Conductancia maxima de Na (mS/cm)
g_k  = 36     # Conductancia maxima de K  (mS/cm)
g_L  = 0.3    # conductancia maxima de escape (mS/cm)
v_Na = 50     # Desplazamiento del potencial de equilibrio de Na (mV)
v_k  = -77    # Desplazamiento del potencial de equilibrio de K (mV)
v_l  = -54    # Desplazamiento del potencial de equilibrio de fuga (mV)
c_m  = 0.1    # Capacitancia de la membrana (uF/cm)

delta = 0.003
t = (0, 6, delta)
v = np.zeros(len(t))
    
plt.plot(b)
plt.show()
  
