from sys import stdin
input = stdin.readline

T = int(input())

for _ in range(T):
    clothes = {}
    n = int(input())
    for _ in range(n):
        cName, cType = input().rstrip().split()
        # 해당 종류의 존재 유무에 따라, (개수) 추가
        if not cType in clothes:
            clothes[cType] = 1
        else:
            clothes[cType] += 1
            
    count = 1
    for i in clothes:
        count *= (clothes[i] + 1) # 해당 종류의 의상을 착용하지 않아도 되는 경우도 포함 (+1)
    print(count - 1) # 모든 의상을 착용하지 않은 경우를 제외 (-1)