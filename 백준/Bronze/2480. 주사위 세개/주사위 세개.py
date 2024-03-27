from collections import Counter

arr = input().split()
numSet = set(arr)

if len(numSet) == 1:
    print(10000 + int(arr[0]) * 1000)

elif len(numSet) == 2:
    cnt = int(Counter(arr).most_common(1)[0][0])
    print(1000 + cnt * 100)

elif len(numSet) == 3:
    arr.sort()
    print(int(arr[-1]) * 100)

else:
    print('error')