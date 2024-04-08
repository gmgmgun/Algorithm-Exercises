"""
-------------------------------------------
[접근 방법]
1. 무방향 그래프 생성: 노드 수 N과 엣지 정보 E를 이용하여 무방향 그래프를 생성
2. 깊이 우선 탐색(DFS) 준비: 각 노드에 대한 방문 순서를 기록하기 위한 배열을 준비
3. 깊이 우선 탐색(DFS) 실행: 시작 노드 R부터 DFS를 시작
                         각 노드의 인접한 노드들을 오름차순으로 정렬하여 탐색
                         스택을 이용하여 깊이 우선 탐색을 구현
4. 깊이 우선 탐색(DFS) 진행: 각 노드를 방문할 때마다 방문 순서를 기록
5. 방문 순서 출력: 노드 1부터 순서대로 각 노드의 방문 순서를 출력

[카테고리]
그래프 이론
깊이 우선 탐색 (DFS)
-------------------------------------------
"""

import sys

# 노드의 수, 엣지의 수, 시작 노드
N, M, R = map(int, sys.stdin.readline().split())
# 엣지 정보
E = [list(map(int, sys.stdin.readline().split())) for i in range(M)]

# 1번부터 N번까지 노드를 가진 무방향 그래프
graph = {i: [] for i in range(1, N+1)}

# 엣지 정보를 조회하면서 그래프에 방문 기록을 남김
for u, v in E:
    graph[u].append(v)
    graph[v].append(u)

# 각 노드에 대한 인접 리스트를 사전에 정렬
for node in graph:
    graph[node].sort()

# 방문 순서를 넣을 배열
visited = [0] * (N + 1)
counter = 1

def dfs(start):
    stack = [start]
    order = 1

    while stack:
        node = stack.pop()
        if not visited[node]:
            visited[node] = order
            order += 1
            for next_node in reversed(graph[node]):
                if not visited[next_node]:
                    stack.append(next_node)

    return visited[1:]  # 0번 인덱스는 사용하지 않음

dfs(R)

result = visited[1:]

print(*result, sep='\n')