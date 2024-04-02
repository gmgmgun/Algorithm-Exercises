s, s_arr = int(input()), list(map(int, input().split()))
n = int(input())
n_arr = [list(map(int, input().split())) for _ in range(n)]


def on_off_switch(switch):
    if switch == 1:
        return 0
    else:
        return 1


def on_off_switches(switches, students):
    for student in students:
        gender, number = student[0], student[1]

        if gender == 1:
            for i in range(number, len(switches) + 1, number):
                switches[i - 1] = on_off_switch(switches[i - 1])

        else:
            switches[number - 1] = on_off_switch(switches[number - 1])
            for i in range(1, len(switches)):
                if number - 1 - i >= 0 and number - 1 + i < len(switches) and switches[number - 1 - i] == switches[number - 1 + i]:
                    switches[number - 1 - i] = on_off_switch(switches[number - 1 - i])
                    switches[number - 1 + i] = on_off_switch(switches[number - 1 + i])
                else:
                    break

    for i in range(len(switches)):
        print(switches[i], end=" ")
        if (i + 1) % 20 == 0:
            print()


on_off_switches(s_arr, n_arr)


