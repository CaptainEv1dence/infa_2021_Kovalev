import numpy as np
import matplotlib.pyplot as plt


details = 1000

xmin = -2
xmax = 2
points = np.arange(xmin,xmax,((xmax-xmin)/details))

def weierstrass(x,Nvar):
    we = np.zeros(details)
    for n in range(0,Nvar):
        we = we + np.cos( 3**n * np.pi * x) / 2**n
    return we

plt.plot(points, np.reshape(weierstrass(points, 500),(details)))
plt.show()