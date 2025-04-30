import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())
deq = deque(range(1, n + 1))
res = []

while deq:
    for _ in range(k - 1):
        deq.append(deq.popleft())
    res.append(str(deq.popleft()))

print(f"<{', '.join(res)}>")