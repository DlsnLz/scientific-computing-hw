# Un nuevo codigo donde se crearan dos funciones: f(x) y g(x).
 
import numpy
import matplotlib
import matplotlib.pyplot

def funciong (t,r):
	return -r*t

def funcionf (z,delta,r):
	return z+delta*funciong(z,r)
u0= 0.1
delta = 0.01
r = 2.0
u= funcionf(t,delta,r)
print u


n = 100
t = range (n)
y = range (n)

for i in range(n):
	u = funcionf(t,delta,r)
	y[i] = u
	
