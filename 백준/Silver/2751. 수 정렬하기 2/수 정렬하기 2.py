import sys
n = int(sys.stdin.readline())
nums = [int(sys.stdin.readline()) for _ in range(n)]

print('\n'.join(map(str, sorted(nums))))