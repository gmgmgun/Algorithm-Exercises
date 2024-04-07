"""
-------------------------------------------
[접근 방법]
1. 기둥들을 위치(L)에 따라 정렬
2. 가장 높은 기둥의 인덱스를 찾음
3. 가장 높은 기둥까지 왼쪽과 오른쪽으로부터 각각 면적을 계산
   - 왼쪽 면적: 현재까지 가장 높은 기둥의 높이를 사용하여 각 구간의 면적을 더함
   - 오른쪽 면적: 동일한 방식으로, 오른쪽부터 가장 높은 기둥까지 면적을 계산
4. 가장 높은 기둥의 면적을 추가로 계산
5. 총 면적을 반환

[카테고리]
구현, 그리디 알고리즘
-------------------------------------------
"""

import sys

n = int(sys.stdin.readline())
p = [tuple(map(int, sys.stdin.readline().split())) for i in range(n)]

def smallest_warehouse_area(pillars):
    pillars.sort()

    max_height_index = max(range(len(pillars)), key=lambda i: pillars[i][1])

    area = 0
    current_height = 0

    for i in range(max_height_index):
        if pillars[i][1] > current_height:
            current_height = pillars[i][1]
        area += current_height * (pillars[i + 1][0] - pillars[i][0])

    current_height = 0

    for i in range(len(pillars) - 1, max_height_index, -1):
        if pillars[i][1] > current_height:
            current_height = pillars[i][1]
        area += current_height * (pillars[i][0] - pillars[i - 1][0])

    area += pillars[max_height_index][1]

    return area

print(smallest_warehouse_area(p))