import sys
input = sys.stdin.readline

def is_inside(px, py, cx, cy, r):
    return (px - cx) ** 2 + (py - cy) ** 2 < r ** 2

T = int(input())
for _ in range(T):
    x1, y1, x2, y2 = map(int, input().split())
    n = int(input())
    count = 0

    for _ in range(n):
        cx, cy, r = map(int, input().split())
        start_in = is_inside(x1, y1, cx, cy, r)
        end_in = is_inside(x2, y2, cx, cy, r)
        
        if start_in != end_in:
            count += 1

    print(count)