m = [list(map(int, input().split())) for _ in range(9)]


def find_max_num(matrix):
    max_num = max(max(row) for row in matrix)
    max_pos = None

    for row in range(9):
        if max_num in matrix[row]:
            max_pos = (row + 1, matrix[row].index(max_num) + 1)
            break

    return max_num, max_pos


num, (max_row, max_col) = find_max_num(m)

print(num)
print(max_row, max_col)
