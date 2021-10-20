v, t, s, d = map(int, input().split())
ans = 'Yes'
if t <= d/v and d/v <= s:
    ans = 'No'
print(ans)