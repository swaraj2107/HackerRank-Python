from collections import Counter

num_shoes = int(input())
inventory = Counter(map(int, input().split()))
num_customers = int(input())
total_revenue = 0

for _ in range(num_customers):
    size, price = map(int, input().split())
    
    if inventory[size] > 0:
        total_revenue += price
        inventory[size] -= 1

print(total_revenue)
