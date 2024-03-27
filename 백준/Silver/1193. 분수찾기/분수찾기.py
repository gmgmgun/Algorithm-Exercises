n = int(input())

i = 0
while (i * (i + 1)) / 2 < n:
    i += 1

r = i
e = int(r * (r - 1) / 2)
o = n - e

if r % 2 == 0:
    s = o
    m = r - o + 1
else:
    s = r - o + 1
    m = o

print(str(s) + '/' + str(m))