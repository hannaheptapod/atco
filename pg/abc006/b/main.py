n = int(input())
MOD = 10007

a = [0, 0, 1]
for i in range(n-3): a[i%3] = sum(a)%MOD

ans = a[(n-1)%3]

print(ans)