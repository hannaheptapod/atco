N = int(input())
R = list(map(int, input().split()))


diff = [R[i+1]-R[i] for i in range(N-1)]
tot = [0]
ans = 2
for di in diff:
    if tot[-1]*di >= 0:
        tot[-1] += di
        continue
    tot.append(di)
    ans += 1
if ans == 2: ans = 0

print(ans)
