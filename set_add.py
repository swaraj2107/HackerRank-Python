n = int(input())
country_stamps = set()

for _ in range(n):
    country_name = input()
    country_stamps.add(country_name)

print(len(country_stamps))
