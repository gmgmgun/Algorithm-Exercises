"""
-------------------------------------------
[접근 방법]
1. 현재 승률을 계산
2. 이진 탐색을 이용하여 승률이 변경되는 지점 찾기
3. 최소한의 게임 수를 찾기 위해, 현재 승률보다 높아지는 지점 찾기
4. 승률이 99% 이상일 경우 변경 불가능하므로 -1 반환
5. 승률을 바꾸기 위해 필요한 추가 게임 횟수를 반환

[카테고리]
이진 탐색
-------------------------------------------
"""

import sys

x, y = map(int, sys.stdin.readline().split())

def min_games_to_change_win_rate(X, Y):
    current_rate = int(100 * Y / X)

    if current_rate >= 99:
        return -1

    left, right = 0, X
    while left <= right:
        mid = (left + right) // 2
        new_rate = int(100 * (Y + mid) / (X + mid))
        if new_rate > current_rate:
            right = mid - 1
        else:
            left = mid + 1

    return left

print(min_games_to_change_win_rate(x,y))
