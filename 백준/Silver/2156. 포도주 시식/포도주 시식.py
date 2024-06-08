import sys
n = int(sys.stdin.readline())
w = [int(sys.stdin.readline().strip()) for _ in range(n)]

def wine():
    d = [0] * n

    d[0] = w[0]

    if n > 1:
        d[1] = w[0] + w[1]

    if n > 2:
        d[2] = max(w[2] + w[1], w[2] + w[0], d[1])

    for i in range(3, n):
        d[i] = max(d[i-1], d[i-2] + w[i], d[i-3] + w[i] + w[i-1])

    return d[n-1]

print(wine())