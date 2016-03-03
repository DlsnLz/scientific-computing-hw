# Funion representativa de la grafica de que representara la extincion y propagacion de dos especies en relacion de un tiempo determinado.


import numpy
import matplotlib
import matplotlib.pyplot


# Proceso para -presa-

kx = 1.06
ky = 2.0
kxy = 0.01
kyx = 0.01
x0 = 15
y0 = 100
d = 0.3
y =  range(101)
t =  range(101)

for i in range(101) :
	y1 = ky*y0- kxy*x0*y0+y0*d
	y0 = y1
	y[i] = y1

ynew=numpy.array(y)
tnew=numpy.array(t)

print ynew
print tnew

matplotlib.pyplot.plot(tnew,ynew)
matplotlib.pyplot.show()
