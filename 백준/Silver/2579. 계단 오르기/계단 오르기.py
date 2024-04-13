"""
-------------------------------------------
[시간]


[문제 해석]
1칸 또는 2칸씩 계단 오르기
3연속으로 1칸씩은 못 감
마지막 계단은 무조건 밟아야 함
계단마다 점수가 쓰여져 있음
얻을 수 있는 점수의 최댓값은?

[접근]
1. 이동하는 방법 2가지(1칸, 2칸) -> DP로 접근
2. DP로 풀이
3. 점화식 구하기(마지막 계단에 도달하는 경우의 수)
    - i = 마지막 계단 인덱스, scores[i] = 마지막 계단 점수
    - dp[i] = 마지막 계단에 도착했을 때 최대 점수
    - dp[i-1]에서 dp[i]로 가는 경우 (1칸 이동)
        i-2 칸은 밟으면 안됨 (i-2, i-1, i 다 밟으면 규칙 위반)
        따라서 dp[i] = dp[i-3] + scores[i] + scores[i-2]
    - dp[i-2]에서 dp[i]로 가는 경우 (2칸 이동)
        따라서 dp[i] = dp[i-2] + scores[i]
    - 따라서 점화식은 dp[i] = max((dp[i-3] + scores[i-1] + scores[i]), (dp[i-2] + scores[i]))

[카테고리]
동적 계획법(DP)
-------------------------------------------
"""

import sys

N = int(sys.stdin.readline())
S = list(int(sys.stdin.readline()) for _ in range(N))


def find_max_score(n, scores):
    if n == 0:  # 0도 자연수
        return 0
    elif n == 1:
        return scores[0]
    elif n == 2:  # 계단이 2개일 경우 1칸 이동 2번의 기대값이 2칸 이동 1번보다 항상 큼
        return scores[0] + scores[1]

    dp = [0] * n
    dp[0] = scores[0]  # 1칸 이동
    dp[1] = scores[0] + scores[1]  # 1칸 이동 2번
    dp[2] = max(scores[0] + scores[2], scores[1] + scores[2])  # 1칸 + 2칸 이동 또는 2칸 + 1칸 이동

    for i in range(3, n):
        # 1칸 이동해서 마지막 계단 도착 vs 2칸 이동해서 마지막 계단 도착
        dp[i] = max((dp[i-3] + scores[i-1] + scores[i]), (dp[i-2] + scores[i]))

    return dp[n-1]


print(find_max_score(N, S))
