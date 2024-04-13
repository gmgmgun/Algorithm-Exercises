"""
-------------------------------------------
[시간]

[문제 해석]
n이 주어졌을 때, n번째 피보나치 수 구하기

[접근]
1. 피보나치 수 -> DP로 접근
2. 점화식 구하기
    f(0) = 0
    f(1) = 1
    f(2) = 1
    f(3) = 2
    ...
    f(n) = f(n-1) + f(n-2)
3. 반복문 돌리면서 점화식 수행
4. 점화식 결과를 저장할 때, 배열 대신 변수를 사용해 공간 복잡도 최적화

[카테고리]
동적 계획법(DP)
-------------------------------------------
"""

import sys

N = int(sys.stdin.readline())


def find_nth_fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    prev2, prev1 = 0, 1  # dp[0] = 0, dp[1] = 1
    
    for i in range(2, n + 1):
        cur = prev1 + prev2  # dp[i] = dp[i-1] + dp[i-2]
        prev2 = prev1
        prev1 = cur
        
    return prev1  # 반복문 마지막 회차에 prev1에 cur 할당


print(find_nth_fibonacci(N))
