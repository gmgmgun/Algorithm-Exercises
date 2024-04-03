from collections import deque

n = int(input())
t = [[input().split(), list(map(int, input().split()))]for _ in range(n)]


def find_order(case):
    num, focus = map(int, case[0])
    q = case[1]

    deck = deque((i, p) for i, p in enumerate(q))
    order = 0

    while deck:
        doc = deck.popleft()
        if any(doc[1] < x[1] for x in deck):
            deck.append(doc)
        else:
            order += 1
            if doc[0] == focus:
                return order


def printer_queue(cases):
    for case in cases:
        print(find_order(case))


printer_queue(t)
