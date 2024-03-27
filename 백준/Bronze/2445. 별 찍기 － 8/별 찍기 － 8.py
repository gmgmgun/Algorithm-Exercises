cnt = int(input())
l = []

for i in range(cnt):
    s = '*' * (i + 1) + ' ' * (2 * (cnt - (i + 1))) + '*' * (i + 1)
    if i != cnt - 1:
        l.append(s)
    print(s)

for s in reversed(l):
    print(s)