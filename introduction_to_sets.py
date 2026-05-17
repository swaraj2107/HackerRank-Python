def average(array):
    res=set(array)
    return round((sum(res)/len(res)),3)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
