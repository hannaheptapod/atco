N, a, b = map(int, input().split())
A = sorted(map(int, input().split()))

ok, ng = A[0], A[-1]
ans = ok
while ok+1 < ng:
    md = (ok+ng)//2

    flag = False
    cnt = 0
    for ai in A:
        if ai > md: break

        if not (md-ai)%a: flag = True
        cnt += -int(-(md-ai)//a)

    for ai in A[::-1]:
        if ai <= md: break

        if not (ai-md)%b: flag = True
        cnt -= (ai-md)//b

    if cnt <= 0:
        if flag: ans = max(ans, md)
        ok = md
    else: ng = md

print(ans)
