import sys
import math

def solve():
    input_data = sys.stdin.read().splitlines()
    if not input_data:
        return

    n = int(input_data[0].strip())
    letters = input_data[1].strip().split()
    k = int(input_data[2].strip())

    not_a_count = sum(1 for letter in letters if letter != 'a')
    total_combinations = math.comb(n, k)
    no_a_combinations = math.comb(not_a_count, k)
    prob_no_a = no_a_combinations / total_combinations
    prob_at_least_one_a = 1 - prob_no_a

    print(f"{prob_at_least_one_a:.4f}")

if __name__ == "__main__":
    solve()
