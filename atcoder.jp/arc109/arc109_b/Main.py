n = int(input())

ok, ng = 0, n+1
while ok+1 < ng:
    md = (ok + ng)//2
    if md*(md+1)//2 <= n+1: ok = md
    else: ng = md

ans = n-ok + 1
print(ans)
