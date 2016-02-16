def minimo (x,y)
	if x<y
		return x
	else 
		return y
s = minime (2,7)


def mcd (x,y)
	m = minimo(x,y)
	for i in (m,0,-1):
		if x%i == 0 and y%i == 0
		return i
