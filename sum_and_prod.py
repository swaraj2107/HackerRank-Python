# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy as np

dim=input().split()
list1=[]

for i in range(int(dim[0])):
    b=[]
    a=input().split()
    for i in a:
        b.append(int(i))
    list1.append(b)
    
arr=np.array(list1)
print(np.prod(np.sum(arr,axis=0)))
