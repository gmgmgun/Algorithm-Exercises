def find_bear_counts():
    cnt_logs = int(input())
    logs = [input().split() for _ in range(cnt_logs)]

    logs_list = []
    cur_logs = []
    cnt_bear = 0

    for log in logs:
        if log == ['ENTER']:
            if cur_logs:
                logs_list.append(cur_logs)
            cur_logs = []
        else:
            cur_logs.append(tuple(log))

    if cur_logs:
        logs_list.append(cur_logs)

    for logs in logs_list:
        cnt_bear += len(set(logs))

    print(cnt_bear)


find_bear_counts()