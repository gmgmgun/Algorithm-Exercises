S = input()


def find_uniq_substr(string):
    uniq_substr = set()

    for start_idx in range(len(string)):
        for end_idx in range(start_idx + 1, len(string) + 1):
            uniq_substr.add(string[start_idx:end_idx])

    return len(uniq_substr)


print(find_uniq_substr(S))
