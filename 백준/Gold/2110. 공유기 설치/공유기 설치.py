"""
-------------------------------------------
[접근 방법]
1. 집의 위치를 정렬
2. 최소 거리(min_gap)를 1, 최대 거리(max_gap)를 가장 먼 두 집의 거리로 설정
3. 이진 탐색 수행, 현재 거리(mid)로 공유기를 c개 설치할 수 있는지 확인
4. 설치 가능 -> 거리를 늘려 더 큰 값을 탐색
5. 설치 불가능 -> 거리를 줄여 계속 탐색

[카테고리]
이진 탐색
-------------------------------------------
"""

import sys

n, c = map(int, sys.stdin.readline().split())
h = [int(sys.stdin.readline().strip()) for i in range(n)]

def install_routers(houses, distance, ctrl):
    count = 1
    last_installed = houses[0]

    for i in range(1, len(houses)):
        if houses[i] - last_installed >= distance:
            count += 1
            last_installed = houses[i]
            if count >= ctrl:
                return True

    return False

def find_max_distance(houses, ctrl):
    houses.sort()
    min_gap = 1
    max_gap = houses[-1] - houses[0]
    result = 0

    while min_gap <= max_gap:
        mid = (min_gap + max_gap) // 2
        if install_routers(houses, mid, ctrl):
            result = mid
            min_gap = mid + 1
        else:
            max_gap = mid - 1

    return result

print(find_max_distance(h, c))
