"""
-------------------------------------------
[접근 방법]
1. 산술평균을 계산하기 위해 주어진 수들의 합을 수의 개수로 나눔
2. 중앙값을 구하기 위해 수들을 정렬한 후 중간값을 찾음
3. 최빈값을 찾기 위해 각 숫자의 빈도를 계산하고, 가장 높은 빈도를 가진 숫자를 선택
   만약 최빈값이 여러 개 있는 경우, 두 번째로 작은 값을 선택
4. 범위를 구하기 위해 수들 중 최댓값과 최솟값의 차이를 계산

[카테고리]
통계 계산
-------------------------------------------
"""

from collections import Counter
import statistics
import sys

n = int(sys.stdin.readline())
nums = [int(sys.stdin.readline()) for i in range(n)]

def basic_statistics(numbers):

    mean = round(sum(numbers) / len(numbers))

    median = statistics.median(numbers)

    frequency = Counter(numbers)
    most_common = frequency.most_common()
    most_common.sort(key=lambda x: (-x[1], x[0]))
    mode = most_common[0][0]

    if len(most_common) > 1 and most_common[0][1] == most_common[1][1]:
        mode = most_common[1][0]

    range_value = max(numbers) - min(numbers)

    print(mean)
    print(median)
    print(mode)
    print(range_value)

basic_statistics(nums)
