n, k = map(int, input().split())
a = list(map(int, input().split()))
a.sort(reverse=True)
maxa = a[0]
suma = sum(a)

if suma <= k:
    ans = 0
    for ai in a: ans += (ai + 1) * ai // 2

else:
    ng = 0
    ok = maxa + 1
    cnt = 0

    while ok - ng > 1:
        md = ng + (ok - ng) // 2
        sm = 0

        for ai in a:
            if ai >= md: sm += ai - md + 1
            else: break
        
        if sm <= k:
            ok = md
            cnt = sm
        else: ng = md
    
    ans = (ok - 1) * (k - cnt)
    for ai in a:
        if ai >= ok:
            ans += (ai + ok) * (ai - ok + 1) // 2
        else: break

print(ans)