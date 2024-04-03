from collections import deque

n = input()
t = list(map(int, input().split()))


def find_signal(tops):
    deck = deque((i + 1, h) for i, h in enumerate(tops))
    signals = [0] * len(tops)
    stack = []

    while deck:
        top = deck.pop()
        i, h = top

        if not stack:
            stack.append(top)
        elif h > stack[-1][1]:
            while stack:
                if h < stack[-1][1]:
                    break
                s = stack.pop()
                signals[s[0]-1] = i
            stack.append(top)
        else:
            stack.append(top)

    return ' '.join(map(str, signals))


print(find_signal(t))