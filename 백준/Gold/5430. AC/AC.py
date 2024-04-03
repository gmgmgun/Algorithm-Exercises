from collections import deque

T = int(input())
for tc in range(T):
    query = input()
    k = int(input())
    q = deque(input()[1:-1].split(','))
    flag = 0

    if k == 0:
        q = []

    for c in query:
        if c == 'R':
            flag += 1
        elif c == 'D':
            if len(q) == 0:
                print('error')
                break
            else:
                if flag % 2 == 1:
                    q.pop()
                else:
                    q.popleft()

    else:
        if flag % 2 == 1:
            q.reverse()
        print('[' + ','.join(q) + ']')