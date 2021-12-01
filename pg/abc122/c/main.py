from bisect import bisect_left as bil, bisect_right as bir
n, q = map(int, input().split())
s = input()
ls = []
prev = ''
for i in range(n):
    si = s[i]
    if prev == 'A' and si == 'C': ls += [i]
    prev = si
for _ in range(q):
    l, r = map(int, input().split())
    ans = bir(ls, r-1) - bil(ls, l)
    print(ans)