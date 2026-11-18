import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return 
    a = int(input_data[0])
    b = int(input_data[1])
    m = int(input_data[2])
    print(pow(a, b))
    print(pow(a, b, m))

if __name__ == "__main__":
    solve()
