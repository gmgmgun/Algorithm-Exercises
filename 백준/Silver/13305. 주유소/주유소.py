"""
-------------------------------------------
[시간]

[문제 해석]
시작점부터 일직선 노드를 따라 끝까지 이동
노드 사이의 길이도 다르고, 노드마다 주유소가 있는데 가격이 다름
도로의 길이와 기름 가격을 입력 받았을 때, 끝->끝으로 가는 최소 비용을 구해라

[접근]
1. 최소 비용 = 최대 이득 구하는 거니까 그리디로 접근
2. 일단 전체 거리만큼 만땅으로 채우고 주유소 도착할 때마다 가격 비교해서 비용을 업데이트를 해주자

[카테고리]
그리디
-------------------------------------------
"""

import sys

N = int(sys.stdin.readline())
C = list(map(int, sys.stdin.readline().split()))
O = list(map(int, sys.stdin.readline().split()))


def find_min_cost(n, c, o):
    cur_distance = sum(c)
    cur_cost = o[0] * cur_distance

    for i in range(1,n):
        cur_distance -= c[i-1]
        if o[i] < o[i-1]:
            cur_cost = cur_cost + (o[i] - o[i-1]) * cur_distance

    return cur_cost


print(find_min_cost(N, C, O))
