"""
-------------------------------------------
[접근]
1. 회의실을 사용할 수 있는 최대 개수를 구해야 함.
    - 최대로 많이 회의를 예약할 수 있는 기준점을 세워서 정렬하자.
    - 시작시간 빠른 순? 종료시간이 지나치게 늦는다면 다른 회의를 못 잡음.
    - 반대로 종료시간이 빠른 순으로 정렬한다면, 남아있는 시간이 제일 많기 때문에 최대한 많은 회의를 잡을 수 있음.
    - 시작시간 == 종료시간인 회의도 있으므로 시작 시간도 2차적으로 정렬 해야 함.
    반례) 1-2 / 3-3 / 2-3 
    시작시간 정렬을 하지 않아서 1-2 이후 3-3이 먼저 처리된다면 2-3은 누락되어버림

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
