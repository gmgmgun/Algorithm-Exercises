import sys
import heapq


def sum_files(files):
    heapq.heapify(files)
    total = 0

    while len(files) > 1:
        cost = heapq.heappop(files) + heapq.heappop(files)
        total += cost
        heapq.heappush(files, cost)

    return total

N = int(sys.stdin.readline().strip())
for _ in range(N):
    K = int(sys.stdin.readline().strip())
    fs = list(map(int, sys.stdin.readline().strip().split()))
    result = sum_files(fs)
    print(result)
