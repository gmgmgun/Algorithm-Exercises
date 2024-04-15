"""
-------------------------------------------
[시간]

[문제 해석]
시작점부터 일직선 노드를 따라 끝까지 이동
노드 사이의 길이도 다르고, 노드마다 주유소가 있는데 가격이 다름
도로의 길이와 기름 가격을 입력 받았을 때, 끝->끝으로 가는 최소 비용을 구해라

[접근]

[카테고리]
그리디
-------------------------------------------
"""

import sys

N = int(sys.stdin.readline())
C = list(map(int, sys.stdin.readline().split()))
O = list(map(int, sys.stdin.readline().split()))


def find_min_cost(n, c, o):
    min_cost = 0
    current_min_price = o[0]

    for i in range(n - 1):
        if o[i] < current_min_price:
            current_min_price = o[i]
        min_cost += current_min_price * c[i]

    return min_cost


print(find_min_cost(N, C, O))
