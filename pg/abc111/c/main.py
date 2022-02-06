n = int(input())
v = list(map(int, input().split()))
l = [{}, {}]
for i in range(n):
    if v[i] not in l[i%2]: l[i%2][v[i]] = 0
    l[i%2][v[i]] += 1
ls = [sorted(li.items(), key=lambda x:x[1], reverse=True) for li in l]
if ls[0][0][0] != ls[1][0][0]: ans = n - (ls[0][0][1] + ls[1][0][1])
elif ls[0][0][1] == n//2:
    if ls[1][0][1] == n//2: ans = n//2
    else: ans = n//2 - ls[1][1][1]
elif ls[1][0][1]: ans = n//2 - ls[0][1][1]
else: ans = n - max(ls[0][1][1] + ls[1][0][1], ls[0][0][1] + ls[1][1][1])
print(ans)