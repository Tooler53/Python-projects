import math

def gaussian(x, mu, sigma):
    return math.exp(-0.5*((x-mu)/sigma)**2) / sigma / math.sqrt(2*math.pi)

import numpy as np
import matplotlib.pyplot as plt

xs = np.arange(-5, 5, 1.00) # Сетка значений по оси абсцисс.
p1, = plt.plot(xs, [gaussian(x, 0, .5) for x in xs], label='$\sigma = 0.5$')
p2, = plt.plot(xs, [gaussian(x, 0, 1) for x in xs], label='$\sigma = 1$')
p3, = plt.plot(xs, [gaussian(x, 0, 2) for x in xs], label='$\sigma = 2$')
plt.legend()
plt.show()