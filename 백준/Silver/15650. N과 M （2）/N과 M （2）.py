def find_perm(n, m, li):
    if len(li) == m:
        print(' '.join(map(str, li)))
        return

    for i in range(1, n + 1):
        if all(i > x for x in li):
            li.append(i)
            find_perm(n, m, li)
            li.pop()


def find_all_perms():
    n, m = map(int, input().split())
    find_perm(n, m, [])


find_all_perms()