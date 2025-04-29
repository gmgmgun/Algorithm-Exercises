import sys

for line in sys.stdin:
    n = int(line.strip())
    a = 1
    length = 1

    while True:
        if a % n == 0:
            print(length)
            break
        a = a * 10 + 1
        length += 1