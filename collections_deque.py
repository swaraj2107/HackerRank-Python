from collections import deque

def solve():
    d = deque()
    try:
        n = int(input())
    except EOFError:
        return
    for _ in range(n):
        line = input().split()
        method_name = line[0]
        if len(line) > 1:
            getattr(d, method_name)(line[1])
        else:
            getattr(d, method_name)()
    print(*(d))

if __name__ == "__main__":
    solve()
