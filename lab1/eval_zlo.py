import matplotlib.pyplot as plt

x = []
y = []
n = 100

with plt.xkcd():
    for i in range (n):
            x.append(float(eval(input())))
            y.append(x[i]**2)
            plt.plot(x, y)
            plt.draw()
            plt.show()