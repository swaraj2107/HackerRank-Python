import math

def solve():
    try:
        ab = float(input())
        bc = float(input())
        res = round(math.degrees(math.atan2(ab, bc)))
        print(f"{res}\u00b0")
        
    except EOFError:
        pass

if __name__ == "__main__":
    solve()
