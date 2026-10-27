from collections import OrderedDict

item_inventory = OrderedDict()
n = int(input())

for _ in range(n):
    data = input().rpartition(' ')
    item_name = data[0]
    net_price = int(data[2])

    if item_name in item_inventory:
        item_inventory[item_name] += net_price
    else:
        item_inventory[item_name] = net_price

for item, total_price in item_inventory.items():
    print(f"{item} {total_price}")
