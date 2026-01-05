from sys import stdin

coin = []
count = 0

N, M = map(int,stdin.readline().split())

for i in range(N):
    coin.append(int(stdin.readline()))

coin.sort(reverse=True)

for value in coin:
    count = count + (M//value)
    M = M % value
    if(M <=0):
        break

print(count)