import sys
from collections import deque

N = int(sys.stdin.readline())
M = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]


def bfs(start, grid, n, shark_size):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = deque([start])
    visited = [[False] * n for _ in range(n)]
    visited[start[0]][start[1]] = True
    min_dist = float('inf')
    eatable_fish = []

    distance = 0
    while queue:
        size = len(queue)
        distance += 1
        for _ in range(size):
            x, y = queue.popleft()
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                    if grid[nx][ny] <= shark_size:
                        visited[nx][ny] = True
                        if 0 < grid[nx][ny] < shark_size:
                            if distance < min_dist:
                                min_dist = distance
                                eatable_fish = [(nx, ny)]
                            elif distance == min_dist:
                                eatable_fish.append((nx, ny))
                        queue.append((nx, ny))
    if eatable_fish:
        eatable_fish.sort()
        return eatable_fish[0], min_dist
    return None, 0


def baby_shark(N, grid):
    shark_size = 2
    eat_count = 0
    time_spent = 0

    # 아기 상어 위치 찾기
    shark_pos = None
    for i in range(N):
        for j in range(N):
            if grid[i][j] == 9:
                shark_pos = (i, j)
                grid[i][j] = 0
                break
        if shark_pos:
            break

    while True:
        fish, time_to_fish = bfs(shark_pos, grid, N, shark_size)
        if fish is None:
            break

        x, y = fish
        grid[x][y] = 0
        time_spent += time_to_fish
        eat_count += 1
        if eat_count == shark_size:
            shark_size += 1
            eat_count = 0
        shark_pos = (x, y)

    return time_spent


print(baby_shark(N, M))