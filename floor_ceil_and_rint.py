# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy as np
np.set_printoptions(legacy='1.13')

array=input().split()
arr=[]

for i in array:
    arr.append(float(i))
    
print(np.floor(arr))
print(np.ceil(arr))
print(np.rint(arr))
