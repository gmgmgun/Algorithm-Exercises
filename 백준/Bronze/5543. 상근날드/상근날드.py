import sys
b = [int(sys.stdin.readline().strip()) for _ in range(3)]
s = [int(sys.stdin.readline().strip()) for _ in range(2)]


def min_cost():
    return min(b) + min(s) - 50


print(min_cost())