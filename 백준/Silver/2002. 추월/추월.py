"""
-------------------------------------------
[접근 방법]
1. N의 값을 사용자로부터 입력받음
2. 차량이 터널에 들어가는 순서와 나오는 순서의 목록을 입력받음
3. 터널에서 나오는 순서대로 각 차량을 검사하며, 해당 차량이 터널에 들어갈 때의 위치와 비교
4. 터널에 들어간 순서에서 차량이 나오는 순서의 맨 앞 차량이 일치하지 않으면 추월한 것으로 간주하고 카운트
5. 이 과정을 반복하며, 모든 차량을 확인한 후 터널 내에서 추월한 총 차량 수를 출력

[카테고리]
리스트, 구현
-------------------------------------------
"""

n = int(input())
enter_list = [input() for _ in range(n)]
exit_list = [input() for _ in range(n)]

def count_overtakes(enter, exit):
    overtakes = 0
    while enter:
        if enter[0] != exit[0]:
            overtakes += 1
            enter.remove(exit[0])
        else:
            enter.pop(0)
        exit.pop(0)
    return overtakes

print(count_overtakes(enter_list, exit_list))