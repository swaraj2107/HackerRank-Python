import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return   
    a = int(input_data[0])
    b = int(input_data[1])
    print(a // b)
    print(a % b)
    print(divmod(a, b))

if __name__ == "__main__":
    solve()
