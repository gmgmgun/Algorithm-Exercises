n, m = map(int, input().split())
dic = {}
res = []
for i in range(n):
    not_seen = input()
    dic[not_seen] = 1
for i in range(m):
    not_heard = input()
    if not_heard in dic: 
        res.append(not_heard)
print(len(res))     
for name in sorted(res):
    print(name)
