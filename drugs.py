# Funcion que identificara el tiempo en el que el cuerpo liberara la droga consumida por el paciente.
# Feb - 27,28,29 -2016
# Dlsn Lzro

# Librerias Necesarias importadas

import numpy
import matplotlib
import matplotlib.pyplot

# Datos de entrada.

k = 0.2
d = 0.1
q0 = 200
aux = q0

# Datos que me fabricaran la grafica.

y = range (101)
t = range (101)

# Funcion que me imprimira los resultados numericos por pantalla.

for i in range(101):
	q = q0-k*d*q0
	q0 = q
	y[i] = q

ynew=numpy.array(y)
tnew=numpy.array(t)
print ynew
print tnew

matplotlib.pyplot.plot(tnew,ynew)
matplotlib.pyplot.show()
