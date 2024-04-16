target = int(input())
N = int(input())
broken = set(input().split() if N > 0 else [])

# 시작 채널 100에서 (+)나 (-)로만 이동할 때의 횟수
answer = abs(target - 100)

# 0번부터 999999까지 가능한 채널 검사
for i in range(1000000):
    str_i = str(i)  # 채널 번호를 문자열로 한 번만 변환
    if all(char not in broken for char in str_i):
        # 모든 숫자가 입력 가능하다면
        presses_to_reach = abs(i - target)  # 타겟 채널까지 (+)나 (-)로 이동하는 횟수
        total_presses = len(str_i) + presses_to_reach  # 숫자 입력 횟수 + 이동 횟수
        answer = min(answer, total_presses)

print(answer)