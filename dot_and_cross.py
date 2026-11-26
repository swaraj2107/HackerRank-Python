import sys
import numpy

data = sys.stdin.read().split()        
n = int(data[0])      

values = numpy.array(data[1:], dtype=int)
a = values[:n * n].reshape(n, n)       
b = values[n * n:2 * n * n].reshape(n, n) 

print(numpy.dot(a, b))
