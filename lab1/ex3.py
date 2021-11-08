import numpy as np
import matplotlib.pyplot as plt


x = np.arange(10, 20, 0.2)
a = (x**2+1) * (np.e**(-abs(x)/10))
b = (1 + np.tan(1/(1+np.sin(x)**2)))
y = np.log(a) / np.log(b)
plt.plot(x, y, )
plt.show()