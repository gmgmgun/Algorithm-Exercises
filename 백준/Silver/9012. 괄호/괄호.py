n = int(input())
a = [input() for _ in range(n)]


def is_vps(string):
    if len(string) % 2 != 0:
        return 'NO'

    stack = []

    for char in string:
        if char == '(':
            stack.append(char)
        else:
            if not stack:
                return 'NO'
            stack.pop()

    if stack:
        return 'NO'

    return 'YES'


def find_vps(arr):
    for s in arr:
        answer = is_vps(s)
        print(answer)


find_vps(a)
