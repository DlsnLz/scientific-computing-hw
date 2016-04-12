# Funcion que identificara el tiempo en el que el cuerpo liberara la droga consumida por el paciente, aplicando el metodo de Runge-Kutta.
# yn + 1 = yn+delta+f(y)
# Marzo - 8 - 16
# Dlsn Lzro


import numpy
import matplotlib
import matplotlib.pyplot

k = 0.2
d = 0.1
q0 = 200
aux = q0
y = range (101)
t = range (101)

def f(q):
	return -k*q

for i in range(101):
	
	q = q0+d*f(q0+0.5*d*f(q0))
	q0 = q
	y[i] = q

ynew=numpy.array(y)
tnew=numpy.array(t)

print ynew
print tnew

matplotlib.pyplot.plot(tnew,ynew)
matplotlib.pyplot.show()