cnt = int(input())

for _ in range(cnt):
    n, s = input().split()
    n = int(n)
    for char in s:
        print(char * n, end='')
    print()