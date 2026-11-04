import re
import sys

def solve():
    input_data = sys.stdin.read().splitlines()
    
    if not input_data:
        return

    try:
        t = int(input_data[0])
    except (ValueError, IndexError):
        return

    for i in range(1, t + 1):
        try:
            re.compile(input_data[i])
            print("True")
        except re.error:
            print("False")

if __name__ == "__main__":
    solve()
