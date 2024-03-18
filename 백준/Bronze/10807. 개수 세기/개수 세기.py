import sys

n = int(sys.stdin.readline())
string = sys.stdin.readline().strip() 
v = sys.stdin.readline().strip()

def solution(string, v):
    answer = 0
    arr = string.split(' ')
    for el in arr:
        if el == v:
            answer += 1
    return answer

print(solution(string, v))