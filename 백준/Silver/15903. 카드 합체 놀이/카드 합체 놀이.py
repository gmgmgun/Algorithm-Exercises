"""
-------------------------------------------
[접근 방법]
1. n과 c를 입력받음
2. n개의 카드의 값을 배열 cards로 입력받음
3. cards를 힙으로 변환
4. 힙을 사용하여 가장 작은 두 카드를 합치고, 이 과정을 c번 반복
5. 각 단계에서 카드를 합칠 때마다, 합쳐진 카드의 값을 힙에 다시 삽입
6. 모든 카드를 합친 후 모든 카드의 값의 합을 출력

[카테고리]
힙, 구현
-------------------------------------------
"""

import heapq

n, c = map(int, input().split())
cards = list(map(int, input().split()))

def min_score(c, cards):
    heapq.heapify(cards)

    for _ in range(c):
        x = heapq.heappop(cards)
        y = heapq.heappop(cards)

        sum_cards = x + y
        heapq.heappush(cards, sum_cards)
        heapq.heappush(cards, sum_cards)

    return sum(cards)

print(min_score(c, cards))