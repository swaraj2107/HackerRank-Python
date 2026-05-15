from itertools import permutations

S, r = input().split()
r = int(r)

res = list(permutations(sorted(S), r))

for p in res:
    print("".join(p))
