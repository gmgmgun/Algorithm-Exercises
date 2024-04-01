n, m = map(int, input().split())
matrix_a = [list(map(int, input().split())) for _ in range(n)]
matrix_b = [list(map(int, input().split())) for _ in range(n)]


def combine_matrix(row, col, a, b):
    for i in range(row):
        print(' '.join(str(a[i][j] + b[i][j]) for j in range(col)))


combine_matrix(n, m, matrix_a, matrix_b)
