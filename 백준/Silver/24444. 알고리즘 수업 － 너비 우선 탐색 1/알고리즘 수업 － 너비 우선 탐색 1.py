"""
-------------------------------------------
[접근 방법]
1. 무방향 그래프 생성
    - 노드 수 N과 엣지 정보 E를 사용하여 각 노드에 대한 인접 리스트를 포함하는 무방향 그래프 생성
2. 인접 리스트 정렬
    - 각 노드의 인접 리스트를 오름차순으로 정렬
    - BFS 실행 중 오름차순으로 노드를 방문하기 위함
3. 방문 순서 기록 배열 준비 각 노드의 방문 순서를 기록하기 위한 배열 visited를 준비
    - 각 노드의 방문 순서를 기록하기 위한 배열 visited를 준비
4. 큐를 이용한 BFS 실행
    - 시작 노드 R에서부터 DFS를 시작
    - 큐를 사용하여 DFS 구현
    - 각 노드를 방문할 때마다 방문 순서를 visited 배열에 기록
5. 방문 순서 출력
    - 노드 1부터 시작하여 각 노드의 방문 순서를 출력
    - 방문하지 않은 노드의 경우 순서가 0으로 표시

[카테고리]
그래프 이론
너비 우선 탐색 (BFS)
큐
-------------------------------------------
"""

import sys
from collections import deque

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

def bfs(start):
    visited_order = [0] * (len(graph) + 1)
    # 큐에 시작 노드 할당 -> 이 노드부터 탐색
    queue = deque([start])
    order = 1
    visited_order[start] = order

    while queue:
        # 큐 앞에서 노드를 빼서
        node = queue.popleft()
        # 노드의 인접 노드를 탐색
        for next_node in sorted(graph[node]):
            # 인접 노드가 방문 기록이 없다면
            if visited_order[next_node] == 0:
                # 방문 순서 + 1
                order += 1
                # 해당 노드에 해당하는 방문 기록 배열에 순서 할당
                visited_order[next_node] = order
                # 큐가 비었으니까 다음 노드의 인접 노드 탐색을 위해 큐에 밀어넣음
                queue.append(next_node)

    return visited_order[1:]  # 0번 인덱스는 사용하지 않음

result = bfs(R)

print(*result, sep='\n')