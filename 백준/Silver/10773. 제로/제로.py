import sys

input = sys.stdin.read().strip().split('\n')

count = int(input[0])
arr = []

for i in range(1, count + 1):
    el = int(input[i])

    if el:
        arr.append(el)
    else:
        arr.pop()

result = sum(arr)
print(result)