import sys
from collections import deque

def check_stacking():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    iterator = iter(input_data)
    
    t = int(next(iterator))
    
    for _ in range(t):
        n = int(next(iterator))
        
        cubes = deque(int(next(iterator)) for _ in range(n))
        
        last_picked = float('inf')
        possible = True
        
        while cubes:
            left = cubes[0]
            right = cubes[-1]
            
            if left >= right:
                current_pick = cubes.popleft()
            else:
                current_pick = cubes.pop()
                
            if current_pick > last_picked:
                possible = False
                break
                
            last_picked = current_pick
            
        if possible:
            print("Yes")
        else:
            print("No")

if __name__ == "__main__":
    check_stacking()
