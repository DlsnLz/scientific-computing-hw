# simular el automata celular de la hormiga de langton
import numpy as np 
import matplotlib as plt
import matplotlib.pyplot as mplt

n = 100
w = np.zeros([n, n], dtype = np.int8)

# direcciones
def nextdirection(d, c):
	
	if 0 =< d and d =< 4:

		if d == 0 and c == 0:
			dn = 1
		else:
		if d == 0 and c == 1:
			dn = 3


		if d == 1 and c == 0:
			dn = 2
		else:
		if d == 1 and c == 1:
			dn = 0


		if d == 2 and c == 0:
			dn = 3
		else:
		if d == 2 and c == 1:
			dn = 1

		if d == 3 and c == 0:
			dn = 0
		else:
		if d == 3 and c == 1:
			dn = 2
	return dn

		
	



