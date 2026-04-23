if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()    
    temp=arr[n-1]
    for i in reversed(arr):
        if i < temp:
            temp=i
            break
    print(temp)
    
