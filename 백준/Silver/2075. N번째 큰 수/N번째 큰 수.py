"""
-------------------------------------------
[접근 방법]
1. N과 N x N 행렬의 값을 사용자로부터 입력받음
2. 각 행렬의 원소를 순회하면서 힙에 삽입
3. 힙의 크기가 N을 초과할 경우, 가장 작은 원소를 제거
   이렇게 하면 힙에는 항상 N개의 가장 큰 원소만 남게 됨
4. 힙의 루트에 위치한 원소, 즉 N번째로 큰 수를 반환

[카테고리]
힙, 정렬
-------------------------------------------
"""

import heapq

N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]


def nth_largest_number(n, numbers):
    heap = []
    for row in numbers:
        for num in row:
            heapq.heappush(heap, num)
            if len(heap) > n:
                heapq.heappop(heap)
    return heap[0]


print(nth_largest_number(N, matrix))