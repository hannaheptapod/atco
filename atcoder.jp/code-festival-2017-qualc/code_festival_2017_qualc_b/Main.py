n = int(input())
a = list(map(int, input().split()))
cross = 1
for ai in a: cross *= (2 - ai%2)
ans = 3**n - cross
print(ans)