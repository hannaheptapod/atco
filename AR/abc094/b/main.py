n, m, x = map(int, input().split())
a = list(map(int, input().split()))
left = right = 0
for ai in a:
    if ai < x: left += 1
    else: right += 1
ans = min(left, right)
print(ans)