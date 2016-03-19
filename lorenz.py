# ATRACTOR DE LORENZ: Es un sistema dinamico determinista tridimensional no lineal derivado de las ecuaciones                                       #                     simplificadas de rollos de conveccion que se producen en las ecuaciones dinamicas de la              #                     atmosfera terrestre.

# Problematica del fenomeno atmosferico
# Graficar x en funcion de z
# DlsnLz _ Universidad de Medellin
# Computacion cientifica _ I semestre

#Numpy es el encargado de anadir toda la capacidad matematica y vectorial a Python haciendo posible operar con #cualquier dato numerico o array (Un array es el termino que traslada el concepto matematico de vector o matriz a la  #programacion anadiendole la nocion de almacenamiento en memoria.). 

# matplotlib.pyplot es una coleccion de funciones de estilo de comandos que hacen el trabajo matplotlib como MATLAB.   # Cada pyplot funcion hace algun cambio a una figura: por ejemplo, crea una figura, crea un area de trazado en una    # figura, traza algunas lineas en un area de trazado, decora la parcela con etiquetas, etc.

import numpy                
import matplotlib
import matplotlib.pyplot

x0 = 0
y0 = 1
z0 = 1.05
r = 10
p = 28
b = 2.667
delta = 0.01
y = range (100001)     # el range sale de la operacion delta/t; t == 100.
x = range (100001)
z = range (100001)

for i in range (100001):
  
	x1 = (delta * r * y0 - delta * r * x0 + x0)
	
	x0   = x1
	x[i] = x1
	
	y1 = ((delta * (x0 * p - x0 * z0 - y0)) + y0)
	
	y0   = y1
	y[i] = y1
	
	z1 = ((delta * (x0 * y0 - b * z0)) + z0)
	
	z0   = z1
	z[i] = z1

xnew=numpy.array(x)
znew=numpy.array(z)

print xnew            #comandos que indican que se imprima una grafica con x en funcion de z
print znew

matplotlib.pyplot.plot(xnew,znew)
matplotlib.pyplot.show()
