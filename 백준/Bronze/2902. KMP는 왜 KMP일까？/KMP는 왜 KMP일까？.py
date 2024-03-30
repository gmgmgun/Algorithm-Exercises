s = input()


def make_algorithm_name(names):
    al_name = ''
    arr = names.split('-')

    for name in arr:
        al_name += name[0]

    return al_name


print(make_algorithm_name(s))