"""
-------------------------------------------
[접근]
모든 경우 확인 -> 브루트포스 + 백트래킹
그래프가 인접 행렬 형태로 주어짐
방문 확인을 위한 배열 필요함
최소 비용 계산해야 함

[카테고리]
깊이 우선 탐색
-------------------------------------------
"""

import sys

N = int(sys.stdin.readline())
W = [list(map(int, sys.stdin.readline().split())) for i in range(N)]


def tsp(N, W):
    min_cost = float('inf')  # 최소 비용을 최대값으로 설정
    visited = [False] * N

    def backtrack(city, count, cost):
        nonlocal min_cost
        if count == N and W[city][0]:  # 다 방문했는지 + 시작 도시로 돌아갈 수 있는지
            # 최소 비용 업데이트
            min_cost = min(min_cost, cost + W[city][0])
            return
        for i in range(N):
            # 방문 안 했는데 갈 수 있으면
            if not visited[i] and W[city][i]:
                # 방문 처리하고
                visited[i] = True
                # 도시 수 증가시키고 비용도 추가해서 재귀
                backtrack(i, count + 1, cost + W[city][i])
                # 백트래킹 해야하니까 다시 false로 바꿈
                visited[i] = False

    visited[0] = True  # 시작 도시 설정
    backtrack(0, 1, 0)  # 백트래킹 시작함
    return min_cost


print(tsp(N, W)) 

