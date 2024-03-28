cnt = int(input())
strings = [input() for _ in range(cnt)]


def find_people_in_company(logs):
    log_dict = {}

    for log in logs:
        name, status = log.split()
        log_dict[name] = status

    for name in sorted(log_dict, reverse=True):
        if log_dict[name] != 'leave':
            print(name)


find_people_in_company(strings)