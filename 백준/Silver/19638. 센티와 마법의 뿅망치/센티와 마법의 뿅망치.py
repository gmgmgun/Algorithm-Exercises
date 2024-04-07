"""
-------------------------------------------
[접근 방법]
1. 거인들의 키를 내림차순으로 정렬
2. 마법의 뿅망치를 사용하여 매번 가장 키가 큰 거인을 줄임
3. 센티의 키보다 큰 거인이 없을 때까지 또는 마법의 뿅망치 사용 횟수가 소진될 때까지 반복
4. 모든 거인이 센티보다 작아지면 YES와 사용한 횟수 출력, 그렇지 않으면 NO와 남은 가장 큰 거인의 키 출력

[카테고리]
구현, 그리디 알고리즘
-------------------------------------------
"""

import heapq
import sys

N,H,T=map(int, sys.stdin.readline().split())

height = []
count = 0

for i in range(N):
    heapq.heappush(height,-(int(sys.stdin.readline())))

for i in range(T):
    magic = heapq.heappop(height) * -1
    if magic == 1:
        heapq.heappush(height, -1)
    elif magic < H:
        heapq.heappush(height, magic * -1)
        break
    else:
        heapq.heappush(height, (magic // 2) * -1)
        count += 1

final = heapq.heappop(height)*(-1)

if final >= H:
    print("NO")
    print(final)
else:
    print("YES")
    print(count)