# Grafica del atractor de lorenz basado basado en el metodo de Edwar Lorenz 1993 " Metodo determinista no periodico "
# DlsnLz
# Universidad de Medellin
# Computacion cientifica _ I semestre
# Marzo 2016

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def lorenz(x, y, z, s=10, r=28, b=2.667):
    x_dot = s*(y - x)
    y_dot = r*x - y - x*z
    z_dot = x*y - b*z
    return x_dot, y_dot, z_dot


delta = 0.01
iteraciones  = 10000

# No se define un rango como arreglo, pero se sabe que para que los valores sean correctos hay que agreragarle 1 mas al ragno de manera que los valores  # iniciales queden completos.

xs = np.empty((iteraciones + 1,))
ys = np.empty((iteraciones + 1,))
zs = np.empty((iteraciones + 1,))

# Inicializando valores iniciales

xs[0], ys[0], zs[0] = (0., 1., 1.05)

# fijando arreglo para pasar a traves del tiempo.

for i in range(iteraciones):
  
    # Derivados comportamientos de el estado de x, y, z; arreglo que aumenta en cada variable 1 y va tomando su valor
   
    x_dot, y_dot, z_dot = lorenz(xs[i], ys[i], zs[i])
    
    xs[i + 1] = xs[i] + (x_dot * delta)
    ys[i + 1] = ys[i] + (y_dot * delta)
    zs[i + 1] = zs[i] + (z_dot * delta)

#Inicializacion de codigos que llaman figuras y trazos en 3d

fig = plt.figure()
ax = fig.gca(projection='3d')

# comando para graficar x,y,z y ademas, se le da titulo a la grafica.

ax.plot(xs, ys, zs)
ax.set_xlabel("X Axis")
ax.set_ylabel("Y Axis")
ax.set_zlabel("Z Axis")
ax.set_title("Lorenz Attractor")

plt.show()
