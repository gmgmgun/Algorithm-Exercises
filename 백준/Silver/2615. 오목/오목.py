# 오목판의 가로 세로 길이
length = 19
# 입력 값을 2차원 배열로 변환
b = [(list(map(int, input().split()))) for _ in range(length)]


def find_omok_winner(board):

    # → ↓ ↘ ↗
    # 우측 이동, 하강 이동, 대각선 하강 이동, 대각선 상승 이동에 대한 변위
    # 예를 들어, 오른쪽으로 이동할 경우 board[0][0] -> board[0][1]
    # x 변화 -> 행이 바뀜 = 세로 탐색  y 변화 -> 열이 바뀜 = 가로 탐색
    dx = [0, 1, 1, -1]
    dy = [1, 0, 1, 1]

    for x in range(length):
        for y in range(length):
            # 2차원 배열을 순회하다가 돌이 착지된 좌표를 발견
            if board[x][y] != 0:
                focus = board[x][y]

                for i in range(4):
                    cnt = 1

                    # new_x, delta_y
                    nx = x + dx[i]
                    ny = y + dy[i]

                    # 변위를 적용한 좌표가 오목판 범위 내에 있고, 값이 연속적인 경우
                    while 0 <= nx < length and 0 <= ny < length and board[nx][ny] == focus:
                        # 카운트 증가
                        cnt += 1

                        # 육목 체크
                        if cnt == 5:
                            # 변위를 적용한 좌표가 오목판 범위 내에 있고, 이전 값이 같은 돌일 경우
                            if 0 <= x - dx[i] < length and 0 <= y - dy[i] < length and board[x - dx[i]][y - dy[i]] == focus:
                                break
                            # 변위를 적용한 좌표가 오목판 범위 내에 있고, 다음 값이 같은 돌일 경우
                            if 0 <= nx + dx[i] < length and 0 <= ny + dy[i] < length and board[nx + dx[i]][ny + dy[i]] == focus:
                                break
                            # break 가 안 걸린 경우 오목 -> 출력 후 종료
                            print(focus)
                            print(x + 1, y + 1)

                            return

                        # 카운트가 5가 될 때까지 탐색
                        nx += dx[i]
                        ny += dy[i]

    print(0)

find_omok_winner(b)

