"""
-------------------------------------------
[접근]
DFS를 사용하여 2차원 그래프 상의 각 영역을 탐색
각 노드에서 인접한 노드로 이동하는 과정을 재귀적으로 구현
2차원 그래프 상에서 연결된 영역(값이 1인 노드들의 그룹)을 찾고, 각 영역의 크기를 계산
dx와 dy 배열을 사용하여 상하좌우 이동을 표현하고, 이를 통해 2차원 공간을 탐색

[카테고리]
깊이 우선 탐색
재귀
그래프
-------------------------------------------
"""

import sys

# 지도 크기, 지도 그래프
N = int(sys.stdin.readline())
graph = [list(map(int, sys.stdin.readline().strip())) for i in range(N)]

# 변위 설정 (우, 상, 좌, 하)
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

# 각 영역 내 노드 수, 현재 탐색 중인 영역 노드 수, 총 영역 수
num = []
count = 0
result = 0

# dfs 탐색
def dfs(x,y):
    if x < 0 or x >= N or y < 0 or y >= N:
        return False

    if graph[x][y] == 1:
        global count
        count += 1
        graph[x][y] = 0  # 현재 노드가 아직 방문하지 않은 노드인 경우, 노드 방문 처리

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(nx, ny)
        return True
    return False

for i in range(N):
    for j in range(N):
        if dfs(i,j) == True:
            num.append(count)
            result += 1
            count = 0

num.sort()

print(result)
print(*num, sep='\n')
