import numpy as np


for i in range (3):
	x = int(input())
	z = np.e**(1/np.sin(x)+1)
	a = 1.25 + (1/(x**15))
	y = np.log(z/a) / (np.log(1 + x**2))

	print('f = ', y, ' for x =' , x)