N = int(input())
LR = [list(map(int, input().split())) for _ in range(N)]

lmax, rmin = 0, 10**9
for k in range(N):
    lmax, rmin = max(lmax, LR[k][0]), min(rmin, LR[k][1])
    
    if lmax <= rmin: x = lmax
    else: x = (lmax + rmin)//2
    
    ans = max(0, lmax - x, x - rmin)
    print(ans)
