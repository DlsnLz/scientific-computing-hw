# Problematica del fenomeno atmosferico

import numpy
import matplotlib
import matplotlib.pyplot

x0 = 0
y0 = 1
z0 = 1.05
sigma = 10
rho   = 28
beta  = 2.667
delta = 0.01
t = range (100001)
y = range (100001)
x = range (100001)
z = range (100001)

for i in range (100001):
	x1 = ((delta*sigma*y0)-(delta*sigma*x0)+x0)
	y1 = ((delta*x0*rho)-(delta*x0*z0)-(delta*y0)+y0)
	z1 = ((delta*x0*y0)-(delta*beta*z0)+z0)
	x0 = x1
	x[i] = x1
	y0 = y1
	y[i] = y1
	z0 = z1
	z[i] = z1

xnew=numpy.array(x)
ynew=numpy.array(y)
znew=numpy.array(z)
tnew=numpy.array(t)

print xnew
print ynew
print znew
print tnew


matplotlib.pyplot.plot(tnew,znew)
matplotlib.pyplot.plot(tnew,xnew)
matplotlib.pyplot.show()

matplotlib.pyplot.plot(xnew,znew)
matplotlib.pyplot.show()
