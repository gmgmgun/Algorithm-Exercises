from collections import Counter

w = input()


def find_most_frequent_char(word):
    char_dict = Counter(word.upper())
    max_freq = max(char_dict.values())
    max_char = None
    for char, freq in char_dict.items():
        if freq == max_freq:
            if max_char is not None:
                return "?"
            max_char = char
    return max_char


print(find_most_frequent_char(w))
