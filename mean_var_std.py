import numpy as np

dim=input().split()
list1=[]

for i in range(int(dim[0])):
    b=[]
    a=input().split()
    for i in a:
        b.append(float(i))
    list1.append(b)
    
arr=np.array(list1)
print(np.mean(arr,axis=1))
print(np.var(arr,axis=0))
val=round(np.std(arr,axis=None),11)
print(val)
