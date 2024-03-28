l = input().split()


def find_largest_reversed(num_list):
    reversed_list = [int(num[::-1]) for num in num_list]
    return max(reversed_list)


print(find_largest_reversed(l))