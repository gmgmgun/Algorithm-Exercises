month, day = map(int, input().split())

oddDays = [1, 3, 5, 7, 8, 10, 12]
evenDays = [4, 6, 9, 11]
totalDays = 0

for i in range(1, month):
    if i in oddDays:
        totalDays += 31
    elif i in evenDays:
        totalDays += 30
    else:
        totalDays += 28

totalDays += day

days = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]

print(days[totalDays % 7])