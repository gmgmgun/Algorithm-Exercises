import sys
T = int(sys.stdin.readline().strip())


def min_cost():
    for _ in range(T):
        g, c, e = map(int, sys.stdin.readline().split())

        if c >= e:
            print(0)
            continue

        answer = e - c

        if g == 1:
            print(answer)

        if g == 2:
            print(answer * 3)

        if g == 3:
            print(answer * 5)


min_cost()