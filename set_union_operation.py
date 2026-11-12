def solve():
    _ = input() 
    english_set = set(map(int, input().split()))
    
    _ = input()
    french_set = set(map(int, input().split()))
    
    at_least_one = english_set.union(french_set)
    
    print(len(at_least_one))

if __name__ == "__main__":
    solve()
