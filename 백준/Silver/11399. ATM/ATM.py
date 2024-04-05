"""
-------------------------------------------
[접근 방법]
1. 사람 수 n과 각각 인출하는데 필요한 시간을 배열 l로 입력 받음
2. 시간의 합을 최소화하려면 필요 시간이 적은 사람부터 인출해야 함
3. 배열을 내림차순 정렬해 적은 사람부터 pop() 실행
4. 인출에 걸리는 시간 = 이전까지 사람들의 시간의 합 + 내가 필요한 시간
5. 그러므로 실행할 때마다 이전 결과값을 계속 더 해줌
6. 실행 결과 또한 누적시켜서 필요 시간의 총합을 도출

[카테고리]
그리디, 정렬
-------------------------------------------
"""

import sys

n = sys.stdin.readline()
l = list(map(int,sys.stdin.readline().split()))

def find_min_minutes(line):
  line.sort(reverse=True)
  
  minutes = 0
  result = 0
  
  while line:
    minutes += line.pop()
    result += minutes  
  
  return result

print(find_min_minutes(l))