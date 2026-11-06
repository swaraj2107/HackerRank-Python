from itertools import combinations_with_replacement

def solve():
    input_data = input().split()
    s = input_data[0]
    k = int(input_data[1])
    sorted_s = sorted(s)
    combinations = combinations_with_replacement(sorted_s, k)
    for combo in combinations:
        print("".join(combo))

if __name__ == "__main__":
    solve()
