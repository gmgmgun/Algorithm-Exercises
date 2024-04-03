from collections import deque

n = input()
a = list(map(int, input().split()))


def pop_balloons(balloons):
    pop_order = []
    deck = deque((i + 1, m) for i, m in enumerate(balloons))

    while deck:
        index, move = deck.popleft()
        pop_order.append(index)

        if move > 0:
            move -= 1
        
        deck.rotate(-move)

    return ' '.join(map(str, pop_order))


print(pop_balloons(a))
