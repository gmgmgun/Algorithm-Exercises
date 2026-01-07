import sys
from collections import deque
input = sys.stdin.readline

n, m, k = map(int, input().split())
arr = [[1] * m for _ in range(n)]
for _ in range(k):
    x, y = map(int, input().split())
    arr[x - 1][y - 1] = 0  # 쓰레기가 있는 위치를 0으로 표시

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

def count_area(i, j):
    cnt = 1
    q = deque([(i, j)])
    arr[i][j] = 1 

    while q:
        x, y = q.popleft()

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy

            if not in_range(nx, ny): 
                continue
            if arr[nx][ny]:
                continue

            cnt += 1 
            arr[nx][ny] = 1
            q.append((nx, ny))

    return cnt

max_ = 0
for i in range(n):
    for j in range(m):
        if not arr[i][j]: 
            max_ = max(count_area(i, j), max_)

print(max_)