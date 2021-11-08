import numpy as np
import matplotlib.pyplot as plt


x = [2, 3, 4, 5, 6]
y = [5, 12, 17, 30, 40]

plt.errorbar(x, y, xerr = 0.05, yerr = 0.9, linestile = 'none')

p,v = np.polyfit(x, y, deg = 2, cov = True)
p_f = np.poly1d(p)
plt.plot(x, p_f(x))
plt.grid(True)
plt.show()