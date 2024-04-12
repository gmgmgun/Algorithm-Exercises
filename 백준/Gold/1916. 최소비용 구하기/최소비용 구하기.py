"""
-------------------------------------------
[접근]
1. A -> B로 가는 최소 비용 구하기
    - 다익스트라 -> 우선순위 큐(힙) 활용
2. 버스 정보를 바탕으로 그래프를 그림
3. 각 도시까지의 최소 비용 배열을 만듦. 시작점은 0, 나머지는 무한대
4. 우선순위 큐 초기화
    - 시작 도시를 큐에 넣음
5. 다익스트라 구현
    - 큐에서 비용이 최소인 요소 꺼냄
    - 그래프를 돌면서 해당 도시에서 갈 수 있는 경로를 탐색
    - 최소 비용 + 다음 경로로 가는 비용 더함
    - 갱신한 비용을 최소 비용 배열의 값과 비교해서 배열 갱신 여부 판단
    - 큐에 밀어 넣음
    - 그래프 탐색이 끝나면 처음부터 다시 시작, 위의 과정을 큐가 빌 때까지 반복함
6. 최소 비용 배열에서 목적지의 인덱스 값을 반환

[카테고리]
최단 경로
다익스트라
우선순위 큐
-------------------------------------------
"""

import heapq
import sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
L = [tuple(map(int, sys.stdin.readline().split())) for _ in range(M)]
S, E = map(int, sys.stdin.readline().split())


def find_min_fare(start, end, bus_list):
    INF = float('inf')

    # 각 도시의 인접 도시와 비용을 저장할 그래프 초기화 (인덱스 = 번호 일치시키려고 N+1로 잡음)
    graph = [[] for _ in range(N + 1)]

    # 그래프에 버스 정보 입력
    for s, e, f in bus_list:
        # 힙을 사용할 거니까 비용을 앞에 둠 (힙은 튜플의 첫번째 원소 기준으로 정렬)
        graph[s].append((f, e))

    # 결과 예시
    # [[], [[2, 2], [3, 3], [1, 4], [10, 5]], [[2, 4]], [[1, 4], [1, 5]], [[3, 5]], []]
    # 외부 배열 인덱스 = 출발 도시
    # 내부 배열 0번 요소 = 비용
    # 내부 배열 1번 요소 = 도착 도시
    # ex) [10,5] 의 경우 도시 1에서 도시 5로 가는 비용 10

    # 각 도시까지의 최소 비용 배열 초기화 *초기값은 무한대로 설정*
    dist = [INF] * (N + 1)

    # 시작 점은 0으로
    dist[start] = 0

    # 우선순위 큐 초기화
    pq = []
    heapq.heappush(pq, (dist[start], start))

    # 다익스트라 구현
    while pq:
        # 현재 가장 비용이 작은 도시를 큐에서 꺼냄
        cur_cost, cur_city = heapq.heappop(pq)

        # 이미 처리된 도시라면 스킵 (최소 비용을 구하기 때문에 비용이 높으면 더 탐색할 이유 x)
        if cur_cost > dist[cur_city]:
            continue

        # 직행 버스 있는 도시들을 확인하고 갱신
        for cost, city in graph[cur_city]:
            new_cost = cur_cost + cost  # 현재 비용에 다른 도시로 넘어가는 비용 더 함
            if new_cost < dist[city]:
                dist[city] = new_cost  # city까지의 최소비용 갱신
                # start에서 city까지 가는데 필요한 갱신된 최소비용을 큐에 추가함
                heapq.heappush(pq, (new_cost, city))


    # 목적 도시까지의 최소 비용 반환
    return dist[end]


# 결과 출력
print(find_min_fare(S, E, L))
