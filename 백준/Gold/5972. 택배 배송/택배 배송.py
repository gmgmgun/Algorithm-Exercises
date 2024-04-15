"""
-------------------------------------------
[시간]

[문제 해석]
양방향 그래프
마주치는 소의 숫자 = 비용
1에서 출발해서 N까지 도착하는데 필요한 최소 비용

[접근]
1. 최단 거리 -> 다익스트라로 접근
2. 다익스트라 풀이
    - 그래프 생성
    - 양방향이므로 노드 번갈아서 삽입
    - 최소 비용 배열은 출발 노드를 제외하고 inf 할당
    - 큐에 (시작 비용(0), 출발점(1)) 삽입 후 while문 실행


[카테고리]
그래프, 최단 경로, 다익스트라
-------------------------------------------
"""
import heapq
import sys

N, M = map(int, sys.stdin.readline().split())
G = [tuple(map(int, sys.stdin.readline().split())) for _ in range(M)]


def find_route(n, g):
    inf = float('inf')
    graph = [[] for _ in range(n + 1)]
    visited = [False] * (n + 1)

    for a, b, cow in g:
        graph[a].append([cow, b])
        graph[b].append([cow, a])

    dist = [inf] * (n + 1)
    dist[1] = 0

    pq = []
    heapq.heappush(pq, (dist[1], 1))

    # 다익스트라 구현
    while pq:
        # 큐에서 꺼내서 현재 헛간 가는 길에 소 몇마리 있는지 확인
        cur_cow, cur_shed = heapq.heappop(pq)

        # 가는 길에 마주치는 최소한의 소보다 현재 마주친 소가 더 많으면 되돌아가서 큐에서 꺼냄
        # if cur_cow > dist[cur_shed]:
        #     continue
        if visited[cur_shed]:
            continue
        visited[cur_shed] = True

        # 그래프 탐색
        for cow, shed in graph[cur_shed]:
            new_cow = cur_cow + cow  # 현재 마주친 소에 가는 길에 마주친 소 더함
            if new_cow < dist[shed]:  # 현재 계산값이 최소 비용보다 작으면
                dist[shed] = new_cow  # 최소 비용 업데이트
                heapq.heappush(pq, (new_cow, shed))  # 큐에 다시 밀어넣고 마저 탐색

    return dist[n]


print(find_route(N, G))
