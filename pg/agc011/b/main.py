n, a = int(input()), list(map(int, input().split()))

a.sort()
sm = [a[0]]
for i in range(1, n): sm += [sm[i-1] + a[i]]
sm = sm[::-1]

for i in range(n-1):
    if sm[i] <= sm[i+1]*3: continue
    else:
        ans = i+1
        break
else: ans = n

print(ans)