import numpy as np
import matplotlib.pyplot as plt


x = np.arange(-2.25,3.25, 0.01 )
plt.plot(x, x**2 - x - 6 , x , x*0)
plt.show()