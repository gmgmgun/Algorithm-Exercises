l = input().split()

def find_largest_reversed(num_list):
    max_val = 0
    for num in num_list:
        reversed_num = int(num[::-1])
        if reversed_num > max_val:
            max_val = reversed_num
    return max_val

print(find_largest_reversed(l))