"""
-------------------------------------------
[시간]

[문제 해석]
사진틀 갱신하기
규칙 1. 추천 받으면 반드시 사진틀에 게시
규칙 2. 비어있는 사진틀이 없으면 추천 횟수가 가장 적은 학생 사진이랑 교체
규칙 3. minimum 추천 횟수가 동률이면 가장 오래된 사진 삭제
규칙 4. 이미 게시된 학생의 경우 추천 횟수만 증가
규칙 5. 사진이 삭제되는 경우 추천 횟수는 0으로 변겨
사진틀의 개수와 추천 결과를 추천 받은 순으로 받았을 때, 최종 후보를 구해라

[접근]
1. 가장 적은 추천 횟수는 빼야 할 경우가 생김 -> 최소 힙을 생각하자
2. 후보 별로 타임 스탬프와 추천 횟수가 필요 -> 튜플로 접근

구현해보니 최소 힙은 사용하기 힘듦. 자료구조에 저장한 요소를 업데이트 해야하는 상황이 발생할 뿐더러,
정렬 요소가 2개임.
-> 딕셔너리와 튜플을 사용하자

1. 사진틀을 딕셔너리로 구현하고, 추천 리스트를 순회하면서
   딕셔너리에 후보 번호를 키, 추천 횟수(count)와 타임 스탬프(time)를 값으로 설정
2. 사진틀에 해당 학생이 있을 경우 -> count 증가하고 현재 인덱스를 time으로 설정
3. 사진틀에 해당 학생이 없을 경우 -> 사진틀이 꽉 찼다면 count 낮은 순 -> time 낮은 순으로 최소값 제거
4. 결과적으로 사진틀엔 n명의 후보만 남게 됨



[카테고리]
구현
시뮬레이션
-------------------------------------------
"""

import sys

N = int(sys.stdin.readline())
C = int(sys.stdin.readline())
L = list(map(int, sys.stdin.readline().split()))


def find_finalists(n, l):
    frame = {}  # {학생 번호: (추천 횟수, 시간 스탬프)}

    for time, student in enumerate(l):
        if student in frame:
            # 기존 튜플을 삭제하지 않고 추천 횟수만 업데이트
            count, t = frame[student]
            frame[student] = (count + 1, t)
        else:
            if len(frame) >= n:
                # 추천 횟수가 가장 적고 가장 오래된 학생을 제거
                # min 함수로 가장 작은 값을 가진 학생을 찾음
                # 추천 횟수가 같다면 타임 스탬프(index) 빠른 순으로 정함
                oldest = min(frame.items(), key=lambda x: (x[1][0], x[1][1]))
                frame.pop(oldest[0])
            frame[student] = (1, time)  # 사진틀에 없으면 추천 횟수를 초기화해서 넣음

    # 최종 후보들을 번호 오름차순 기준으로 정렬
    finalists = sorted(frame.keys())

    return finalists


print(*find_finalists(N, L))
