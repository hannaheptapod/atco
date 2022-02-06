k, t = map(int, input().split())
a = list(map(int, input().split()))

sm = sum(a)
mx = max(a)

ans = max(0, 2*mx - sm - 1)

print(ans)