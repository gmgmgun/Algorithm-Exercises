N,L = map(int,input().split())

leak=list(map(int,input().split()))
leak.sort()

tape=1
dist=0

for i in range(1,N):
    dist +=abs(leak[i]-leak[i-1]) 
    if L > dist:
        continue
    else:
        tape+=1
        dist=0
        
print(tape)