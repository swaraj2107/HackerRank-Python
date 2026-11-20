def solve():
    _ = input()
    english_set = set(map(int, input().split()))
    
    _ = input()
    french_set = set(map(int, input().split()))
    
    english_only = english_set.difference(french_set)
    
    print(len(english_only))

if __name__ == "__main__":
    solve()
