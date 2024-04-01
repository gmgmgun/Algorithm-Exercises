n = int(input())
r = [input() for _ in range(n)]


def find_sleeping_spots(room):
    length = len(room)
    hor = 0
    ver = 0

    for row in room:
        for space in row.split('X'):
            if len(space) >= 2:
                hor += 1

    for col in range(length):
        col_space = ''.join(row[col] for row in room)
        for space in col_space.split('X'):
            if len(space) >= 2:
                ver += 1

    return hor, ver


horizontal, vertical = find_sleeping_spots(r)

print(horizontal, vertical)
