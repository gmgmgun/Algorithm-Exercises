"""
-------------------------------------------
[접근 방법]
1. 나무의 수 n, 목표량 m, 나무들의 높이 w를 입력 받음
2. 목표 길이 m을 만족하거나 초과하는 조건에서, 나무들을 자를 수 있는 최대 높이 h를 찾아야 함
3. 배열을 내림차순으로 정렬한 후, 가장 높은 나무의 높이에서 시작
4. 현재 높이 h에서 나무들을 자른 후의 합이 m 이상이 될 때까지 h를 감소시키며 탐색
5. h를 감소시키면서 나무들을 자르고, 자른 나무의 길이 합이 m 이상인 최초의 h가 답

[카테고리]
이진 탐색, 그리디, 정렬
-------------------------------------------
"""

import sys

n, m = map(int,sys.stdin.readline().split())
w = list(map(int,sys.stdin.readline().split()))

def find_max_height(woods, need):
    low, high = 0, max(woods)  # 가능한 높이의 최소값과 최대값 설정

    while low <= high:
        h = (low + high) // 2  # 중간값으로 절단기 높이 설정
        sum = 0
        for wood in woods:
            if wood > h:  # 나무가 절단기보다 더 길면
                sum += wood - h  # 자르고 남은 부분을 sum에 더함

        if sum >= need:
            low = h + 1  # sum이 목표량 이상 -> 더 높게 잘라봄
        else:
            high = h - 1  # sum이 목표량 이하 -> 더 낮게 잘라봄

    return high  # 최대값을 구하는 거니까 high 반환

print(find_max_height(w, m))
