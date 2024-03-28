from collections import Counter

w = input()

def find_most_frequent_char(word):
    char_dict = Counter(word.upper())
    max_freq = max(char_dict.values())
    max_chars = [char for char, freq in char_dict.items() if freq == max_freq]
    return max_chars[0] if len(max_chars) == 1 else "?"

print(find_most_frequent_char(w))
