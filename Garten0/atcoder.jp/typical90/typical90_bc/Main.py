n, p, q = map(int, input().split())
a = list(map(int, input().split()))
ans = 0
for i in range(n-4):
    tmpi = a[i] % p
    for j in range(i+1, n-3):
        tmpj = (tmpi * a[j]) % p
        for k in range(j+1, n-2):
            tmpk = (tmpj * a[k]) % p
            for l in range(k+1, n-1):
                tmpl = (tmpk * a[l]) % p
                for m in range(l+1, n):
                    tmpm = (tmpl * a[m]) % p
                    ans += (tmpm == q)
print(ans)