def solve():
    _ = input() 
    set_a = set(map(int, input().split()))
    
    _ = input()
    set_b = set(map(int, input().split()))
    
    sym_diff = set_a.symmetric_difference(set_b)
    sorted_diff = sorted(list(sym_diff))
    
    for val in sorted_diff:
        print(val)

if __name__ == "__main__":
    solve()
