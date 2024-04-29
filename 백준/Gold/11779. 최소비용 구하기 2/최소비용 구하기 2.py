import sys
import heapq

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
L = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]
S, E = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(N + 1)]

for current, destination, cost in L:
    graph[current].append((destination, cost))

INF = float('inf')
dist = [INF] * (N + 1)
path = [-1] * (N + 1)
dist[S] = 0
heap = [(0, S)]

while heap:
    current_cost, u = heapq.heappop(heap)

    if current_cost > dist[u]:
        continue

    for v, weight in graph[u]:
        new_cost = current_cost + weight
        if new_cost < dist[v]:
            dist[v] = new_cost
            path[v] = u
            heapq.heappush(heap, (new_cost, v))

route = []
current = E
while current != -1:
    route.append(current)
    current = path[current]
route.reverse()

print(dist[E])
print(len(route))
print(' '.join(map(str, route)))
