import sys
from collections import deque

M, N = map(int, sys.stdin.readline().split())
S = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

q = deque([])


def bfs(m, n, matrix):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and matrix[nx][ny] == 0:
                matrix[nx][ny] = matrix[x][y] + 1
                q.append((nx, ny))


def tomato(m, n, matrix):
    count = 0

    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 1:
                q.append((i, j))

    bfs(m, n, matrix)

    for row in matrix:
        for val in row:
            if val == 0:
                return -1
            count = max(count, val)

    return count - 1


print(tomato(M, N, S))
