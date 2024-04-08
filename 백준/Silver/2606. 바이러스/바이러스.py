"""
-------------------------------------------
[접근]
1. 1번 컴퓨터 시작해서 바이러스가 퍼짐
2. 1번 컴퓨터를 루트 노드로 해서 dfs 탐색

[카테고리]
깊이 우선 탐색
스택
-------------------------------------------
"""

import sys

# 노드의 수, 엣지의 수, 엣지 정보
N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
E = [list(map(int, sys.stdin.readline().split())) for i in range(M)]

# 그래프 생성
graph = {i: [] for i in range(1, N + 1)}

for u, v in E:
    graph[u].append(v)
    graph[v].append(u)

visited = [False] * (N + 1)

# dfs 시작
stack = [1]   # 1번 컴퓨터부터 시작하니까 [1]로 할당
count = 0   # 몇대가 감염되었는지 카운팅

# 스택을 비우고 채우고 반복하면서 뎁스 뚫기
while stack:
    node = stack.pop()
    if not visited[node]: 
        visited[node] = True
        count += 1
        for next_node in graph[node]:
            if not visited[next_node]:
                stack.append(next_node)

print(count - 1)


