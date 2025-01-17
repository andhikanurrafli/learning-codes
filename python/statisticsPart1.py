
import numpy
from scipy import stats

# learning how to create a histogram and mathplot in python

gameSizes = numpy.random.randint(1,10, size=20)
print(gameSizes)

x = numpy.mean(gameSizes)
print(x)

y =numpy.median(gameSizes)
print(y)

z = stats.mode(gameSizes)
print(z)

print('latihan statistik 1')
print('Mean dari my_data adalah:',x)
print('median adalah', y)
print('modus:',z.mode)


import matplotlib.pyplot as plt

plt.hist(gameSizes, bins=10)
plt.xlabel('Size (gigabyte)')
plt.ylabel('Game Count')
plt.title('Game Size Numbers')
plt.show()
