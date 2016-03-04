# Un nuevo codigo donde se crearan dos funciones: f(x) y g(x).

#Codigo del dia 23 de febrero; dos funciones g() y f() para un nuevo mapa logistico.
import numpy
import matplotlib
import matplotlib.pyplot

def funciong(t,r):
	return -r*t
def funcionf(z,delta,r):
	return z+delta*funciong(z,r)
y0=0.1
delta=0.01
r=2.0
y1=funcionf(y0,delta,r)
print y1

n=100
t=range(n)
y=range(n)
for i in range(n):
	y1=funcionf(y0,delta,r)
	y[i]=y1
	
