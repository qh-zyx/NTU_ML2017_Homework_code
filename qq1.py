import numpy
import numpy as np
dataA = 'data/matrixA.txt'
dataB = 'data/matrixB.txt'

p = np.loadtxt(dataA, delimiter=',')
# print(p)

p2 = np.loadtxt(dataB, delimiter=',')
# print(p2)

result = p @ p2

resultSorted = np.sort(result, kind='quicksort')

np.savetxt("result.txt", resultSorted, fmt='%d')



