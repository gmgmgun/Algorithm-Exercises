a_1, a_0 = map(int, input().split())
c = int(input())
n_0 = int(input())


def is_big_o(a_1, a_0, c, n_0):

    for n in range(n_0,100):
        if a_1 * n + a_0 > c * n:
            return 0

    return 1


print(is_big_o(a_1, a_0, c, n_0))