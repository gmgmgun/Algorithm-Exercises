"""
-------------------------------------------
[시간]

[문제 해석]
수열 A가 주어졌을 때,
가장 긴 감소하는 부분 수열의 길이를 구해라

[접근]
1. 전체에서 부분 찾기 -> DP로 접근
2. 점화식 도출
    dp[i]가 가장 긴 감소하는 부분 수열의 길이일 때,

[카테고리]
셋
-------------------------------------------
"""

import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))


def find_dec_sub(arr):
    dp = [1] * N  # 각 인덱스별로 최소한 자기 자신만을 가진 부분 수열의 길이를 저장할 배열

    for i in range(1, N):
        for j in range(i):
            if arr[j] > arr[i]:  # 현재 값이 이전 값보다 작을 때만 증가하는 부분 수열의 길이를 업데이트
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)  # dp 배열 중 가장 큰 값이 가장 긴 감소하는 부분 수열의 길이


print(find_dec_sub(A))