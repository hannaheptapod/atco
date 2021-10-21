n, k = map(int, input().split())
a = list(map(int, input().split()))
mod = 10**9 + 7
l = r = 0
for i in range(n):
    ai = a[i]
    for j in range(n):
        if ai > a[j]:
            if i < j: r += 1
            else: l += 1
ans = (k-1)*k*l//2 + k*(k+1)*r//2
ans %= mod
print(ans)