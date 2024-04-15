"""
-------------------------------------------
[시간]

[문제 해석]

[접근]



[카테고리]
-------------------------------------------
"""
import heapq
import sys

N, M = map(int, sys.stdin.readline().split())
G = [tuple(map(int, sys.stdin.readline().split())) for _ in range(M)]


def find_route(n, m, g):
    inf = float('inf')

    graph = [[] for _ in range(n + 1)]

    for a, b, cow in g:
        graph[a].append([cow, b])
        graph[b].append([cow, a])

    dist = [inf] * (n + 1)
    dist[1] = 0

    pq = []
    heapq.heappush(pq, (dist[1], 1))

    # 다익스트라 구현
    while pq:
        cur_cow, cur_shed = heapq.heappop(pq)

        if cur_cow > dist[cur_shed]:
            continue

        for cow, shed in graph[cur_shed]:
            new_cow = cur_cow + cow
            if new_cow < dist[shed]:
                dist[shed] = new_cow
                heapq.heappush(pq, (new_cow, shed))

    return dist[n]


print(find_route(N, M, G))
