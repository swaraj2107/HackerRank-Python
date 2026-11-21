import sys
import numpy

data = sys.stdin.read().split()        
n, m = int(data[0]), int(data[1])      

values = numpy.array(data[2:], dtype=int)
a = values[:n * m].reshape(n, m)       
b = values[n * m:2 * n * m].reshape(n, m) 

print(numpy.add(a, b))
print(numpy.subtract(a, b))
print(numpy.multiply(a, b))
print(numpy.floor_divide(a, b))
print(numpy.mod(a, b))
print(numpy.power(a, b))
