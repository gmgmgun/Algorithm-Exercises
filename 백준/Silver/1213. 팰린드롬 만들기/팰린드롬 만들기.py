from collections import Counter

s = input()


def make_raw_door(name):
    name = list(name)
    letter_cnt = Counter(name)
    odd_count = sum(1 for char, count in letter_cnt.items() if count % 2 != 0)

    if odd_count > 1:
        return "I'm Sorry Hansoo"

    mid = [char for char, count in letter_cnt.items() if count % 2 != 0]
    half = sorted(char * (count // 2) for char, count in letter_cnt.items())

    raw_door = ''.join(half + mid + half[::-1])

    return raw_door


print(make_raw_door(s))