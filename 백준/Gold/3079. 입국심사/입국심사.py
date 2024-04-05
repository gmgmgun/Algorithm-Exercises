"""
-------------------------------------------
**지선생님 찬스 사용**
[접근 방법]
1. 심사대의 수 n과 입국심사를 받아야 할 사람의 수 m, 각 심사대별 심사 시간 t를 입력 받음
2. 모든 사람이 심사를 받는 데 걸리는 시간의 최솟값을 찾아야 함
3. 이를 위해 이분 탐색을 사용. 최소 시간을 1, 최대 시간을 가장 긴 심사 시간과 입국자 수의 곱으로 설정
4. 중간값(mid_time)을 구하고, 해당 시간 안에 심사 가능한 인원 수를 계산
5. 계산된 인원 수가 입국자 수(m)보다 적으면 최소 시간(min_time)을 중간값 이후로 조정
6. 계산된 인원 수가 입국자 수(m)와 같거나 많으면 최대 시간(max_time)을 중간값 이전으로 조정
7. 이분 탐색을 통해 최소 입국심사 시간을 찾음

[카테고리]
이분 탐색, 시뮬레이션
-------------------------------------------
"""

import sys

n, m = map(int, sys.stdin.readline().split())
t = [int(sys.stdin.readline().strip()) for i in range(n)]

def immigration(M, times):
    min_time, max_time = 1, max(times) * M

    while min_time <= max_time:
        mid_time = (min_time + max_time) // 2
        people = sum(mid_time // time for time in times)

        if people >= M:
            max_time = mid_time - 1
        else:
            min_time = mid_time + 1

    return min_time

print(immigration(m, t))

