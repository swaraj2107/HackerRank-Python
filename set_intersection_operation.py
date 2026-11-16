def solve():
    _ = input() 
    english_set = set(map(int, input().split()))
    
    _ = input()
    french_set = set(map(int, input().split()))
    
    both_subscriptions = english_set.intersection(french_set)
    
    print(len(both_subscriptions))

if __name__ == "__main__":
    solve()
