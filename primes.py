# esta funcion define si un numero es menor que otro.

def minimo (x,y):
	if x < y:
		return x
	else:
		return y

def mcd (x,y):
	m = minimo(x,y)
	for i in range (m,0,-1):
		if x % i == 0 and y % i == 0:
			return i
# esta funcion define si un numero es comprimo o no.

def arecoprime (a,b):

	m = mcd (a,b)

	if m==1:
		return 1
	else:
		return 0


print arecoprime (10,12)
