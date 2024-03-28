cnt = int(input())
fruit_dict = {}

for _ in range(cnt):
    f, n = input().split()
    n = int(n)
    if f in fruit_dict:
        fruit_dict[f] += n
    else:
        fruit_dict[f] = n


def should_ring_bell(f_dict):
    for fruit, quantity in f_dict.items():
        if quantity == 5:
            return "YES"
    return "NO"


print(should_ring_bell(fruit_dict))