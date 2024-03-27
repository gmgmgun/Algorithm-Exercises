cnt = int(input())
l = []

for i in range(cnt):
    s = '*' * (i + 1) + ' ' * (2 * (cnt - (i + 1))) + '*' * (i + 1)
    l.append(s)
    print(s)

l.pop()
for s in reversed(l):
    print(s)