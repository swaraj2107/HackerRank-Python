from itertools import groupby

s = input().strip()
print(*(f"({len(list(g))}, {int(k)})" for k, g in groupby(s)))
