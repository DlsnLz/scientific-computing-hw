# realaizar la funcion del crecimiento y decrecimiento de la relacion de predador y presa


import numpy
import matplotlib
import matplotlib.pyplot


x0 = 15
y0 = 100
kx = 1.06
ky = 2.0
kxy = 0.01
kyx = 0.01
d = 0.1
y = range (101)
t = range (101)
x = range (101)


for i in range (101):
	
	y1 = y0+d*((kx*y0)-(kxy*x0*y0))
	x1 = x0+d*((kyx*y0*x0)-(kx*x0))
	
	y0 = y1
	y[i] = y1
	
	x0 = x1
	x[i] = x1

xnew=numpy.array(x)
ynew=numpy.array(y)

print xnew
print ynew

matplotlib.pyplot.plot(ynew,xnew)
matplotlib.pyplot.show()

