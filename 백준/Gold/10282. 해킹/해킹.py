import sys
import heapq

T = int(sys.stdin.readline())
cases = []
for i in range(T):
    N, D, C = map(int, sys.stdin.readline().split())
    arr = [tuple(map(int, sys.stdin.readline().split())) for _ in range(D)]
    cases.append([N, C, arr])


def find_infect_time(n, com, depend):
    graph = [[] for _ in range(n + 1)]

    for a, b, s in depend:
        graph[b].append((a, s))

    inf = float('inf')
    min_time = [inf] * (n + 1)
    min_time[com] = 0
    pq = [(0, com)]

    while pq:
        cur_time, cur_com = heapq.heappop(pq)

        if cur_time > min_time[cur_com]:
            continue

        for next, time in graph[cur_com]:
            infect_time = cur_time + time
            if infect_time < min_time[next]:
                min_time[next] = infect_time
                heapq.heappush(pq, (infect_time, next))

    count = 0
    last_infect_time = 0

    for time in min_time:
        if time < inf:
            count += 1
            if time > last_infect_time:
                last_infect_time = time

    return count, last_infect_time


for case in cases:
    N, C, arr = case
    result = find_infect_time(N, C, arr)
    print(*result)


