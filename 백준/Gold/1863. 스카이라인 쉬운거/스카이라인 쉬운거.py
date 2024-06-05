import sys
N = int(sys.stdin.readline())


def skyline():
    stack = []
    count = 0

    for _ in range(N):
        _, y = map(int, sys.stdin.readline().split())

        while stack and stack[-1] > y:
            stack.pop()
            count += 1

        if (not stack or stack[-1] < y) and y > 0:
            stack.append(y)

    count += len(stack)

    return count


print(skyline())
