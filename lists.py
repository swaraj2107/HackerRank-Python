if __name__ == '__main__':
    N = int(input())
    list2=[]
    list1=[]
    for i in range(N):
        a=input().split(" ")
        list1.append(a)
    
    for i in list1:
        if i[0]=='insert':
            pos=int(i[1])
            val=int(i[2])
            list2.insert(pos,val)
        if i[0]=='print':
            print(list2)
        if i[0]=='remove':
            val=int(i[1])
            list2.remove(val)
        if i[0]=='append':
            val=int(i[1])
            list2.append(val)
        if i[0]=='sort':
            list2.sort()
        if i[0]=='pop':
            list2.pop(-1)
        if i[0]=='reverse':
            list2.reverse()
        
