from bisect import bisect_left as bil, bisect_right as bir

N = int(input())

sq = [i**2 for i in range(N+1)]
set_sq = set(sq)

ans = 0
for i in range(1, N+1):
    for l in range(bil(sq, i), N+1):
        if not sq[l]%i: break

    for j in range(1, N-l+1):
        if not sq[l+j]%i:
            ans += -int((l-bir(sq, i*N))//j)
            break
    else: ans += 1
print(ans)
