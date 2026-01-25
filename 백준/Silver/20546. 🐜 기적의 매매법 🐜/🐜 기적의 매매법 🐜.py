import sys

input = sys.stdin.readline

n = int(input().rstrip())

chart = list(map(int, input().rstrip().split()))

BNP = [n, 0]
TIMING = [n, 0] 

for i in range(len(chart)): 
    BNP[1] += (BNP[0] // chart[i]) 
    BNP[0] -= (BNP[0] // chart[i] * chart[i])


for i in range(11): 
    check = chart[i:i+4]
    check_up = 0
    check_down = 0

    for j in range(3):
        if check[j+1] > check[j]: 
            check_up+=1
        if check[j+1] < check[j]: 
            check_down+=1

    if check_down == 3: 
        TIMING[1] += (TIMING[0] // chart[i+3]) 
        TIMING[0] -= (TIMING[0] // chart[i+3] * chart[i+3])

    elif check_up == 3: 
        TIMING[0] += (TIMING[1] * chart[i+3])
        TIMING[1] = 0

BNP = chart[13] * BNP[1] + BNP[0]
TIMING = chart[13] * TIMING[1] + TIMING[0]

if BNP>TIMING:
    print("BNP")
elif BNP < TIMING:
    print("TIMING")
else:
    print("SAMESAME")