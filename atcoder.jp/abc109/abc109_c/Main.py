from math import gcd
n, x = map(int, input().split())
l = list(map(int, input().split()))
dst = [abs(x - li) for li in l]
ans = dst[0]
for i in range(n-1):
    ans = gcd(ans, dst[i+1])
print(ans)