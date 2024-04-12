"""
-------------------------------------------
[접근]
1. 회의실을 사용할 수 있는 최대 개수를 구해야 함.
    - 최대로 많이 회의를 예약할 수 있는 기준점을 세워서 정렬하자.
    - 시작시간 빠른 순? 종료시간이 지나치게 늦는다면 다른 회의를 못 잡음.
    - 반대로 종료시간이 빠른 순으로 정렬한다면, 매 시도마다 가장 많은 경우의 수를 고려할 수 있음.

[카테고리]
그리디
-------------------------------------------
"""

import sys

N = int(sys.stdin.readline())
M = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]


def find_max_meetings(schedules):
    schedules.sort(key=lambda x: (x[1], x[0]))

    last_end_time = 0
    count = 0

    for start, end in schedules:
        if start >= last_end_time:
            last_end_time = end
            
            count += 1

    return count


print(find_max_meetings(M))
