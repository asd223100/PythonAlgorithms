import matplotlib.pyplot as plot
import numpy as np

xpt = np.linspace(1, 10, 100)
constant = xpt / xpt
log = np.log2(xpt)
linear = xpt
nlogn = xpt * np.log2(xpt)
quadratic = xpt * xpt
polynomial=xpt**2
exponential = 2 ** xpt
plot.plot(xpt, constant, label='O(1)')
plot.plot(xpt, log, label='O(logn)')
plot.plot(xpt, linear, label='O(n)')
plot.plot(xpt, nlogn, label='O(nlogn)')
plot.plot(xpt, quadratic, label='O(n*n)')
plot.plot(xpt, polynomial, label='O(n^2)')
plot.plot(xpt, exponential, label='O(2^n)')
plot.legend(loc='best')
plot.show()
