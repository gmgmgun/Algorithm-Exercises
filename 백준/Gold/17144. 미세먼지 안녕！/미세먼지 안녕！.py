"""
-------------------------------------------
[접근]
1. 미세먼지 확산 -> 공기청정기 동작 순으로 구현
2. 좌표 이동이 필요 -> delta 활용
3. 공기청정기 위와 아래는 반대 방향으로 돌음 -> 상단부, 하단부로 분기해서 처리
4. T초 후의 변화를 확인하기 위해 (먼지 확산 -> 상단부 가동 -> 하단부 가동)을 T만큼 반복
5. 반복 이후 grid가 변경되었기 때문에 grid를 다시 순회하면서 0보다 큰 요소(공기청정기가 아닌 좌표)의 값만 합산
6. 합산한 결과를 출력

[카테고리]
구현, 시뮬레이션
-------------------------------------------
"""

import sys

R, C, T = map(int, sys.stdin.readline().split())  # 가로 세로 시간(초)
grid = [list(map(int, sys.stdin.readline().split())) for _ in range(R)]  # 집을 그리드로 구현

# delta 값 반시계방향으로 설정, 방향은 항상 오른쪽부터 시작함 (우 상 좌 하)
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]


# 변위 값을 적용하는 함수
def cal_new_pos(x, y, idx):
    nx = x + dx[idx]
    ny = y + dy[idx]

    return nx, ny


# 미세먼지 확산 구현
def spread_dust(dusts):
    def spread(x, y, density):
        count = 0  # 확산 횟수
        spread_amount = density // 5  # 확산 후 농도

        for idx in range(4):  # 전 방향으로 확산
            nx, ny = cal_new_pos(x, y, idx)  # 이동 후 새 좌표

            # 새 좌표가 범위를 초과하거나 공기청정기 위치면 무시
            if 0 <= nx < R and 0 <= ny < C and grid[nx][ny] != -1:
                grid[nx][ny] += spread_amount
                count += 1

        grid[x][y] -= spread_amount * count  # 확산된 만큼 매개 좌표에서 농도 감소

    # 먼지를 다 확산 시킬 때까지 반복
    while dusts:
        dust = dusts.pop()
        spread(*dust)


# 공기청정기 동작 구현
def clean_air(pos, direct):
    c_x, c_y = pos  # 공기 청정기의 x, y 좌표

    # 바람이 사출되는 위치
    x = c_x  # 높이는 공기청정기와 동일
    y = c_y + 1  # 공기 청정기 오른쪽에서 사출되므로 + 1

    idx = 0  # delta 배열 인덱스 (우 방향)
    wind = 0  # 공기청정기에서 사출한 바람

    while True:
        nx, ny = cal_new_pos(x, y, idx)  # 바람 이동 후 새 좌표

        # 벽에 닿기 전까진 한 방향으로 계속 진행
        if nx >= R or ny >= C or nx < 0 or ny < 0:
            # 벽에 닿았다면 방향 변경
            # 상단부(반시계방향): 우 -> 상 -> 좌 -> 하 순으로 변경
            # 하단부(시계방향): 우 -> 하 -> 좌 -> 상 순으로 변경
            idx = (idx + direct) % 4
            continue  # 방향만 변경하고 다시 계속 진행

        if x == c_x and y == c_y:  # 사출된 바람이 돌아오면 while문 탈출
            break

        # 미세먼지가 바람에 의해 밀려났으므로 현재 위치의 미세먼지는 wind, 밀려난 미세먼지는 wind에 저장
        grid[x][y], wind = wind, grid[x][y]
        # 바람이 이동한 좌표로 스위칭
        x, y = nx, ny


def goodbye_dust():
    dusts = []  # 미세먼지의 좌표를 저장할 배열
    cleaner = []  # 공기청정기의 좌표를 저장할 배열

    # (x 좌표, y 좌표, 먼지 농도)를 저장할 최초 그래프 생성
    for x, col in enumerate(grid):
        for y, density in enumerate(col):
            if density > 0:
                dusts.append((x, y, density))
            if density == -1:
                cleaner.append((x, y))

    # T만큼 반복
    for _ in range(T):
        spread_dust(dusts)  # 미세먼지 확산
        clean_air(cleaner[0], 1)  # 공기청정기 상단부 가동
        clean_air(cleaner[1], -1)  # 공기청정기 하단부 가동

        # 바뀐 grid를 순회하면서 dusts를 채움
        for x, col in enumerate(grid):
            for y, density in enumerate(col):
                if density > 0:
                    dusts.append((x, y, density))

    remained_dust = sum(dusts[i][2] for i in range(len(dusts)))

    # 합산한 결과를 출력
    print(remained_dust)

goodbye_dust()
