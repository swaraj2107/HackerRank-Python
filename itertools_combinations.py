from itertools import combinations

S, k = input().split()
k = int(k)
S_sorted = sorted(S)

for i in range(1, k + 1):
    for combo in combinations(S_sorted, i):
        print("".join(combo))
