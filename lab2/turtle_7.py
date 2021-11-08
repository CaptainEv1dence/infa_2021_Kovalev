import turtle as tr
import numpy as np


i = 0
x = 0

while i < 100:
    tr.goto(x * np.cos(i), x * np.sin(x))
    x += 0.05
    i += 0.05
