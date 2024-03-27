import sys

price = int(sys.stdin.readline())
direct_list = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(6)]

x, y = 0, 0
prev_x, prev_y = 0, 0
area = 0

for direct in direct_list:
    prev_x, prev_y = x, y

    if direct[0] == 1:
        x += direct[1]
    elif direct[0] == 2:
        x -= direct[1]
    elif direct[0] == 3:
        y -= direct[1]
    else:
        y += direct[1]

    area += prev_x * y
    area -= x * prev_y

area = abs(area) / 2

print(int(price * area))
