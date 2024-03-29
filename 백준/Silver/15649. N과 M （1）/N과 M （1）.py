def find_comb(n, m, li):
    if len(li) == m:
        print(' '.join(map(str, li)))
        return

    for i in range(1, n + 1):
        if i not in li:
            li.append(i)
            find_comb(n, m, li)
            li.pop()


def find_all_combs():
    n, m = map(int, input().split())
    find_comb(n, m, [])


find_all_combs()
