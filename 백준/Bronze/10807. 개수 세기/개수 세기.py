import sys

n = int(sys.stdin.readline())
string = sys.stdin.readline().strip() 
v = sys.stdin.readline().strip()

answer = 0
arr = string.split(' ')
for el in arr:
  if el == v:
    answer += 1

print(answer);