def solve():
    try:
        t = int(input())
    except EOFError:
        return

    for _ in range(t):
        try:
            a, b = input().split()
            result = int(a) // int(b)
            print(result)
            
        except ZeroDivisionError as e:
            print("Error Code:", e)
            
        except ValueError as e:
            print("Error Code:", e)

if __name__ == "__main__":
    solve()
