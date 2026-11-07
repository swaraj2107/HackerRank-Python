from collections import OrderedDict

def solve():
    words_dict = OrderedDict()
    
    try:
        n = int(input())
    except EOFError:
        return

    for _ in range(n):
        word = input().strip()
        if word in words_dict:
            words_dict[word] += 1
        else:
            words_dict[word] = 1
            
    print(len(words_dict))
    
    print(*(words_dict.values()))

if __name__ == "__main__":
    solve()
