def minion_game(string):
    vowels = 'AEIOU'
    kevin_score = 0
    stuart_score = 0
    length = len(string)

    # Calculate scores for Kevin and Stuart
    for i in range(length):
        if string[i] in vowels:
            kevin_score += length - i  # All substrings starting with this vowel
        else:
            stuart_score += length - i  # All substrings starting with this consonant

    # Determine the winner or if it's a draw
    if kevin_score > stuart_score:
        print(f"Kevin {kevin_score}")
    elif stuart_score > kevin_score:
        print(f"Stuart {stuart_score}")
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)
