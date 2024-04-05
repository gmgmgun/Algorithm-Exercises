"""
-------------------------------------------
[접근 방법]
1. 좌표 개수 n, 좌표 배열 c를 입력 받음
2. 새 배열의 요소를 값을 기준으로 0부터 1씩 증가시켜야 함
3. 변경된 가장 작은 값이 0이기 때문에 index를 활용 -> set으로 중복 제거 후 정렬
5. set을 가지고 딕셔너리로 각각의 값과 인덱스를 매핑함
4. (원본 배열의 값 = 딕셔너리의 키)를 활용해 새 배열에 딕셔너리의 값(= set의 인덱스)를 넣음  

[카테고리]
정렬
-------------------------------------------
"""

import sys

n = sys.stdin.readline()
c = list(map(int, sys.stdin.readline().split()))


def zip_coord(coords):
    uniq = sorted(set(coords))

    # 값이 몇 번째 인덱스에 있는지 딕셔너리로 매핑
    dict = {val: idx for idx, val in enumerate(uniq)}

    # 원본 배열의 각 요소를 새 인덱스로 변환
    result = [dict[coord] for coord in coords]

    return ' '.join(map(str, result))

print(zip_coord(c))

