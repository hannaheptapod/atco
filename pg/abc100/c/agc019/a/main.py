q, h, s, d = map(int, input().split())
n = int(input())
ans = 0
p = min(8*q, 4*h, 2*s, d)
ans += p*(n//2)
n %= 2
p = min(4*q, 2*h, s)
ans += p*n
print(ans)