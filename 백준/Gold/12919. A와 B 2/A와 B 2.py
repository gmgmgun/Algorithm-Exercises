"""
-------------------------------------------
[시간]

[문제 해석]
A와 B로만 이루어진 문자열 S와 T를 입력 받음
동작 1. S += 'A'
동작 2. S += 'B' , S = S[::-1]
해당 동작들을 섞어서 S가 T가 될 수 있는지 검사

[접근]
거꾸로 생각하기
단편적으로 역추적하면 전체 경우의 수를 확인할 수 없음
뒤집을 때 오염되기 때문
예를 들어 BABA를 검사할 때
단순히 T를 자르면서 반복문을 돌린다면 BABA -> BAB -> BA -> B라는 결과가 나오지만
A -> BA -> BAB -> BABA도 가능함
그래서 재귀로 모든 경우의 수를 탐색해야 함
재귀를 사용 안해도 풀 수 있을텐데 이따 고민해볼 것

[카테고리]
브루트포스
재귀
-------------------------------------------
"""

import sys

S = sys.stdin.readline().strip()
T = sys.stdin.readline().strip()

answer = 0


def a_and_b(s, t):
    global answer
    if t == s:
        answer = 1
        return

    if len(t) == 0:
        return

    if t[-1] == 'A':
        a_and_b(s, t[:-1])

    if t[0] == 'B':
        a_and_b(s, t[1:][::-1])


a_and_b(S, T)

print(answer)
