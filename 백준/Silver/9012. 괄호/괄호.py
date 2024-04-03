n = int(input())
a = [input() for _ in range(n)]


def is_vps(string):
    if len(string) % 2 != 0:
        return 'NO'
    
    count = 0

    for char in string:
        if char == '(':
            count += 1
        elif char == ')':
            if count == 0:
                return 'NO'
            count -= 1

    return 'YES' if count == 0 else 'NO'


def find_vps(arr):
    for s in arr:
        answer = is_vps(s)
        print(answer)


find_vps(a)
