# Funcion que identificara el tiempo en el que el cuerpo liberara la droga consumida por el paciente, aplicando el metodo de Runge-Kutta.
# yn + 1 = yn+deltat+f(y)


import numpy
import matplotlib
import matplotlib.pyplot

k = 0.2
d = 0.1
q0 = 200
rango = 101
t = range (rango)
y = range (rango)
aux = q0

def funcion(qn):
	return -k*qn

for i in range(rango):

	q = funcionq*d*q0
	q0 = q
	y[i] = q


ynew=numpy.array(y)
tnew=numpy.array(t)
print ynew
print tnew

matplotlib.pyplot.plot(tnew,ynew)
matplotlib.pyplot.show()
	

