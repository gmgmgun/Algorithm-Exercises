import sys
from collections import deque
T = int(sys.stdin.readline())


def bfs(grid, x, y, M, N):
    queue = deque([(x, y)])
    while queue:
        cx, cy = queue.popleft()
        if 0 <= cx < M and 0 <= cy < N and grid[cx][cy] == 1:
            grid[cx][cy] = 0  # 방문 처리
            queue.append((cx + 1, cy))
            queue.append((cx - 1, cy))
            queue.append((cx, cy + 1))
            queue.append((cx, cy - 1))


def count_worms(grid, M, N):
    worms = 0
    for i in range(M):
        for j in range(N):
            if grid[i][j] == 1:
                bfs(grid, i, j, M, N)
                worms += 1
    return worms


results = []
for _ in range(T):
    M, N, K = map(int, sys.stdin.readline().split())
    grid = [[0] * N for _ in range(M)]
    for _ in range(K):
        x, y = map(int, input().split())
        grid[x][y] = 1

    worms = count_worms(grid, M, N)
    results.append(worms)

for result in results:
    print(result)

