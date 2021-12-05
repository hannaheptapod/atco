a, b, x = map(int, input().split())
ok = 0
ng = 10**9 + 1
while ok+1 < ng:
    md = (ok + ng) // 2
    if a*md + b*len(str(md)) <= x: ok = md
    else: ng = md
print(ok)