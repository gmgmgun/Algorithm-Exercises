T = int(input())
cases = []

for _ in range(T):
    n = int(input())
    r1 = list(map(int, input().split()))
    r2 = list(map(int, input().split()))
    cases.append([n, r1, r2])


def max_score(n, row1, row2):
    if n == 1:
        return max(row1[0], row2[0])

    dp = [[0] * 2 for _ in range(n)]

    dp[0][0] = row1[0]
    dp[0][1] = row2[0]

    if n > 1:
        dp[1][0] = max(row2[0] + row1[1], row1[1])
        dp[1][1] = max(row1[0] + row2[1], row2[1])

    for i in range(2, n):
        dp[i][0] = max(dp[i - 1][1], dp[i - 2][0], dp[i - 2][1]) + row1[i]
        dp[i][1] = max(dp[i - 1][0], dp[i - 2][0], dp[i - 2][1]) + row2[i]

    return max(dp[n - 1][0], dp[n - 1][1])


for case in cases:
    n, r1, r2 = case
    result = max_score(n, r1, r2)
    print(result)