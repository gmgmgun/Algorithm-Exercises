import sys

N = int(sys.stdin.readline())
K = int(sys.stdin.readline())
S = list(map(int, sys.stdin.readline().split()))


def max_score(n, k, sens):
    if k >= n:
        return 0

    sens.sort()
    intervals = [(sens[i] - sens[i-1]) for i in range(1, n)]
    intervals.sort(reverse=True)

    min_sum = sens[-1] - sens[0]

    for i in range(k - 1):
        min_sum -= intervals[i]

    return min_sum


print(max_score(N, K, S))
