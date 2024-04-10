"""
-------------------------------------------
[접근 방법]
경우의 수 찾는 문제 -> 브루트포스 -> dfs


[카테고리]
깊이 우선 탐색
-------------------------------------------
"""

import sys

N, S = map(int, sys.stdin.readline().split())
M = list(map(int, sys.stdin.readline().split()))


def sum_sub(arr, num, goal):

    def dfs(index, cur):
        if index == num:    # 배열 마지막까지 왔을 때 탈출 조건
            return 1 if cur == goal else 0    # 현재 합 = goal이면 1 아니면 0 리턴

        count = dfs(index + 1, cur + arr[index])

        count += dfs(index + 1, cur)

        return count

    return dfs(0, 0) - (1 if goal == 0 else 0)  # 0이면 빈 문자열 빼줘야 함


print(sum_sub(M, N, S))

