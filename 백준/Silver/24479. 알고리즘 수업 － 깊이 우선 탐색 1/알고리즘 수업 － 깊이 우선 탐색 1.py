"""
-------------------------------------------
[접근 방법]
1. 무방향 그래프 생성
    - 노드 수 N과 엣지 정보 E를 사용하여 각 노드에 대한 인접 리스트를 포함하는 무방향 그래프 생성
2. 인접 리스트 정렬
    - 각 노드의 인접 리스트를 오름차순으로 정렬
    - DFS 실행 중 오름차순으로 노드를 방문하기 위함
3. 방문 순서 기록 배열 준비 각 노드의 방문 순서를 기록하기 위한 배열 visited를 준비
    - 각 노드의 방문 순서를 기록하기 위한 배열 visited를 준비
4. 스택을 이용한 DFS 실행
    - 시작 노드 R에서부터 DFS를 시작
    - 스택을 사용하여 DFS 구현
    - 각 노드를 방문할 때마다 방문 순서를 visited 배열에 기록
5. 방문 순서 출력
    - 노드 1부터 시작하여 각 노드의 방문 순서를 출력
    - 방문하지 않은 노드의 경우 순서가 0으로 표시

[카테고리]
그래프 이론
깊이 우선 탐색 (DFS)
스택
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
            for next_node in reversed(graph[node]):  # 스택이니까 역순으로 정렬해야 작은 숫자부터 확인
                if not visited[next_node]:
                    stack.append(next_node)

    return visited[1:]  # 0번 인덱스는 사용하지 않음

dfs(R)

result = visited[1:]

print(*result, sep='\n')