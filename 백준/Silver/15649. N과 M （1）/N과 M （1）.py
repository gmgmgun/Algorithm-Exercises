def find_comb(n, m, li, used_set):
    if len(li) == m:
        print(' '.join(map(str, li)))
        return

    for i in range(1, n + 1):
        if i not in used_set:
            used_set.add(i)
            li.append(i)
            find_comb(n, m, li, used_set)
            li.pop()
            used_set.remove(i)


def find_all_combs():
    n, m = map(int, input().split())
    find_comb(n, m, [], set())


find_all_combs()