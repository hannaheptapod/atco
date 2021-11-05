n = int(input())
d = list(map(int, input().split()))
m = int(input())
t = list(map(int, input().split()))
d.sort()
t.sort()
id = it = 0
while id < n and it < m:
    if d[id] > t[it]: break
    elif d[id] == t[it]:
        id += 1
        it += 1
    else: id += 1
if it == m: ans = 'YES'
else: ans = 'NO'
print(ans)