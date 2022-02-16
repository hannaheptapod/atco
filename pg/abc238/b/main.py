n = int(input())
a = list(map(int, input().split()))

s = set([0])
tmp = 0

for ai in a:
    tmp = (tmp + ai)%360
    s.add(tmp)

ls = sorted(s)
len_s = len(ls)
ls += ls

ans = 0

for i in range(len_s): ans = max(ans, (ls[i+1]-ls[i])%360)

print(ans)