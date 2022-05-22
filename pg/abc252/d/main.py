from collections import Counter

N = int(input())
A = list(map(int, input().split()))

cnt = list(Counter(A).values())
l = len(cnt)
if l < 3: ans = 0
else:
    sq = [ci**2 for ci in cnt]

    x = [0]*(l-1) + [cnt[-1]]
    y = [0]*(l-1) + [cnt[-1]**2]

    for i in range(l-2, -1, -1):
        x[i] = x[i+1] + cnt[i]
        y[i] = y[i+1] + cnt[i]**2

    ans = sum(cnt[i]*(x[i+1]**2 - y[i+1]) for i in range(l-2))//2

print(ans)
